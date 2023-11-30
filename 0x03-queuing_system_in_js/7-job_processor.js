// creates a queue with kue

import kue from "kue";


const blacklistNumbers = ["4153518780", "4153518781"];


// create a queue
const queue = kue.createQueue();

// sends a notification to the "phoneNumber"
function sendNotification(phoneNumber, message, job, done) {
    // Track the progress of the job (0%)
    job.progress(0, 100);
    // Check blacklisted phone number
    if (blacklistNumbers.includes(phoneNumber)) {
        const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
        // Fail the job with an Error object and the error message
        done(new Error(errorMessage));

    }
    // Track the progress of the job (50%)
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}
// Process jobs from the "push_notification_code_2"
// queue two jobs at a time
queue.process("push_notification_code_2", 2, (job, done) => {
    const { phoneNumber, message } = job.data;

    // Call the sendNotification function with the job data
    sendNotification(phoneNumber, message, job, done);
});