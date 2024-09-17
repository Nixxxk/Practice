row1 = [1,1,1]
row2 = [1,1,1]
row3 = [1,1,1]

matrix = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
possition = input('Enter the possition where u want to hide money...!')
row_number = int(possition[0])
column_number = int(possition[1])
row_selected = matrix[row_number-1]
row_selected[column_number-1]='X'
print(f"{row1}\n{row2}\n{row3}")