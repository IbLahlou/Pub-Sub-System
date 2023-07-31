import redis

class Subscriber:
    def __init__(self):
        self.redis_host = 'localhost'
        self.redis_port = 6379

    def subscribe_channel(self):
        redis_client = redis.StrictRedis(host=self.redis_host, port=self.redis_port)

        # Subscribe to the channel named 'pub_sub_channel'
        pub_sub = redis_client.pubsub()
        pub_sub.subscribe('pub_sub_channel')

        # Start listening for messages
        for message in pub_sub.listen():
            if message['type'] == 'message':
                print(f"Received message: {message['data'].decode('utf-8')}")

if __name__ == "__main__":
    subscriber = Subscriber()
    subscriber.subscribe_channel()
