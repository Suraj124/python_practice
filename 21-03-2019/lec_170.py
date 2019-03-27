from threading import Thread

class BookMyBus:

    def buy(self):
        print("Confirming a seat")
        print("Processing a Payment")
        print("Printing the ticket")

obj=BookMyBus()
t1=Thread(target=obj.buy)
t2=Thread(target=obj.buy)
t3=Thread(target=obj.buy)
t1.start()
t2.start()
t3.start()