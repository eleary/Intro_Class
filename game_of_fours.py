import math 
zero_string = "44-44"
print "%s=%i" %(zero_string, eval(zero_string))
one_string = "44/44"
print "%s=%i" %(one_string, eval(one_string))
two_string = "(4*4)/(4+4)"
print "%s=%i" %(two_string, eval(two_string))
three_string = "(4+4+4)/4"
print "%s=%i" %(three_string, eval (three_string))
four_string = "((4*4*4)/(4**2))"
print "%s=%i" %(four_string, eval(four_string))
five_string = "(math.factorial(4)/4)-(4/4)"
print "%s-%i" %(five_string, eval(five_string))
six_string = "((4-4)+math.factorial(4))/4"
print "%s-%i" %(six_string, eval(six_string))
seven_string = "(math.factorial(4)/4)+(4/4)"
print "%s=%i" %(seven_string, eval(seven_string))
eight_string = "(4**2)*4/(4+4)"
print "%s=%i" %(eight_string, eval(eight_string))
nine_sting = "4+4+4/4"
print "%s=%i" %(nine_sting, eval(nine_sting))
ten_string = "(math.factorial(4)+4*4)/4"
print "%s=%i" %(ten_string, eval(ten_string))
eleven_string = "4**2-4-(4/4)"
print "%s=%i" %(eleven_string, eval(eleven_string))
twelve_string = "math.factorial(4)-4*4+4"
print "%s=%i" %(twelve_string, eval(twelve_string))
thirteen_string = "4**2-4+(4/4)"
print "%s=%i" %(thirteen_string, eval(thirteen_string))
