const expressPort = 3000
const kafkaBroker  = '127.0.0.1'

const { Kafka, logLevel } = require('kafkajs')

const express = require('express');
const { createServer } = require('node:http');
const { Server } = require('socket.io');

const app = express();
const server = createServer(app);
const io = new Server(server);

const kafka = new Kafka({
  logLevel: logLevel.INFO,
  brokers: [`${kafkaBroker}:9092`],
  clientId: 'mnist-consumer',
})

const topic = 'mnist_result'
const consumer = kafka.consumer({groupId: 'node-consumer-group7'})

const run = async (socket) => {
  await consumer.connect()
  await consumer.subscribe({ topic, fromBeginning: true })
  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
	const json_value = message.value
	const value = JSON.parse(json_value)
	console.log(value.result)
	socket.emit('mnist-send', value)
    },
  })
}


app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
})

var consuming = false
io.on('connection', (socket) => {
    console.log('a user connected')
    if (!consuming) {
	console.log('starting kafka consumer')
	run(socket).catch(e => console.error(`[kafka consumer] ${e.message}`, e))
	consuming = true
    }
});

server.listen(expressPort, () => {
  console.log(`Listening on port ${expressPort}`)
})

