def vote(a):
    if a<18:
        return ("no")
    else:
        return ("yes")
a=int(input('enter age:'))
print('is he/she able to vote:', vote(a))
