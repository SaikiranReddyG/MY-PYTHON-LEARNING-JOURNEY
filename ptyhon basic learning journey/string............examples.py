                                          #various examples
#QUESTION 1>>> program to reverse the string
s = input('enter a valid string')
#1st way
print(s[::-1])
#2nd way
print(''.join(reversed(s)))





#QUESTION 2>>>   program to reverse order of words
s = input('enter any string')
y = s.split()
y1 = []
i = len(y)-1
while i>=0:
    y1.append(y[i])
    i = i-1
output =''.join(y1)
print(output)

#chatgpt way
def revrese_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

string = "gangula sai kiran reddy"
reversed_string = revrese_words(string)
print(reversed_string)





#QUESTION 3>>>   program to reverse internal content of each words
s = input('enter some string')
y = s.split()
y1 = []
i = 0
while i<len(y):
    y1.append(y[i][::-1])
    i = i+1
output =''.join(y1)
print(output)
#chat gpt way
def revrese_words_contents(string):
    words = string.split()
    reversed_words = [words[::-1]for word in words]
    return " ".join(reversed_words)

string = "gangula sai kiran reddy"
reversed_string_contents = revrese_words_contents(string)
print(reversed_string_contents)




#QUESTION 4>>>   program to print charecters at odd and even positions of a string
s = input('enter some string')
print('charecters at the even positions',s[::2])
print('charecters at the odd positions',s[1::2])

#2nd way
s= input('enter some charecters')
i = 0
print('charecters at even')
while i<len(s):
    print(s[i],end=',')
    i = i+2
i = 1
print('charecters at odd')
while i<len(s):
    print(s[i],end=',')
    i = i+2



#QUESTION 5>>>   program to merge alternate charecters of two strings
q = input('enter 1st string')
w = input('enter 2nd string')
output=''
i,j = 0,0
while i<len(q) or j<len(w):
    if i<len(q):
        output=output+q[i]
        i += 1
    if j<len(w):
        output = output+w[j]
        j += 1
print(output)

#CHATGPT way
def merge_strings(s1,s2):
    merged = ""
    for i in range(min(len(s1), len(s2))):
        merged += s1[i] + s2[i]
    merged += s1[i+1:] + s2[i+1:]
    return  merged
s1 = "sacjksncsjkldc"
s2 = "74598379879"
merged_string = merge_strings(s1,s2)
print(merged_string)


#QUESTION 5>>>  sort the charecters of the strings with alphabets followed by numbers
s = input("enter a string")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1 = s1+x
    else:
        s2 = s2+x
for x in sorted (s1):
        output=output+x
for x in sorted (s2):
    output=output+x
print(output)

#CHATGPT way
def sort_string(string):
    alpha = ""
    num = ""
    for char in string:
        if char.isalpha():
            alpha +=char
        elif char.isnumeric():
            num += char
    return ' '.join(sorted(alpha) + sorted(num))

string = "ajnkjaned53dsakdf432"
sorted_string = sort_string(string)
print(sorted_string)


#QUESTION  6>>>> Input: a4b3c2     Output: aaaabbbcc
#chat gpt way
input_str = 'a4b3c2'
output_str = ""
current_char = ""

for i in input_str:
    if i.isalpha():
        current_char = i
    else:
        output_str += current_char * int(i)

print(output_str)



#QUESTION  7>>>> Input: a4k3b2     Output: aeknbd
#chat gpt way
given_str = "a4k3b2"
needed_str = ""
present_char = ""
for i in given_str:
    if i.isalpha():
        present_char = i
        needed_str += present_char
    else:
        for j in range(int(i)):
            needed_str += chr(ord(present_char) + j + 1)
print(needed_str)




#QUESTION  8>>>> program to remove duplicate charecters from given input string
#chat gpt way
s = input('enter a input string to eliminate duplicates')
output_str = ""
for i in s:
    if i not in output_str:
        output_str += i
print(output_str)






#QUESTION  8>>>> program to find no of occurances of each  charecters from given input string
#chat gpt way
input_str = input("enter a string required for the count")
char_count = {}
for i in input_str:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print(char_count)



#QUESTION  9>>>> program with Input: 'one two three four five six seven'   Output: 'one owt three ruof five xis seven'
#chat gpt way
d =  input('enter any string')
h = d.split()
h1 = []
i = 0
while i<len(h):
    if i%2==0:
         h1.append(h[i])
    else :
        h1.append(h[i][::-1])

        i= i+1
output =' '.join(h1)
print('original string:',d)
print('output sstring:',output)