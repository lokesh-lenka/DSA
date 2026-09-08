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

'''
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
        




