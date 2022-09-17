x = input('Please input x:')
x = eval(x)
if x<0 or x>=20:
    print(0)
elif 0<=x<5:
    print(x)
elif 5<=x<10:
    print(3*x-5)
elif 10<=x<20:
    print(0.5*x-2)