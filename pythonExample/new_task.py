import sys
import pika

messages =' '.join(sys.argv[1:]) or 'Hello World'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tasks')
channel.basic_publish(exchange='', routing_key='tasks', body=messages)
print('[x] Send %r' %messages)
