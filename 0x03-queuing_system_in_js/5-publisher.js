// connects to a redis server
import redis from "redis";

// create a redis client
const publisherClient = redis.createClient();


// Set event handlers for publisherClient 
publisherClient .on("error", err => console.log(`Redis client not connected to the server: ${err}`));
publisherClient .on("connect", () => console.log(`Redis client connected to the server`));

// Publishes a message to a channel
function publishMessage(message, time){
    setTimeout(() => {
        console.log(`About to send ${message}`);
        // publish message to the channelS
        publisherClient.publish("holberton school channel", message);
    }, time);



}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);