def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0 and b>0 and c>0:
        s=3
    if a>0 and b>0 and c<0 or a>0 and b<0 and c>0 or a<0 and b>0 and c>0:
        s=2
    if a>0 and b<0 and c>0 or a<0 and b>0 and c>0 or a>0 and b>0 and c<0:
        s=1


    return s
print (main(1,2,3))