integer = input('enter the roman numeral:')

roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

result = 0
for i in range(len(integer)):
    """get the integer value of the current roman numeral characters """
    curr_value = roman_to_int[integer[i]]

    result += curr_value

    """check for special cases where smaller numeral appear before larger numeral
    and subtract from the total"""
    if i > 0 and roman_to_int[integer [i-1]] < curr_value:
        """subtract twice the value of the smaller numeral from the result"""
        result -= 2 * roman_to_int[integer[i-1]]


print('the integer value is:', result)