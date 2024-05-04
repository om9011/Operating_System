import threading
import time
import random

# Shared buffer
buffer = []
buffer_size = 5

# Lock for accessing the buffer
buffer_lock = threading.Lock()

# Condition variables
buffer_not_full = threading.Condition(lock=buffer_lock)
buffer_not_empty = threading.Condition(lock=buffer_lock)

def producer():
    global buffer

    while True:
        item = random.randint(1, 100)

        with buffer_not_full:
            while len(buffer) == buffer_size:
                buffer_not_full.wait()

            with buffer_lock:
                buffer.append(item)
                print(f"Produced {item}. Buffer: {buffer}")

            buffer_not_empty.notify()

        time.sleep(random.uniform(0.1, 0.5))  # Simulate production time

def consumer():
    global buffer

    while True:
        with buffer_not_empty:
            while len(buffer) == 0:
                buffer_not_empty.wait()

            with buffer_lock:
                item = buffer.pop(0)
                print(f"Consumed {item}. Buffer: {buffer}")

            buffer_not_full.notify()

        time.sleep(random.uniform(0.1, 0.5))  # Simulate consumption time

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, daemon=True)
consumer_thread = threading.Thread(target=consumer, daemon=True)

# Start threads
producer_thread.start()
consumer_thread.start()

# Allow threads to run for a certain duration
time.sleep(5)
