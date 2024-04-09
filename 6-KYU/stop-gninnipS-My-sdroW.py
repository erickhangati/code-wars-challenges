"""
Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, but with all words that
have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters
and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"
"""


def spin_words(sentence):
    reversed_sentence = []

    for word in sentence.split(" "):
        word_alpha = "".join(filter(lambda x: x.isalpha(), word))

        if len(word_alpha) >= 5:
            reversed_sentence.append(word_alpha[::-1])
        else:
            reversed_sentence.append(word)

    return " ".join(reversed_sentence)


res = spin_words("Stop gninnipS My sdroW!")
print(res)
