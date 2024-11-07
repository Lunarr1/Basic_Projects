def main ():
    word_count = {}
    sentence = input("Please enter a sentence: ")
    sentence = sentence.lower()
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word}:{count}")
main()

