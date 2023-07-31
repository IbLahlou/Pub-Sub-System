from publisher import Publisher
from subscriber import Subscriber
import threading

if __name__ == "__main__":
    # Start the subscriber in a separate thread
    subscriber_thread = threading.Thread(target=Subscriber().subscribe_channel)
    subscriber_thread.daemon = True
    subscriber_thread.start()

    # Start the publisher in the main thread
    Publisher().publish_message()

    # Wait for the subscriber thread to finish (if needed)
    # subscriber_thread.join()
