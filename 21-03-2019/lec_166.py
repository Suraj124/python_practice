from threading import Thread            # 2nd way of creating Thread

class myThread(Thread):

    def run(self):
        for i in range(11):
            print(i)

t=myThread()
t.start()