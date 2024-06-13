#!/usr/bin/env python3

import base64
import json

import kafka
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


def plot_and_predict(model, pixels):
    test = tf.constant([pixels])
    tf.shape(test)
    test_norm = tf.cast(test, tf.float32) / 255.

    prediction = model.predict(test_norm)
    number = tf.nn.softmax(prediction).numpy().argmax()
    print(f"number: {number}")
    
    pixels_array = np.asarray(pixels)
    raw_img = np.split(pixels_array, 28)
    plt.imshow(raw_img)
    plt.title(number)
    plt.axis("off")
    plt.show()

    return number


def classify_stream(model):
    consumer = kafka.KafkaConsumer(
        "tf.public.mnist_test",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        consumer_timeout_ms=1000,enable_auto_commit=True,
        group_id="mnist_classifier")

    def serializer(message):
        return json.dumps(message).encode('utf-8')
    
    producer = kafka.KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=serializer
    )
    
    for msg in consumer:
        val_json = json.loads(msg.value)
        pixels = base64.b64decode(val_json['payload']['after']['pixels'])
        a  = [int(n) for n in pixels]
        number = plot_and_predict(model, a)
        producer.send('mnist_result', {'result': int(number), 'pixels': val_json['payload']['after']['pixels']})
        producer.flush()


model = tf.keras.models.load_model('./mnist_model.keras')
classify_stream(model)
