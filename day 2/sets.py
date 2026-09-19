# numbers = { 10,20,30,40,10}
# print(numbers)

# python_students = {"Afla", "Aju", "Rahul", "Maya"}
# react_students = {"Afla", "Maya", "John"}

# print("Both courses:", python_students & react_students)
# print("All students:", python_students | react_students)
# print("Only Python:", python_students - react_students)

#1
numbers = { 10,20,30,40,50 }
print(numbers)

#2
numbers = {10, 20, 10, 30, 20, 40}
print(numbers) #40,10,20,30

#3
fruits = { "apple","banana","mango" }
fruits.add("orange")
print(fruits)

#4
fruits = {"apple","banana","mango"}
fruits.remove("banana")

#5
numbers = {5, 10, 15, 20, 25}
for num in numbers:
    print(num)

#6
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A & B) #7
print(A - B) #8
print(B - A) #8

#9
python = {"HTML", "CSS", "Python", "SQL"}
web = {"HTML", "CSS", "JavaScript", "React"}

print(python & web)
print(python | web)
print(python - web)

#10
numbers = {10, 20, 30}

numbers.add(40)
numbers.remove(20)
numbers.update([50, 60])

print(numbers) #{10,30,40,50,60}