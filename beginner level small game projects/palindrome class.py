# x = int(input('enter a number to check if it is a palindrome'))


def is_palindrome(x):
        if x > 0:
            temp = x
            rev_int_elements = []
            while temp > 0:
                digit = temp % 10
                rev_int_elements.append(digit)
                temp = temp // 10

            org_int_numbers = rev_int_elements[::-1]
            return rev_int_elements == org_int_numbers
        elif x == 0:
            return True
        else:
            return False


y = is_palindrome(1956591)
print(y)