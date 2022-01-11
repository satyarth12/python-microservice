import pika  # for sending events to RabbitMQ
import json

params = pika.URLParameters(
    "amqps://lvhcfubi:aZ3GVvZLrrjG3ufYnh1nqN1KsK9bpZJp@puffin.rmq2.cloudamqp.com/lvhcfubi")

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()  # creating channel


def publish(method, body):
    """Publishing ampq channel connection"""

    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="admin",
                          body=json.dumps(body), properties=properties)
