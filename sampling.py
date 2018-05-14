import math
from scipy import stats


def los_calc_z(los,tails): #LOS calculator for z-test (used for Large Samples)
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


def los_calc_t(los,n,num): #LOS calculator for t-test (used for Small Samples)
    if(num==1):
        return stats.t.ppf((1-(los/100)),n)

    elif(num==2):
        #double population: t(n1+n2-2,t_a)


def case1(n1,n2,x1,x2,s1,s2): #population sds not known, so we take s1, s2

def case2(n1,n2,s1,s2,popsd): #population sds are known and they are the same

def case3(): #population sds not known but they are said to be the same



def large_sample(num,n1,n2):
    if(num==1): #single large sample
        print("\nLarge Sample Test (one Sample)")

        x=float(input("Enter mean of the Sample:\n"))
        u=float(input("Enter mean of the Population:\n"))
        sd=float(input("Enter Standard Deviation:\n"))

        z_a=los_calc_z(int(input("Enter LOS:\n")),int(input("Is the hypothesis one tailed or two tailed?\n")))

        z=((x-u)/(sd/math.sqrt(n)))
        print("Z =",z,"Za =",z_a)

        if(z<0):
            z=-z

        if(z>z_a):
            print("Null hypothesis rejected, alternate hypothesis accepted!")
        elif(z<z_a):
            print("Null hypothesis accepted, alternate hypothesis rejected!")




    elif(num==2): #double large sample
        print("\nLarge Sample Test (two Samples)")

        yesno=input("Is Population SD the same for both populations? Y/N:\n")
        if(yesno=="y") or (yesno=="Y"):

            yesno=input("Is Population SD known? Y/N:\n")

            if(yesno=="y") or (yesno=="Y"): #case 2
                n1=float(input("Enter size of the first Sample\n"))
                n2=float(input("Enter size of the second Sample:\n"))

                x1=float(input("Enter mean of the first Sample\n"))
                x2=float(input("Enter mean of the second Sample:\n"))

                popsd=float(input("Enter common SD of the Populations:\n"))

                z=case2(n1,n2,x1,x2,popsd)

            else: #case 3
                n1=float(input("Enter size of the first Sample\n"))
                n2=float(input("Enter size of the second Sample:\n"))

                x1=float(input("Enter mean of the first Sample:\n"))
                x2=float(input("Enter mean of the second Sample:\n"))

                s1=float(input("Enter SD of the first Sample/Population:\n"))
                s2=float(input("Enter SD of the second Sample/Population:\n"))

                case3(n1,n2,x1,x2,s1,s2)

        else: #case 1
            n1=float(input("Enter size of the first Sample\n"))
            n2=float(input("Enter size of the second Sample:\n"))

            x1=float(input("Enter mean of the first Sample:\n"))
            x2=float(input("Enter mean of the second Sample:\n"))

            s1=float(input("Enter SD of the first Sample/Population:\n"))
            s2=float(input("Enter SD of the second Sample/Population:\n"))

            case1(n1,n2,x1,x2,s1,s2)


        z_a=los_calc_z(int(input("Enter LOS:\n")),int(input("Is the hypothesis one tailed or two tailed?\n")))

    else:
        print("Error, only 1 or 2 Samples can be predicted!")










def small_sample(num,n1,n2):
    if(num==1):
        print("\nSmall Sample Test (one Sample)")

    elif(num==2):
        print("\nSmall Sample Test (two Samples)")

    else:
        print("Error, only 1 or 2 Samples can be predicted!")



def get_data():

    if(int(input("Enter number of Samples:\n"))==1):

        n=float(input("Enter size of the Sample:\n"))

        if (n>=30):
            large_sample(1,n,0) #single large sample
        else:
            small_sample(1,n,0) #single small sample

    else:
        n1=float(input("Enter size of the first Sample:\n"))
        n2=float(input("Enter size of the second Sample:\n"))

        if (n1>=30) and (n2>=30):
            large_sample(2,n1,n2) #double large sample
        else:
            small_sample(2,n1,n2) #double small sample



print("\nTesting of Hypothesis by Urmil Shroff\n")

get_data()
