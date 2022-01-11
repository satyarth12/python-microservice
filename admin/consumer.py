"""Consumer code for the admin microservice
"""

import pika  # for sending events to RabbitMQ

params = pika.URLParameters(
    "amqps://lvhcfubi:aZ3GVvZLrrjG3ufYnh1nqN1KsK9bpZJp@puffin.rmq2.cloudamqp.com/lvhcfubi")

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()  # creating channel

channel.queue_declare(queue="admin")


def callback(chnl, method, properties, body):
    pass


# consuming the data packets sent by the producer
channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
