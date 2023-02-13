
try:
    def myage():
        age = int(input("Enter your age"))
        months = age * 12
        print(f"You have lived for {months} months")
    myage()
except:
    print("Not a number")

