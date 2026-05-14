numbers=[2,9,5,4,6]
largest=float('-inf')
second=float('-inf')
for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
print("Second largest: ",second)
