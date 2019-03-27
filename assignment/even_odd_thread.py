from threading import Thread,current_thread

class EvenNumber(Thread):
    def run(self):
        for i in range(2,10,2):
            print("Even",i)
        print("End of Even Thread")

class OddNumber(Thread):
    def run(self):
        for i in range(1,10,2):
            print("Odd",i)
        print("End of odd Thread")

class main_thread:
    def __init__(self):
        for i in range(1,101):
            print(i)

m=main_thread()
t1=EvenNumber()
t2=OddNumber()
t1.start()
t2.start()

