def sort_words_with_lengths(words):
    return [(word, len(word)) for word in sorted(words, key=len, reverse=True)]

# Example usage:
words = ["apple", "banana", "strawberry", "kiwi"]
print(sort_words_with_lengths(words))
