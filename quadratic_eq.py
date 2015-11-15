import math
a = float(raw_input("a? "))
b = float(raw_input("b? "))
c = float(raw_input("c? "))
print a, b, c
discriminate = ((b)+math.sqrt(b*b+4*a*c))/2*a
discriminate_a = ((b)-math.sqrt(b*b+4*a*c))/2*a
print discriminate
print discriminate_a