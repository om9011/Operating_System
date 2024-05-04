import threading
import time
import random as rand


shared_resource = []
readers_count = 0
mutex = threading.Lock()
read_lock = threading.Lock()


def writer():
    global shared_resource

    while True:
        data_to_write = threading.current_thread().name + ":" + str(rand.randint(1,25))

        mutex.acquire()
        # Critical Section
        shared_resource.append(data_to_write)
        print(f"{threading.current_thread().name} writes '{data_to_write}'")
        mutex.release()

        time.sleep(1)


def reader():
    global readers_count
    global shared_resource

    while True:
        read_lock.acquire()
        readers_count += 1
        if readers_count == 1:
            mutex.acquire()
        read_lock.release()

        # Critical Section
        print(f"{threading.current_thread().name} reads {shared_resource}")

        read_lock.acquire()
        readers_count -= 1
        if readers_count == 0:
            mutex.release()
        read_lock.release()

        time.sleep(1)


writer_thread = threading.Thread(target=writer, name="Writer", daemon=True)

reader_threads = [threading.Thread(target=reader, name=f"Reader-{i + 1}", daemon=True) for i in range(3)]


writer_thread.start()
for reader_thread in reader_threads:
    reader_thread.start()
    print()


time.sleep(5)

# Optionally, you can stop the threads if needed
writer_thread.join()
for reader_thread in reader_threads:
    reader_thread.join()
