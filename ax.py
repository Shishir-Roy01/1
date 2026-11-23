
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit) 

for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

numbers = [4, 7, 12, 19, 24, 31]
even_nums = []
odd_nums = []

for n in numbers:
    if n % 2 == 0:
        even_nums.append(n)
    else:
        odd_nums.append(n)

print("Even", even_nums)  
print("Odd", odd_nums)    


i = 1
while i <= 5:
    status = "Even" if i % 2 == 0 else "Odd"
    print(f"{i} -> {status}")
    i += 1






