# Exercise 1

username = input("Enter your username: ")
age = int(input(f"{username}, enter your age: "))

print(100 - age)

# Exercise 2

width = int(input("Enter the width of the room: "))
length = int(input("Enter the length of the room: "))
height = int(input("Enter the height of the room: "))

print(f"Volume of the room: {width * length * height}")

# Exercise 3

celsius = int(input("Enter the temperature in Celsius: "))
fahrenheit = 32 + celsius * (9 / 5)

print(fahrenheit)

# Exercise 4

temperature = int(input("Enter your body temperature: "))

if (temperature < 35):
  print("Too cold")
elif (temperature > 37):
  print("Too hot")
else:
  print("Everything looks good")


# Exercise 5

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

if num1 < num2 and num2 < num3:
  print(f"Ascending order: {num1, num2, num3}")
elif num1 < num3 and num3 < num2:
  print(f"Ascending order: {num1, num3, num2}")
elif num2 < num1 and num1 < num3:
  print(f"Ascending order: {num2, num1, num3}")
elif num2 < num3 and num3 < num1:
  print(f"Ascending order: {num2, num3, num1}")
elif num3 < num1 and num1 < num2:
  print(f"Ascending order: {num3, num1, num2}")
elif num3 < num2 and num2 < num1:
  print(f"Ascending order: {num3, num2, num1}")