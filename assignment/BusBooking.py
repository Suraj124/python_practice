from threading import Thread,Semaphore

class BusBooking:
    def __init__(self,seatAvailable):
        self.seatAvailable=seatAvailable
        self.l=Semaphore()
    def buyTicket(self,requestSeat):
        self.requestSeat=requestSeat
        self.l.acquire()
        if self.requestSeat<=self.seatAvailable:
            print(requestSeat,"seat booked")
            self.seatAvailable-=self.requestSeat
        else:
            print("Seat not avaialable")
        self.l.release()

obj=BusBooking(10)
t1=Thread(target=obj.buyTicket,args=(5,))
t2=Thread(target=obj.buyTicket,args=(6,))
t1.start()
t2.start()