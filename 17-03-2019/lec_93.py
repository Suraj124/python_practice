
# def generator(x,y):
#     while x<=y:
#         yield x
#         x+=1

# # result=generator(10,20)
# for i in generator(1,10):print(i)

def even_generator(x):
        a=2
        c=1
        while(c<=x):
                yield a
                a+=2
                c+=1
for i in even_generator(10):print(i)


