import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

/**
 * Sets a new key-value pair in Redis.
 * @param {String} schoolName - The key for the Redis store.
 * @param {String} value - The value associated with the key.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Retrieves and displays the value associated with a given key from Redis.
 * @param {String} schoolName - The key to retrieve the value for.
 */
async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
