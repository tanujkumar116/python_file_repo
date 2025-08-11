import string

def word_frequency(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    paragraph = "Hello world! This is a test. Hello again, world."
    frequencies = word_frequency(paragraph)
    for word, count in sorted(frequencies.items()):
        print(f"{word}: {count}")
