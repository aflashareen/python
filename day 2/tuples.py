# person = ("Afla",18,"Developer")
# name, age, job = person

# print(name)
# print(age)
# print(job)
# print(person)

# #swapping variables
# a = 10
# b = 20

# a, b = b, a
# print(a)
# print(b)

# #using * for multiple values
# numbers = (10,20,30,40,50)

# first, *middle, last = numbers

# print(first)
# print(middle)
# print(last)

# 1
# numbers = (10,20,30,40,50)
# print(numbers[2])

# #2
# fruits = ("apple","banana","mango","orange")
# print(fruits[-1])

# #3
# number = (10,20,30,40,50)
# print(number[1:4])
# # first, *middle, last = number
# # print(middle)

# #4
# colors = ("red","blue","green","yellow")
# print(len(colors))

# #5
# fruits = ("apple","banana","mango","orange")
# print("mango" in fruits)

#6
numbers = (5, 10, 15, 20, 25)
for num in numbers:
    print(num)

#7
numbers = (10,20,10,30,10,40)
print(numbers.count(10))

#8
fruits = ("apple", "banana", "mango", "orange")
print(fruits.index("mango"))

#9
numbers = (11,20,33,40,55,60)
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
print(even)

#10
numbers = (10, 20, 30, 40, 50)
sum = 0
for i in numbers:
    sum += i
print(sum)

#11
student = ("Afla", 21, "Python")
name, age, course = student
print(name)
print(age)
print(course)

#12
a = 100
b = 200

a, b = b, a
print(a)
print(b)

#13
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

#14
fruits = ("apple", "banana", "mango")
change = list(fruits)
change[1] = "orange"
fruits=tuple(change)
print(fruits)

#15
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10)) #3
print(numbers.index(30)) #3