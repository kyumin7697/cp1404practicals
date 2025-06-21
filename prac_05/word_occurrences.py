"""""
Word Occurrences
Estimate: 40 minutes
Actual:
"""
#Text: this is a collection of words of nice words this is a fun thing it is
def main():
    text = input("Text: ")
    words = text.split()
    word_to_count = {}

    for word in words:
        word = word.lower()
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    print(word_to_count)

main()
