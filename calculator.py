def multiplication(a, b):
    return a * b
def addition(a, b):
    return a + b
def division(a, b):
    return a / b
def subtraction(a, b):
    return a - b
print("pick the calcul")
print("1 addition")
print("2 subtraction")
print("3 multiplication")
print("4 division")
while True:
    choice = input("Enter choice (1/2/3/4: ")
    try:
        firstnumber = float(input("Enter number one"))
        secondnumber = float(input("Enter number two"))
    except:
        print("Your a dumass who can't use a calculator")
        continue
    if choice == "1":
        print(firstnumber, "+" , secondnumber, "=" , addition(firstnumber, secondnumber))
    elif choice == "2":
        print(firstnumber, "-" , secondnumber, "=" , subtraction(firstnumber, secondnumber))
    elif choice == "3":
        print(firstnumber, "*" , secondnumber, "=" , multiplication(firstnumber, secondnumber))
    elif choice == "4":
        if secondnumber == 0:
            print("can't divide by 0")
        else:
            print(firstnumber, "/" , secondnumber, "=" , division(firstnumber, secondnumber)) #made by a dumass
        
