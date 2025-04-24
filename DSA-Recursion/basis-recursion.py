def func1(n):
    if n == 0:
        return 0
    print(f"Inner call, value of n now is : {n}")
    func1(n-1)
    print(f"Outer call, value of n now is : {n}")


def main():
    func1(5)
    return

main()

