# thread = a flow of execution. Like a separate order of instructions.
#          However, each global thread takes a turn  running to achieve concurrency
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intesitive)
#
# io bound =  program/task spends most of its time waiting for external events(user input, web scraping)
#             use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffe():
    time.sleep(4)
    print("You drank coffe")


def study():
    time.sleep(5)
    print("You finished studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

print(threading.active_count())  # amount of threads running right now
print(threading.enumerate())  # which thread
print(time.perf_counter())

x.join()
y.join()
z.join()
# eat_breakfast()
# drink_coffe()
# study()

