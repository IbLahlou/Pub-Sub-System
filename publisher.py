import redis

class Publisher:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def publish(self, channel, message):
        self.redis_client.publish(channel, message)
