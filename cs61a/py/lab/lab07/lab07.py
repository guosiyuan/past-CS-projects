## Linked List Class and Generic Functions ##

######################
# Linked Lists Class #
######################

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1, 2, 3, 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        "*** YOUR CODE HERE ***"
        string=''
        store=self
        while len(store)>0:
            string=string+'{0}'.format(store.first)
            store=store.rest
            if len(store)>0:
                string=string+', '
        return '<'+string+'>'

            

def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> insert(link, 9001, 0)
    >>> link
    Link(9001, Link(1, Link(2, Link(3))))
    >>> insert(link, 100, 2)
    >>> link
    Link(9001, Link(1, Link(100, Link(2, Link(3)))))
    >>> insert(link, 4, 5)
    Index out of bounds
    """
    "*** YOUR CODE HERE ***"
    
    if index>=len(link):
        print( 'Index out of bounds')
        return
    elif index==1:
        store=link.rest
        link.rest=Link(value,store)
   
    elif index==0:
        link.rest=Link(link.first,link.rest)
        link.first=value
    else:
        insert(link.rest,value,index-1)
















