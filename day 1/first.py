print("Hello World")
name = "afla"
print(name)
age = 20

# indentation
if age >= 18:
    print("You are an adult")
    print("You can vote")

# data types
# int
x = 10
print(type(x))

#float
y = 10.5
print(type(y))

#complex
z = 2 + 5j
print(z)
print(type(z))

#range
#odd
for i in range(1, 12, 2):
    print(i)

#even
for j in range(2,11,2):
    print(j)

#conditional statements
n = 5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
elif n == 0:
    print("Zero")

#fizzbuzz
b = 15
if n / 3 and n / 5 :
    print("FizzBuzz")
elif n / 3 :
    print("Fizz")
elif n / 5 :
    print("Buzz")
else :
    print(n)

#even numbers
def even_or_add(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_add(10))
print(even_or_add(7))

#Loops
#for
# for i in range(1,11):
#     print(i)
#while
i = 10
# while i >= 1:
#     print(i)
#     i -= 1
#break
for i in range(1,11):
    if i == 6:
        break
    print(i)
#continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#pass
for i in range(1,6):
    if i == 3:
        pass
    print(i)