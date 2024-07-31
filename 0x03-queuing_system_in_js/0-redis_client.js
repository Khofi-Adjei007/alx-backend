import redis from 'redis';

const client = redis.createClient();

// Event handler for successful connection to Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors with the Redis server
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
