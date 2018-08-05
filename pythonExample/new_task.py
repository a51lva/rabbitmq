import sys
import pika

messages =' '.join(sys.argv[1:]) or 'Hello World'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='tasks2',durable=True)
channel.basic_publish(exchange='', routing_key='tasks2', body=messages,
                        properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
                      ))
print('[x] Send %r' %messages)
connection.close()

