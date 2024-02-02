import threading
import time
import queue

# Shared buffer between producer and consumer
buffer = queue.Queue(maxsize=5)

def producer():
    for i in range(10):
        item = f"Item-{i}"
        buffer.put(item)
        print(f"Produced: {item}")
        time.sleep(1)

def consumer():
    while True:
        item = buffer.get()
        print(f"Consumed: {item}")
        time.sleep(2)

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()
