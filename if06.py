def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    counter=0
    counter1=0
    if a<0 :
        counter+=1
    else:
        counter1+=1
        
    if b<0:
        counter+=1
    else:
        counter1+=1
    if c<0:
        counter+=1
    else:
        counter1+=1
    if counter1>counter:
        s="there are a lot of positive numbers"
    else:
        s="there are a lot of negative numbers"



    return s
print (main(1,2,-3))