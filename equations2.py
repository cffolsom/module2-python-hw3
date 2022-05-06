from math import pi

def equations():
    question = input("What do you want to do? Square, Circle? ")
    if question.lower() == "square":
        length = int(input("Give me the length: "))
        width = int(input("Now the width... "))
        area = length * width
        print(area)
    elif question.lower() == "circle":
        radius = int(input("Give me the radius of a Circle: "))
        circumference = (2 * pi) * radius
        print(circumference)