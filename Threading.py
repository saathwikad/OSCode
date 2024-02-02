import threading
import time

# Define a semaphore with an initial value of 3
semaphore = threading.Semaphore(3)

# Function that simulates a resource being accessed
def access_resource(thread_id):
    print(f"Thread {thread_id} is waiting to access the resource.")
    with semaphore:
        print(f"Thread {thread_id} has acquired the semaphore and is accessing the resource.")
        time.sleep(2)  # Simulating some work being done
    print(f"Thread {thread_id} has released the semaphore and finished accessing the resource.")

# Create threads to access the resource
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
