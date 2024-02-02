import threading
import time

# Number of philosophers
num_philosophers = 5

# Semaphore for controlling access to shared resources
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

def philosopher(index):
    left_fork = forks[index]
    right_fork = forks[(index + 1) % num_philosophers]

    while True:
        with left_fork:
            with right_fork:
                print(f"Philosopher {index} is eating.")
                time.sleep(2)
        print(f"Philosopher {index} is thinking.")
        time.sleep(1)

# Create philosopher threads
philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]

# Start threads
for thread in philosopher_threads:
    thread.start()

# Wait for threads to finish
for thread in philosopher_threads:
    thread.join()
