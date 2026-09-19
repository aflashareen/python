#1
numbers = [10, 20, 30, 40, 50]
toSet = set(numbers)
toSet.add(60)
toSet.remove(20)
numbers = list(toSet)
numbers[4] = 35
print(numbers)

numbers.append(60)
numbers.remove(20)
numbers[1]=35
print(numbers)

#2
fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))

#3
student = ("Afla", 21, "Python")
name, age, course = student
print(name)
print(age)
print(course)

#4
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.count(20))
print(numbers.index(20))

#5
numbers = {10, 20, 10, 30, 20, 40}
print(numbers)
