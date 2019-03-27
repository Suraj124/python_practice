from threading import Thread

class BookMyBus:
    def __init__(self,availabeSeat):
        self.availabeSeat=availabeSeat

    def buy(self,requestedSeat):
        self.requestedSeat=requestedSeat
        print("Total availabe seat is ",self.availabeSeat)
        if self.requestedSeat<=self.availabeSeat:
             print("Confirming a seat")
             print("Processing a Payment")
             print("Printing the ticket")
             self.availabeSeat-=self.requestedSeat
        else:
            print("Sorry, No seats availabe!!!!")


obj=BookMyBus(10)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(3,))
t3=Thread(target=obj.buy,args=(3,))
t1.start()
t2.start()
t3.start()