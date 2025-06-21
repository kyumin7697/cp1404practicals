"""""
Word Occurrences
Estimate: 40 minutes
Actual: 43 minutes
"""

#Text(ex): this is a collection of words of nice words this is a fun thing it is
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

    sorted_words = sorted(word_to_count.keys())

    max_word_length = max(len(word) for word in sorted_words)

    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_to_count[word]}")

main()
