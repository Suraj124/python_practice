from threading import current_thread,Thread

def displayNumber():
    print("Current Thread running is :",current_thread().getName())
    for i in range(11):
        print(i)
print("Current Thread running is :",current_thread().getName())
t=Thread(target=displayNumber)
t.start()