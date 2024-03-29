class Fraction:
	# instantiate two data types, numerator and denominator
    def __init__(self,top,bottom):
    	# The notation self.num in the constructor defines the fraction
    	# object to have an internal data object called num as part of its state
        self.num = top
        self.den = bottom
    def show(self):
    	print(self.num,"/",self.den)

    def __str__(self):
    	return str(self.num)+"/"+str(self.den)
    #okay, lets look at some behaviour, can we add the two Fractions
	#myfraction = Fraction(3,5) #instantiate class
	#myfraction_2 = Fraction (4,2)# specify which behavior to implement
	#print(myfraction + myfraction_2)

    #the problem is that the “+” operator does not understand the Fraction operands.
    #We can fix this by providing the Fraction class with a
    #method that overrides the addition method.

    def __add__(self,otherfraction):
   		newnum = self.num*otherfraction.den + self.den*otherfraction.num
   		newden = self.den*otherfraction.den
   		#common = gcd(newnum,newden)
   		return Fraction(newnum//common,newden//common)

    def __eq__(self, otherfraction):
        firstnum = self.num * otherfraction.den
        secondnum = otherfraction.num * self.den


        return firstnum == secondnum


myfraction_1 = Fraction(3,5)
myfraction_2 = Fraction(4,6)

myfraction_3 = myfraction_2 + myfraction_1
print(myfraction_3)
