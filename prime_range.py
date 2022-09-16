
minimum = int(input("Enter the Minimum number: "))
maximum = int(input("Enter the Maximum number: "))
number_list = []

for i in range(minimum, maximum + 1):
    count = 0
    for j in range(2, int(i / 2 + 1)):
        if i % j == 0:
            count += 1            
            break

    if count == 0 and i != 1:
        number_list.append(i)
        print(i, end=' ')
print(number_list)
