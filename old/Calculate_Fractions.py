def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    # This method allows the Fraction class to use the multiply arithmetic expression.
    def __mul__(self, otherfraction):
        # To multiply two fractions together, simply multiply both numerators and both denominators.
        # Multiplication of one numerator with the second numerator.
        newnum = self.num * otherfraction.num
        # Multiplication of one denominator with the second denominator.
        newden = self.den * otherfraction.den
        # GCD module is called to reduce the fraction to the simplest terms.
        common = gcd(newnum, newden)
        # Returns the new fraction.
        return Fraction(newnum // common, newden // common)

    # This method allows the Fraction class to use the modulo divide expression.
    def __mod__(self, otherfraction):
        # To divide two fractions, we must cross multiply the parts of the fractions.
        # Multiply the numerator of one fraction with the denominator of the other.
        newnum = self.num * otherfraction.den
        # Multiply the denominator of one fraction with the numerator of the other.
        newden = self.den * otherfraction.num
        # GCD module is called to reduce the fraction to the simplest terms.
        common = gcd(newnum, newden)
        # Returns the new fraction.
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


def main():

    x = Fraction(1, 2)
    y = Fraction(2, 3)
    print(x + y)
    print(x == y)

    # New print functions display the results of multiplying and dividing fractions.
    print(x * y)
    print(x % y)


main()
