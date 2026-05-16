numbers=[1,2,3,4,7,9,8]
largest=numbers[1]
for num in numbers:
  if num > largest:
    largest=num
print("largest element: ", largest)
