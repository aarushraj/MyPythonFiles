# Sort a list in descending order and perform binary search on it

numbers = [23, 53, 12, 75, 6, 45]
print(numbers)

#Sorting the list in  ascending order
numbers.sort(reverse=True)

print("Sorted Array (In descending order): ")
print(numbers)

L = 0
U = (len(numbers))-1
M = 0

item = int(input("Enter number to be searched: "))
flag = 0

while L<=U:
    M = int((U+L)/2)

    if item < numbers[M]:
        L = M+1
    elif item > numbers[M]:
        U = M-1
    else:
        flag = 1
        break

if(flag==1):
    print("ITEM HAS BEEN FOUND AT INDEX: " + str(M))
else:
    print("ITEM NOT FOUND!")