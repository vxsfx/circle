import math



def no_pi_circ(r):
    """finds circumfrence given only radius"""

    """
    take a quarter of a circle
    take the hypotenuse of the 2 radius of the quarter

    """

    ##start at 90 deg
    h = math.sqrt(2*r*r)
    #ah, 
    ah = 0
    b=1
    
    for i in range(1, 100):
        hs = (h/2)**2 
        n = math.sqrt(r*r - hs)
        dr = r - n
        h = math.sqrt(dr*dr + hs)
        
        #ah += h
        
        b *= 2##

    #return (h * (2**i) * 4) -> more accurate
    return (h * b * 4) # alt using b

    #add to ah variable instead of alt above, has very large error 
    #return (ah * 4)

if __name__ == "__main__":
    r = 2
    print(2 * math.pi * r)
    print(no_pi_circ(r))

    #find pi
    print(f"pi ≈ {no_pi_circ(r) / (2*r)}")
    print(f"pi = {math.pi}")