#a simple testing example
def add_three(x:int) -> int:
    return x + 3

def multiply_by_two(x:int) -> int:
    return x * 2      #mutant found as 2*2 is same as 2+2

def main():
    assert add_three(1) == 4
    assert add_three(2) == 5
    assert add_three(3) == 6
    assert  multiply_by_two(2) == 4
    print("all tests pass")


if __name__  == '__main__':
    main()