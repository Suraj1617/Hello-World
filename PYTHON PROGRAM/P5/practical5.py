num = int(input("Enter a number:"))

if num <=1:
    print("Neither Prime Nor Composite")

elif num == 2:
    print("Even Prime Number")


else:
    for i in range(2,num):
        if num%i==0:
            print("composite number")
            break

    else:
        print("Prime Number")
