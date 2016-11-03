# CS 61A Fall 2014
# Name:Siyuan Guo
# Login:bgy

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,name,price):
        self.price=price
        self.product=name
        self.balance=0
        self.stock=0
    def vend(self):
        if self.stock==0:
            return 'Machine is out of stock.'
        
        elif self.balance==self.price:
            self.balance=0
            self.stock-=1
            return 'Here is your {0}.'.format(self.product)
        elif self.balance<self.price:
            return 'You must deposit ${0} more.'.format(self.price-self.balance)
        elif self.balance>self.price:


            print("'Here is your {0} and ${1} change.'".format(self.product,self.balance-self.price))
            self.balance=0
            self.stock-=1


    def restock(self,amount):
        self.stock+=amount
        return 'Current {0} stock: {1}'.format(self.product, self.stock)


    def deposit(self,amount):
        self.balance+=amount

        if self.stock==0:
            return 'Machine is out of stock. Here is your ${0}.'.format(self.balance)
            self.balance=0

        else:
            return 'Current balance: ${0}'.format(self.balance)
        
            






