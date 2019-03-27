from threading import Thread            # first way of creating Thread

def displayNumber():
    for i in range(11):
        print(i)

t=Thread(target=displayNumber)
t.start()