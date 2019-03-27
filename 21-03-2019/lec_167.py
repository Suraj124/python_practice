import threading        #Third way of creating Thread

class myThread:
    def displayNumber(self):
        print("Current thread : ",threading.current_thread().getName())
        for i in range(11):
            print(i)

obj=myThread()
t=threading.Thread(target=obj.displayNumber)
t.start()