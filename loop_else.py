#exception handling

a=input("Enter the no. ")
#print(f"multiplication table of {a} is: ")
print("multiplication table of "+ a + " is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Something went wrong")

print("Table is succefully printed")
print("End of the program")

