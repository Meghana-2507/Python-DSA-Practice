numbers=[1,3,4,5,2,6]
smallest=numbers[1]
for num in numbers:
  if num < smallest:
    smallest=num
print("Smallest element:", smallest)
