import pika  # for sending events to RabbitMQ
import json
from vars import AMPQ_BROKER_URL

params = pika.URLParameters(
    AMPQ_BROKER_URL)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()  # creating channel


def publish(method, body):
    """Publishing ampq channel connection with admin microservice's consumer"""

    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="admin",
                          body=json.dumps(body), properties=properties)
