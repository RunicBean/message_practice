import pika

credentails = pika.PlainCredentials('svcansible', 'gcstub')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.148.176.65', 5672, '/', credentials=credentails))

channel = connection.channel()

channel.queue_declare(queue='restart')
for i in range(100):
    channel.basic_publish(exchange='', routing_key='restart', body='#{} World'.format(i))
print("向队列hello添加数据结束")
# 缓冲区已经flush而且消息已经确认发送到了RabbitMQ中，关闭通道
connection.close()