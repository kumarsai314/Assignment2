def area(W,H):
    return W*H
def perimeter(W,H):
    return 2*(W+H)
W= int(input('Enter Width:'))
H= int(input('Enter Height:'))
print('area of rectangle:',area(W,H))
print('perimeter of rectangle:',perimeter(W,H))
