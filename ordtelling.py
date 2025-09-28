# Oppgave 2.1 - Bokstavtelling av et ord

def cl(word):
    return len(word)

# Loop som teller om du vil flere ganger eller ikke
while True:
    w = input("Write a word: ")
    print(f"The word '{w}' has {cl(w)} letters.")
    a = input("Again? (yes/no): ").lower()
    if a != "yes":
        print("Moving on...")
        break

# Oppgave 2.2 - Litt lik som oppgave 2.2 men teller ord i en setning
print("What about words in a sentence?")
start = input("Do you want to count words in a sentence? (yes/no): ").lower()
if start == "yes":
    def word_count(sentence):
        words = sentence.split()
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        return freq

    while True:
        s = input("Write a sentence: ")
        result = word_count(s)
        print("Word frequencies:")
        for word, count in result.items():
            print(f"'{word}': {count}")
        again = input("How about another sentence? (yes/no): ").strip().lower()
        if again != "yes":
            print("Moving on...")
            break

# Oppgave 2.3 - Full analyse av en setning
print("Now how about a full summary")
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"The sentence has {len(words)} words.")

# Bruker word_count fra tidligere
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word frequencies:")
for word, count in freq.items():
    print(f"'{word}': {count}")

# Bruker cl fra tidligere
print("Letter count for each word:")
for word in words:
    print(f"'{word}': {cl(word)} letters")