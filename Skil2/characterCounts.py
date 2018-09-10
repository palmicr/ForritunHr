import string
text=str(input("Enter a sentence: "))
uppercase_count = 0
lowercase_count = 0
digit_count = 0
punctuation_count = 0
for c in text:
    if(c == " "):
        continue
    elif(c.islower()):
        lowercase_count = lowercase_count + 1
    elif(c.isupper()):
        uppercase_count = uppercase_count + 1
    elif(c.isdigit()):
        digit_count = digit_count + 1
    elif(c in string.punctuation):
        punctuation_count = punctuation_count + 1
print("{:>15}{:>5}".format("Upper case",str(uppercase_count)))
print("{:>15}{:>5}".format("Lower case",str(lowercase_count)))
print("{:>15}{:>5}".format("Digits",str(digit_count)))
print("{:>15}{:>5}".format("Punctuation",str(punctuation_count)))