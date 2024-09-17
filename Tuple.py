# tuple1 = (3,-23,True,"Nikhil")
# print(type(tuple1)) #tuples are immutable/unchangable.


if __name__ =='__main__':
    n = int(input())

    a = map(int, input().split())

    t = tuple(a)

    print(hash(t))