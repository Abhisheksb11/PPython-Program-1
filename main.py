class Investment:
    def __init__(self,p,i):
        self.principal = p
        self.interest =i

    def value(self,n):
        v = pow((1+self.interest),n)
        return self.principal * v

 

    def __str__(self):
        return 'Principal - $%.2f,Interest rate - %.2f%%' %(self.principal,self.interest)
 

 

p = float(input("Enter principal amount"))
i = float(input("Enter interest"))
n = int(input("Enter time period"))
i1 = Investment(p,i)
investment = i1.value(n)
print("Investment value after {0} years is {1}".format(n,investment))
