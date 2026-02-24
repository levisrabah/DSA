# A program that reverses word order

# def reverse_word_order(s):
#     return ' '.join(s.split()[::-1])
# print(reverse_word_order("I love RedianSoftware"))

# Reverses each word in the string but keeps the word order the same
def reverse_each_word(s):
    return ' '.join(word[::-1] for word in s.split())
print(reverse_each_word("I love RedianSoftware"))