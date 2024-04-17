red=int(input("Enter the red: "))
green=int(input("Enter the green: "))
blue=int(input("Enter the blue: "))



if not(red > 255 or red < 0) and not(green > 255 or green < 0) and not(blue > 255 or blue < 0):
    print("No problems found!")

if red > 255 or red < 0:
    print("Red number is not correct.")

if green > 255 or green < 0:
    print("Green number is not correct.")

if blue > 255 or blue < 0:
    print("Blue number is not correct.")

