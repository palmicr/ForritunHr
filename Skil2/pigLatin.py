or_word = input("Enter a word: ")
while or_word != ".":
    to_move = ""
    count = 0
    if len(or_word) > 0 and or_word.isalpha():
        if or_word[0] in 'aeiou':
            pl_word = or_word + "yay"
        else:
            for char in or_word:
                if char not in 'aeiou':
                    to_move += char
                    count += 1
                elif char in 'aeiou':
                    break
            pl_word = or_word[count:] + to_move + "ay"
        print(pl_word)
    or_word = input("Enter a word: ")