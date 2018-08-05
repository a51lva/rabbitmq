#Message acknowledgment and durability
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tasks2',durable=True) #Message durability

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1) #This tells RabbitMQ not to give more than one message to a worker at a time
channel.basic_consume(callback,queue='tasks2')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()