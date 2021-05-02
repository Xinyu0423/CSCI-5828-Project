import pika
import requests
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
response=requests.get("http://csci5828api.herokuapp.com/api/product")
channel.basic_publish(exchange='',
                      routing_key='products',
                      body=response)
                      
connection.close()
