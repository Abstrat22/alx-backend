// creates a queue with kue

import kue from "kue";

// create a queue instance
const queue = kue.createQueue();


// sends a notification to the "phoneNumber"
function sendNotification(phoneNumber, message){
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Queue process to listen to new jobs on "push_notification_code"
queue.process("push_notification_code", (job, done) => {

    // Extract data from the job
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function with the job data
    sendNotification(phoneNumber, message);

})