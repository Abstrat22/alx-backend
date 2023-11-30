// connects to a redis server
import redis from "redis";

// create a redis client
const subscriberClient = redis.createClient();


// Set event handlers for subscriberClient
subscriberClient.on("error", err => console.log(`Redis client not connected to the server: ${err}`));
subscriberClient.on("connect", () => console.log(`Redis client connected to the server`));

// Subscribe to the "holberton school channel"
subscriberClient.subscribe("holberton school channel");

// Handle incoming messages
subscriberClient.on("message", (channel, message) => {
    console.log(message);
      // Check if the message is "KILL_SERVER"
  if (message === "KILL_SERVER") {
    // Unsubscribe and quit when receiving "KILL_SERVER"
    subscriberClient.unsubscribe();
  }
});