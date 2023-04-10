from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from ws import models
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        '''
        当有客户端向后端发送websocket连接请求时，自动触发该函数
        :param message:
        :return:
        '''
        # 服务器允许客户端创建连接
        self.accept()

    def websocket_receive(self, message):
        '''
        浏览器基于websocket向后端发送数据，自动触发接受消息，并且处理信息
        :param message:
        :return:
        '''
        # 输出消息
        account = self.scope['url_route']['kwargs']['code']
        models.TblUser.objects.create(account=account, type=4)
        print(account)
        # 服务端向前端回消息
        self.send('服务器收到了你的消息：%s' % (message['text']))

    def disconnect(self, message):
        '''
        客户端与服务端断开连接时，自动触发该函数
        :param message:
        :return:
        '''
        print('断开连接')
        raise StopConsumer()