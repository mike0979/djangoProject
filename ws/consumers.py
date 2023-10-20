from channels.generic.websocket import WebsocketConsumer
import json
import logging

# 获取logger对象
logger = logging.getLogger('django')

# 用于跟踪客户端连接的字典
connected_clients = {}

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # 获取客户端传递的code参数
        self.code = self.scope['url_route']['kwargs']['code']
        # 将该连接添加到connected_clients字典中
        connected_clients[self.code] = self

    def websocket_receive(self, event):
        message_text = event.get('text')
        # 处理从客户端接收的消息
        # 这里可以添加自定义的处理逻辑
        self.send(f'服务器收到了你的消息：{message_text}')

    def disconnect(self, close_code):
        # 在断开连接时从connected_clients字典中移除该连接
        del connected_clients[self.code]

def send_message_to_client(code, message):
    # 通过code找到对应的客户端连接，并向其发送消息
    if code in connected_clients:
        connected_clients[code].send(json.dumps(message))
        logger.info(message)
    else:
        logger.info(f"Client with code {code} not found.")