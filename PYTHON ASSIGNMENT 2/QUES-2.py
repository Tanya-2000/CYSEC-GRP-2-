def lesser_of_two_even(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return (a)
        else:
            return (b)
    else:
        if a>b:
            return (a)
        else:
            return (b)
print(lesser_of_two_even(2,4))
print(lesser_of_two_even(2,5))

