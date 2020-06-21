class Complex:

    type = "complex number"
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def createComlpexNumber(self):
        number = "Complex number is " + str(self.real) +  " + " + str(self.imaginary) + "i"
        return number

    def setReal(self, real):
        self.real = real

    def setImaginary(self, imaginary):
        self.imaginary = imaginary

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imaginary

myNumber = Complex(9, 18)
print (myNumber.createComlpexNumber())

myNumber.setReal(20)
myNumber.setImaginary(7)
print(myNumber.createComlpexNumber())
print(myNumber.getReal())
print(myNumber.getImaginary())
