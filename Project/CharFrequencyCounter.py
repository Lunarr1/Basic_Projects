def main():
    char_count = {} #make a dictionary
    sentence = input("Please input a sentence:") #accept input
    sentence = sentence.lower() #lowercase everything

    for char in sentence: #for every character in "sentence"
        if char.isalpha(): #check if every character in "sentence" is alplhabetical alpha = alphabetical
            if char in char_count: #if the characters is in char_count
                char_count[char] += 1 #add one to the count
            else:
                char_count[char] = 1 #add a new one, and add one to the count

    for char, count in char_count.items(): #for every character, and count in char_count
#char_count.items() by using .items(),it calls the dictionary's both key and value and display
        print(f"{char}: {count}")

main()