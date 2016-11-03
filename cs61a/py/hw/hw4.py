# CS 61A Fall 2014
# Name:Siyuan Guo
# Login:bgy

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


def interval(a, b):
    """Construct an interval from a to b."""
    a=[a,b]
    a.sort()
    return a

def lower_bound(x):
    """Return the lower bound of interval x."""
    return min(x)

def upper_bound(x):
    """Return the upper bound of interval x."""
    return max(x)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """

    assert not (0>lower_bound(y) and 0<upper_bound(y)),'contains 0'    
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    p1 = lower_bound(x)-lower_bound(y)
    p2 = lower_bound(x)-upper_bound(y)
    p3 = upper_bound(x)-lower_bound(y)
    p4 = upper_bound(x)-upper_bound(y)
    return interval(min(p1,p2,p3,p4), max(p1,p2,p3,p4))

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))
    #these two intervals give different result for parallel resistors.
    '[1,2],[1,2]'

def multiple_references_explanation():
  return """ for the first one when we get two intervals
   from applying mul_interval and add_interval, 
   we get two new intervals, but when we use these two intervals to derive a 
   new interval using div_interval, we get an interval which is not directy 
   relate to the original r1,r2. If we set r1,r2 to be [1,2],[1,2], the upperbound 
   of the final result is [0.5,2], but we can never get the '2' whichever single 
   number we try within the range r1 and r2"""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    x1=-b/(2*a)
    if x1>lower_bound(x) and x1<upper_bound(x):
        if abs(upper_bound(x)-x1)<abs(lower_bound(x)-x1):
            x2=lower_bound(x)

        else:
            x2=upper_bound(x)
    else:
        x1=lower_bound(x)
        x2=upper_bound(x)
    ft1=a*x1*x1+b*x1+c
    ft2=a*x2*x2+b*x2+c
    return interval(ft1,ft2)

    

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), (10, 24, -6, -8, 3)))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"




