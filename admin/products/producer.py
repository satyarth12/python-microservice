import pika  # for sending events to RabbitMQ
import json
from django.conf import settings

params = pika.URLParameters(
    settings.AMPQ_BROKER_URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()  # creating channel


def publish(method, body):
    """Publishing ampq channel connection with main microservice's consumer"""

    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="main",
                          body=json.dumps(body), properties=properties)
