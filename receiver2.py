"""
消费者/接收消息方
"""
import pika

# 远程主机的RabbitMQ Server设置的用户名密码
credentials = pika.PlainCredentials('svcansible', 'gcstub')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.148.176.65', 5672, '/', credentials))

# 创建通道
channel = connection.channel()
# 声明队列
channel.queue_declare(queue='restart')
"""
你可能会问为什么我们还要声明队列呢? 我们在之前代码里就有了,但是前提是我们已经知道了我们已经声明了代码,但是我们可能不太确定
谁先启动~ So如果你们100%确定也可以不用声明,但是在很多情况下生产者和消费者都是分离的.所以声明没有坏处
"""


# 订阅的回调函数这个订阅回调函数是由pika库来调用的
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 定义通道消费者参数
channel.basic_consume(on_message_callback=callback,
                      queue='restart',
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()