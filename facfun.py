def factorial(x):
    f=1

    if x>0 :
        for x in range(1,x+1):
            f= f*x
        print('Factorial of a number is ',f)
    elif x==1 :
            print('Factorial of a number is 1')
    elif x==0 :
            print('Factorial of a number is not valid')
