num1 = int(input("Give Me A Number Mosky Boy"))
num2 = int(input("Give A Number for Gage now"))

while num1 % num2 != 0:
    # inform user of result
    print("Hey Dummy, those numbers are not divisible evenly. TRY AGAIN")

    # gather user input again
    num1 = int(input("May I Have A Number?"))
    num2 = int(input("May I Have A Number?"))

print("Finnally, You Got It Right")
