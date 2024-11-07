def main():
    letter_count = {}
    sentence = input("Please enter a sentence: ")
    sentence = sentence.lower()  # Make it case-insensitive
    
    for char in sentence:
        if char.isalpha():  # Only consider alphabetic characters
            if char in letter_count:
                letter_count[char] += 1  # Increment count if letter already exists
            else:
                letter_count[char] = 1  # Add new letter with a count of 1
    
    # Print letters in alphabetical order
    for letter in sorted(letter_count.keys()):
        print(f"{letter}: {letter_count[letter]}")

main()
