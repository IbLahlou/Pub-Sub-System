import subprocess
import time
from publisher import Publisher
from subscriber import Subscriber

def on_message(channel, message):
    print(f"Received message on channel '{channel}': {message}")

if __name__ == "__main__":
    # Start the Redis server as a separate process
    redis_process = subprocess.Popen(["redis-server"])

    # Wait for a moment to make sure the Redis server is up and running
    time.sleep(2)

    # Initialize the pub-sub components
    publisher = Publisher()
    subscriber = Subscriber()

    channel_name = "example_channel"

    # Start the subscriber thread and subscribe to the channel
    subscriber.subscribe(channel_name, on_message)
    subscriber.start()

    # Publish some messages to the channel
    publisher.publish(channel_name, "Hello, World!")
    publisher.publish(channel_name, "This is a pub-sub system example.")
    Message = input("Enter the message: ")
    publisher.publish(channel_name,Message)

    # Let the subscriber run for a few seconds to receive messages
    time.sleep(5)

    # Unsubscribe and stop the subscriber
    subscriber.unsubscribe(channel_name)
    subscriber.join()

    # Stop the Redis server process
    redis_process.terminate()
    redis_process.wait()
