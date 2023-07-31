import redis
import threading

class Subscriber(threading.Thread):
    def __init__(self, host='localhost', port=6379, db=0):
        super(Subscriber, self).__init__()
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)
        self.pubsub = self.redis_client.pubsub()
        self.channels = set()

    def subscribe(self, channel, callback):
        self.channels.add(channel)
        self.pubsub.subscribe(channel)
        self.callback = callback

    def unsubscribe(self, channel):
        self.channels.discard(channel)
        self.pubsub.unsubscribe(channel)

    def run(self):
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                channel = message['channel'].decode('utf-8')
                if channel in self.channels:
                    data = message['data'].decode('utf-8')
                    self.callback(channel, data)
