import timeit

p=timeit.timeit('"-".join(str(i) for i in range(100))',number=10000)

print(p)

p=timeit.timeit('"-".join([str(i) for i in range(100)])',number=10000)

print(p)

p=timeit.timeit('"-".join(map(str,range(100)))',number=10000)

print(p)