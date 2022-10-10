def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==1:
        s='positive odd number'
    if a>0 and a%2==0:
        s="positive even number"
    if a<0 and a%2==1:
        s= "negative odd number"
    if a<0 and a%2==0:
        s="negative even number"
    if a==0:
        s="the number is zero"
    return