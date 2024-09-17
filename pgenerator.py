import random

#print(f"{letters} \n\n {numbers}\n \n {symbols}")

letter = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters=letter.split()

number = "0 1 2 3 4 5 6 7 8 9"
symbol = "! @ # $ % ^ & * ( ) { } | : ? > < / . , ' ; ] [ \ = - _ + ]"
numbers=number.split()
symbols=symbol.split()

print("Wellcome to pgernerator...!")

n_letters=int(input("How many letter you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))

password=[]

for i in range(1,n_letters+1):
    char=random.choice(letters)
    password=password+char
for i in range(1,n_numbers+1):
    char1=random.choice(numbers)
    password=password+char1
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password=password+char


random.shuffle(password)


print(password)


print(type(password))

random.shuffle(password)

# pass=""
# for char in pass:
#     pass+=char

# print(pass)