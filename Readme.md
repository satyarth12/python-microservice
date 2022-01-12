# Python Microservice Architecture
    > This is a mini yet important project to understand the fundamentals of a microservice application.
    > Tech Stacks Used are:

    -   **Django Framework**: Django along with Django Rest-Framework were used to make the admin microservice (out of two microservices).
            Django helped in rapid development and clean, pragmatic design, eventually helped in setting up the admin APIs to manage the dashboard side.

    -   **Flask Framework**: Flask is a lightweight web application framework which was used to make the second microservice, main.
            Flask app has only two endpoints which eventually makes the interal API call to the admin microservice with the help of rabbitMq and pika.
            SQLAlchemy + Flask provides a good setup to talk with and configure MYSQL.
    
    -   **RabbitMQ**: RabbitMQ is a message broker: it accepts and forwards messages. RabbitMQ, and messaging in general, uses some jargon.
            - Producing means nothing more than sending. A program that sends messages is a producer.
            - Consuming has a similar meaning to receiving. A consumer is a program that mostly waits to receive messages.
            - A queue is a sequential data structure with two primary operations: an item can be enqueued (produced) at the tail and dequeued (consumed) from the head.

    -   **Pika**: Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.

    -   **MySQL**: MySQL is an open-source relational database management system that facilitates effective management of databases by connecting them to the software. It is a  
            stable, reliable and powerful solution.


![python_microservice](https://user-images.githubusercontent.com/45152281/149139627-e3a14a46-70a2-4277-81a4-b1e9b00ac483.jpg)
