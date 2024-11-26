# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    counter = 0
    while counter < num:
        counter = counter + 1


def main():
    print(cpu_count())
    start_time = time.perf_counter()  # Store the start time
    absolute = 10 ** 9
    number = round((1/4) * 10 ** 9)
    print("Counting to", absolute)
    print("Each process counting to", number)
    a = Process(target=counter, args=(round(number),))
    b = Process(target=counter, args=(round(number),))
    c = Process(target=counter, args=(round(number),))
    d = Process(target=counter, args=(round(number),))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    end_time = time.perf_counter()  # Store the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print("MAIN")
    print("Real execution time:", elapsed_time, "seconds")


if __name__ == "__main__":
    main()

# 1 thread = 67.76 s
# 2 threads = 35.27 s
# 3 threads = 29.44 s
# 4 threads = 27.82 s
# 5 threads = s
