import redis

class Publisher:
    def __init__(self):
        self.redis_host = 'localhost'
        self.redis_port = 6379

    def publish_message(self):
        redis_client = redis.StrictRedis(host=self.redis_host, port=self.redis_port)
        while True:
            message = input("Enter a message to publish (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            # Publish the message to a channel named 'pub_sub_channel'
            redis_client.publish('pub_sub_channel', message)

if __name__ == "__main__":
    publisher = Publisher()
    publisher.publish_message()
