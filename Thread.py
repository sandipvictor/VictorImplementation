#
from threading import *
from time import sleep
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hi")
#             sleep(1)
# t1 = Hello()
# t1.start()
# t2 = Hi()
# sleep(0.1)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("bye")
#

class MyThread(Thread):
    def run(self):
        print("{} started!".format(self.getName()))           # "Thread-x started!"
        sleep(1)                                      # Pretend to work for a second
        print("{} finished!".format(self.getName()))  # "Thread-x finished!"
        sleep(1)
def main():
    for x in range(4):                                     # Four times...
        mythread = MyThread(name="Thread-{x}")  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, invoke the run method
        mythread.join()
        sleep(.9)                                     # ...Wait 0.9 seconds before starting another
# if __name__ == '__main__':
main()

