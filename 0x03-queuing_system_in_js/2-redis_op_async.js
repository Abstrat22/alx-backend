// connects to a redis server
import redis from "redis";
import {promisify} from "util";

// create a redis client
const client = redis.createClient();


client.on("error", err => console.log(`Redis client not connected to the server: ${err}`));
client.on("connect", () => console.log(`Redis client connected to the server`));

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// set the schoolName to value on the redis server
// and print a confirmation
function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);

}
// Async function to Get value of the key, "schoolName" from the redis server
async function displaySchoolValue(schoolName){
    try{ const value = await getAsync(schoolName);
        console.log(value);
    } catch (err){console.error(`Error: ${err}`);}

}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');