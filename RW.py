import threading
import time

# Shared data
shared_data = 0
readers_count = 0
readers_lock = threading.Lock()
writers_lock = threading.Lock()

def reader():
    global shared_data
    with readers_lock:
        readers_count += 1
        if readers_count == 1:
            writers_lock.acquire()

    print(f"Reader reads: {shared_data}")

    with readers_lock:
        readers_count -= 1
        if readers_count == 0:
            writers_lock.release()

    time.sleep(1)

def writer():
    global shared_data
    with writers_lock:
        shared_data += 1
        print(f"Writer writes: {shared_data}")

    time.sleep(2)

# Create reader and writer threads
reader_threads = [threading.Thread(target=reader) for _ in range(3)]
writer_threads = [threading.Thread(target=writer) for _ in range(2)]

# Start threads
for thread in reader_threads + writer_threads:
    thread.start()

# Wait for threads to finish
for thread in reader_threads + writer_threads:
    thread.join()
