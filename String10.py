def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    d = "({}+{})*2={}".format(x,y,2*(x+y))
    return d
print(main(3,4))