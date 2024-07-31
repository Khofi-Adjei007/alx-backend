#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue();

/**
 * Sends a notification message to a specified phone number.
 * @param {String} phoneNumber - The recipient's phone number.
 * @param {String} message - The notification message.
 */
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber},`,
    'with message:',
    message,
  );
};

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
