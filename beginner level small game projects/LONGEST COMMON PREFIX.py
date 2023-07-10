"""input list of strings"""
STRINGS = input('enter a list of strings here')

def loongest_common_prefix(strs):
    if not strs:
        return " "
    """sort the strings to ensure the shortest string is the first"""
    sorted(strs)
    """initialize the longest common prefix to be the first string in the list"""
    lcp = strs[0]

    """iterate through the charecters of the first string"""
    for i in range(len(lcp)):
        """iterate through remaining strings in the list"""
        for s in strs[1:]:
            """if the charecters at the same position is not as in the first string
            update the longest common prefix and break out of the loop"""
            if s[i] != lcp[i]:
                lcp = lcp[:1]
                break
        else:
            continue
        break

    return lcp


lcp = loongest_common_prefix(STRINGS)

print('the longest common prefix is:', lcp)
