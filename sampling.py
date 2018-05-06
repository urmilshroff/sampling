import math

def large_sample(num,n1,n2):
    if(num==1):
        print("\nOkay, this looks like a Large Sample Test with only one Sample!")

        x=float(input("Enter mean of the Sample:\n"))
        u=float(input("Enter mean of the Population:\n"))
        sd=float(input("Enter the standard deviation:\n"))
        los=float(input("Enter the Level of Significance:\n"))
        tails=int(input("Is the hypothesis one tailed or two tailed?\n"))

        if(los==5): #WET
            if(tails==2):
                z_a=1.96
            else:
                z_a=1.65
        elif(los==1):
            if(tails==2):
                z_a=2.58
            else:
                z_a=2.33

        z=((x-u)/(sd/math.sqrt(n)))
        print("z =",z)

        if(z<0):
            z=-z

        if(z>z_a):
            print("|z|>z_a!\nNull hypothesis rejected, alternate hypothesis accepted!")
        elif(z<z_a):
            print("|z|<z_a!\nNull hypothesis accepted, alternate hypothesis rejected!")



    elif(num==2):
        print("\nOkay, this looks like a Large Sample Test with two Samples!")

        x1=float(input("What's the mean of the first Sample?\n"))
        x2=float(input("Enter the mean of the second Sample as well:\n"))

        num=input("Is the mean of the Population given? Y/N:\n")
        #fix later
        u=float(input("Enter mean of the Population:\n"))
        sd=float(input("Enter the standard deviation:\n"))
        los=float(input("Enter the Level of Significance:\n"))
        tails=int(input("Is the hypothesis one tailed or two tailed?\n"))

        if(los==5):
            if(tails==2):
                z_a=1.96
            else:
                z_a=1.65
        elif(los==1):
            if(tails==2):
                z_a=2.58
            else:
                z_a=2.33

    else:
        print("Error, only 1 or 2 Samples allowed!")

def small_sample(num,n1,n2):
    if(num==1):
        print("\nOkay, this looks like a Small Sample Test with only one Sample!")

    elif(num==2):
        print("\nOkay, this looks like a Small Sample Test with two Samples!")

    else:
        print("Error, only 1 or 2 Samples allowed!")



def get_data(num):
    n=float(input("Enter size of the sample:\n"))

    if(n>=30):
        large_sample()
    else:
        small_sample()


print("\nTesting of Hypothesis by Urmil Shroff\n")

if(int(input("Enter the number of Samples:\n"))==1):
    n=float(input("Enter the size of the Sample:\n"))

    if (n>=30):
        large_sample(1,n,0)
    else:
        small_sample(1,n,0)

else:
    n1=float(input("Enter the size of the first Sample:\n"))
    n2=float(input("Now enter the size of the second Sample:\n"))

    if (n1>=30) and (n2>=30):
        large_sample(2,n1,n2)

    else:
        small_sample(2,n1,n2)
