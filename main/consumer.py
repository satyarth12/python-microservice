"""Consumer code for the main microservice
which it receives from admin app's microservice
"""

import pika  # for sending events to RabbitMQ
import json

from main import Product, db

params = pika.URLParameters(
    "amqps://lvhcfubi:aZ3GVvZLrrjG3ufYnh1nqN1KsK9bpZJp@puffin.rmq2.cloudamqp.com/lvhcfubi")

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()  # creating channel

channel.queue_declare(queue="main")


def callback(chnl, method, properties, body):
    print("RECEIVED IN MAIN")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(
            id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('product created')

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('product updated')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product deleted')


# consuming the data packets sent by the producer
channel.basic_consume(
    queue="main", on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
