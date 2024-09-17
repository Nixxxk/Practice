marks = [45, 21, 33, 12, 5]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("OK GOT IT...!")

#     index +=1


for index, mark in enumerate(marks, start=2):
    print(mark)
    if(index==3):
        print("OK GOT IT...!")


