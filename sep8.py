'''
Student Marks Manager
---------------------

marks = []
for mark in range(3):
    mark = int(input("Enter the marks:"))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
removed_mark = marks.pop()
print(f'remove mark is {removed_mark}')
print(f'final student marks list is {marks}')
print(f'count of students marks list is {marks}')

BMI
-----
1)
n_of_t_user_input = int(input("enter the value:"))
for i in range(n_of_t_user_input):
    weight = float(input("Enter the weight in kgs:"))
    height = float(input("Enter the height in metres:"))
    name = input("enter the user name:")

    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            print(f"{name}: under weight")
        elif 18.5 <= bmi <= 24.9:
            print(f"{name}: normal weight")
        elif 25.0 <= bmi <= 29.9:
            print(f"{name}: over weight")
        else:
            print(f"{name}: obesity")
    else:
        print("enter positive values")

2)
while True:
    weight = int(input("enter the weight in kgs:"))
    height = float(input("enter the height in metres:"))
    try:
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                print(f"{name}: under weight")
            elif 18.5 <= bmi <= 24.9:
                print(f"{name}: normal weight")
            elif 25.0 <= bmi <= 29.9:
                print(f"{name}: over weight")
            else:
                print(f"{name}: obesity")
            break
        else:
            print("invalid input")
    except Exception as e:
        print(f"The Error is {e}")

number list analyzer
------------------------


numbers = [20, 10, 30, 20, 40, 20]
print(f'the original list is {numbers}')
numbers.sort()
numbers.reverse()
print(numbers)
num = int(input("Enter a number to search for: "))
if num in numbers:
    print(f'the count of this number is {numbers.count(num)}')
    print(f'the index of this number is {numbers.index(num)}')
    print(f'the largest value is {max(numbers)}')
    print(f'the smallest value is {min(numbers)}')
    print(f'the smallest value is {sum(numbers)}')
else:
    print("number not found")


even and odd number separation
---------------------------------


nums = [10, 15, 20, 25, 30, 35]
even = []
odd = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even nums:", even)
print("Odd nums:", odd)
print("First three values:", nums[:3])
print("Last three values:", nums[-3:])

nums_backup = nums.copy()

nums.clear()

print("Original list using clear():", nums)
print("Backup list:", nums_backup)


unique name manager
-----------------------


names = ["Asha", "Rahul", "Asha","John","Rahul"]
print(names)
names = set(names)
print(names)
names.add("Meera")
names.update(["Arun","Priya"])
print(names)
if "John" in names:
    names.remove("John")
print(names)
names.discard("David")
print(names)
for name in names:
    print(name)


course student comparision
-------------------------------

'''

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

print("--- Union ---")
for student in python_students | da_students:
    print(student)

print("\n--- Intersection ---")
for student in python_students & da_students:
    print(student)

print("\n--- Symmetric Difference ---")
for student in python_students ^ da_students:
    print(student)

print("\n--- Relationships ---")
if da_students <= python_students:
    print("DA is a subset of Python")
else:
    print("DA is NOT a subset of Python")

if da_students >= python_students:
    print("DA is a superset of Python")
else:
    print("DA is NOT a superset of Python")

if da_students.isdisjoint(python_students):
    print("Classes are disjoint")
else:
    print("Classes are NOT disjoint")


























        




