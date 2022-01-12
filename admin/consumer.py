"""Consumer code for the admin microservice
which it receives from main app's microservice
"""

from products.models import Products
import pika  # for sending events to RabbitMQ
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()


params = pika.URLParameters(
    "amqps://lvhcfubi:aZ3GVvZLrrjG3ufYnh1nqN1KsK9bpZJp@puffin.rmq2.cloudamqp.com/lvhcfubi")

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()  # creating channel

channel.queue_declare(queue="admin")


def callback(chnl, method, properties, body):
    id_ = json.loads(body)

    if properties.content_type == 'product_liked':
        instance = Products.objects.get(id=id_)
        instance.likes = instance.likes + 1
        instance.save()


# consuming the data packets sent by the producer
channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
