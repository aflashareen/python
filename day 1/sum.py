# n = 5
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)

n = 10
even = 0
for i in range(1 ,n + 1):
    if i % 2 == 0 :
        even += 1

#print(even)

#find largest
numbers = [4,9,2,7,1]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i

#print(largest)

#count digits
num = 58392
count = 0
while num > 0:
    num = num // 10
    count += 1

#print(count)

#reverse number 
nums = 1234
reverse = 0

while nums > 0:
    digit = nums % 10
    reverse = reverse * 10 + digit
    nums = nums // 10
print(reverse)
