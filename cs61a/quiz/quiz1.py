# CS 61A Fall 2014
# Name:SiyuanGuo
# Login:25803804


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    assert type(a)==int and type(b)==int and type(c)==int,'arguments should be integer'
    if (a==b and b!=c) or (b==c and c!=a) or (a==c and c!=b):
        return True
    else:
        return False


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    assert a>0 and b>0,'arguments should be positive'
    assert type(a)==int and type(b)==int,'srguments should be integer'
    x,y=a,b
    while a!= 1:
        if a%2==0:
            a=a//2
            if a==b:
                return True
        else:
            a=3*a+1
            if a==b:
                return True
    while y!= 1:
        if y%2==0:
            y=y//2
            if y==x:
                return True
        else:
            y=3*y+1
            if y==x:
                return True
    return False


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    from operator import abs
    assert perimeter%2==0,'perimeter should be even'
    assert perimeter>4,'invalid perimeter'
    dif_para=100
    h=1
    while (h+1)<perimeter/2:
        
        dif_1=abs(h/(perimeter/2-h)-((perimeter/2-h)/h)+1)
        dif_2=abs((h+1)/(perimeter/2-(h+1))-(perimeter/2-(h+1))/(h+1)+1)
        h=h+1
        if dif_1>dif_2:
            if dif_2<dif_para:
                dif_para=dif_2
                output=h
    return output

