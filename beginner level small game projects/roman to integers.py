def roman_to_integers(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in s:
        value = roman_map[c]
        if value > prev_value:
            result += value - 2 * prev_value

        else:
            result += value

        prev_value = value

    return result


print(roman_to_integers('MCMXCIV'))