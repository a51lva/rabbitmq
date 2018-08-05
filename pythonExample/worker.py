#Round-robin dispatching
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tasks')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")

channel.basic_consume(callback,queue='tasks',no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()