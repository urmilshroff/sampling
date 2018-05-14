import math
from scipy import stats


def los_calc_z(los): #LOS calculator for z-test
    if(los==5):
        if(tails==2):
            return z_a=1.96 #two-tailed @ 5% LOS
        else:
            return z_a=1.65 #one-tailed @ 5% LOS

    elif(los==1):
        if(tails==2):
            return z_a=2.58 #two-tailed @ 1% LOS
        else:
            return z_a=2.33 #one-tailed @ 1% LOS


def los_calc_t(los,n,num): #LOS calculator for t-test
    if(num==1):
        return stats.t.ppf((1-(los/100)),n)

    elif(num==2):
        #double population: t(n1+n2-2,t_a)




def large_sample(num,n1,n2):
    if(num==1):
        print("\nOkay, this looks like a Large Sample Test with only one Sample!")

        x=float(input("Enter mean of the Sample:\n"))
        u=float(input("Enter mean of the Population:\n"))
        sd=float(input("Enter the standard deviation:\n"))
        z_a=los_calc_z(int(input("Enter the Level Of Significance:\n")))
        tails=int(input("Is the hypothesis one tailed or two tailed?\n"))



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
        z_a=los_calc_z(int(input("Enter the Level Of Significance:\n")))
        tails=int(input("Is the hypothesis one tailed or two tailed?\n"))



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

if(int(input("Enter number of Samples:\n"))==1):
    n=float(input("Enter size of the Sample:\n"))

    if (n>=30):
        large_sample(1,n,0) #large sample single
    else:
        small_sample(1,n,0) #small sample single

else:
    n1=float(input("Enter size of the first Sample:\n"))
    n2=float(input("Enter size of the second Sample:\n"))

    if (n1>=30) and (n2>=30):
        large_sample(2,n1,n2) #large sample double

    else:
        small_sample(2,n1,n2) #small sample double
