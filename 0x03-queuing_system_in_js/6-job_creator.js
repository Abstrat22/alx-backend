// creates a queue with kue

import kue from "kue";

// create a queue instance
const queue = kue.createQueue();

// Object containing job data
const jobData = {
    phoneNumber: "0247450258",
    message: "Hello from the center of the earth!",
  }

// Create a job in the "push_notification_code" queue
const job = queue.createJob("push_notification_code", jobData);
 
// Event handler for successful job creation
job.on("enqueue", () => {
    console.log(`Notification job created: ${job.id}`);
  });

// Event handler for successful job completion
job.on("complete", () => {
  console.log("Notification job completed");
});

// Event handler for job failure
job.on("failed", (err) => {
  console.log(`Notification job failed: ${err}`);
});

// Save the job to the queue
job.save((err) => {
  if (err) {
    console.error("Error creating job:", err);
  } else {
    console.log("Job saved to the queue.");
  }
});
