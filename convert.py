def convert():
    celsius = eval(input("What is the celsius temperature? "))
    fahrenheit = (9 / 5) * celsius + 32
    print("The temperature is", fahrenheit, "F.")

if __name__ == "__main__":
    convert()