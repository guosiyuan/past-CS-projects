#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.initial=self.start
        "*** YOUR CODE HERE ***"

    def __next__(self):
        if self.start>self.end:
            self.start=self.initial
            raise StopIteration
        value=self.start

        self.start+=1
        return value
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        
        return self
        "*** YOUR CODE HERE ***"

##############
# Generators #
##############

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >=0:
        yield n
        n-=1

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, start):
        self.start=start
    def __iter__(self):
        while self.start>=0:
            yield self.start
            self.start-=1

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n!=1:
        yield n
        if n%2==0:
            n//=2
        else:
            n=n*3+1
    yield 1
    "*** YOUR CODE HERE ***"

###########
# Streams #
###########

class Stream:
    class empty:
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def add_streams(s1, s2):

    def computerest():
        return add_streams(s1.rest,s2.rest)
    return Stream(s1.first+s2.first,computerest)






def integer_stream(first):
        def compute_rest():
            return integer_stream(first+1)
        return Stream(first, compute_rest)

s3=integer_stream(1)
s4=integer_stream(2)


s1=Stream(1, lambda:Stream(2, lambda: Stream.empty))


s2=Stream(2, lambda:Stream(4, lambda: Stream.empty))


