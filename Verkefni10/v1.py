import string

sentence = input("Input a sentence: ")

# Here you should add the missing part
new = list(sentence)
unique_letters = []

for i in new:
    if i.isalpha:
        if i in unique_letters:
            continue
        elif i in string.punctuation:
            continue
        elif i in string.whitespace:
            continue
        else:
            unique_letters.append(i)
    else:
        continue
    
print("Unique letters:", unique_letters)
