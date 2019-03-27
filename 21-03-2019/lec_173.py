from threading import Thread,Lock

class BookMyBus:
    def __init__(self,availabeSeat):
        self.availabeSeat=availabeSeat
        self.l = Lock()
        print("Total availabe seat is ",self.availabeSeat)
    
    def buy(self,requestedSeat):
        self.l.acquire()
        self.requestedSeat=requestedSeat
        
        if self.requestedSeat<=self.availabeSeat:
             print("You have booked",self.requestedSeat,"seats")
             print("Confirming a seat")
             print("Processing a Payment for",self.requestedSeat,"Seats")
             print("Printing the ticket")
             self.availabeSeat-=self.requestedSeat
             print("Total availabe seat is ",self.availabeSeat)
        else:
            print("Sorry, Only",self.requestedSeat,"seats are availabe!!!!")
        
        self.l.release()


obj=BookMyBus(10)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(3,))
t3=Thread(target=obj.buy,args=(3,))
t4=Thread(target=obj.buy,args=(2,))
t1.start()
t2.start()
t3.start()
t4.start()