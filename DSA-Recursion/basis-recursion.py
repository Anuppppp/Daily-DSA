# Indirect recursion call "Calling a recursion function from another fucntionm"

def func1(n):
    """
    Recursively prints the flow of function calls from top (n) down to 0,
    and then back from 0 up to n, illustrating how recursive calls work.

    Parameters:
    n (int): A non-negative integer that determines the depth of recursion.

    Behavior:
    - Prints "Inner call" before each recursive call (descending phase).
    - Prints "Outer call" after each recursive call returns (ascending phase).

    Example:
    func1(3)
    Inner call, value of n now is : 3
    Inner call, value of n now is : 2
    Inner call, value of n now is : 1
    Outer call, value of n now is : 1
    Outer call, value of n now is : 2
    Outer call, value of n now is : 3
    """
    if n == 0:
        return 0
    print(f"Inner call, value of n now is : {n}")
    func1(n-1)
    print(f"Outer call, value of n now is : {n}")


def main():
    func1(5)
    return

main()

