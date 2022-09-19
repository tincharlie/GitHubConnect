import math

class Complex(object):
    def __init__(self,real,imginary):
        self.real = real
        self.imginary = imginary
        
    def __add__(self, no):
        temp = Complex(None,None)
        temp.real=self.real+no.real  
        temp.imginary=self.imginary+no.imginary 
        return temp
          
    def __sub__(self, no):
        temp = Complex(None,None)
        temp.real=self.real-no.real  
        temp.imginary=self.imginary-no.imginary  
        return temp
        
    def __mul__(self, no):
        temp = Complex(None,None)
        num1 = complex(self.real, self.imginary)
        num2 = complex(no.real, no.imginary)
        product = num1 * num2
        temp.real = product.real
        temp.imginary = product.imag    
        return temp
        
    def __truediv__(self, no):
        temp = Complex(None,None)
        num1 = complex(self.real, self.imginary)
        num2 = complex(no.real, no.imginary)
        result = num1 / num2
        temp.real = result.real
        temp.imginary = result.imag    
        return temp
        
    def mod(self):
        temp = Complex(None,None)
        temp.real = math.sqrt(self.real**2 + self.imginary**2)
        temp.imginary = 0.00
        return temp

    def __str__(self):
        """

        Desc: Return string

        Created By : Wasim
        :return:
        """
        if self.imginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imginary >= 0:
                result = "0.00+%.2fi" % (self.imginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imginary))
        elif self.imginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imginary))
        return result

        
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str,[x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')