// connects to a redis server
import redis from "redis";

// create a redis client
const client = redis.createClient();


client.on("error", err => console.log(`Redis client not connected to the server: ${err}`));
client.on("connect", () => console.log(`Redis client connected to the server`));

// set the schoolName to value on the redis server
// and print a confirmation
function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);

}
// Get value of key, "schoolName" from the redis server
function displaySchoolValue(schoolName){
    client.get(schoolName, (err, value) => {
        if(err){
            console.log(err);
            throw err
        }
        console.log(value)
    });
    

}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');