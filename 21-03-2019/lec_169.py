import threading
import time
class myThread:
    def displayNumber(self):
        print("Current thread : ",threading.current_thread().getName())
        time.sleep(1)
        for i in range(11):
            print(i)

obj=myThread()
t=threading.Thread(target=obj.displayNumber)
t.start()

t2=threading.Thread(target=obj.displayNumber)
t2.start()

t3=threading.Thread(target=obj.displayNumber)
t3.start()