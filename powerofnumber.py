def power(a,b):
    if b==0:
        return 1
    else:
        return  a**b
a= int(input('enter a number:'))
b= int(input('enter power:'))
print('power of a number:',power(a,b))
