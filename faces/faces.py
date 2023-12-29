def main():
    sentence = input("Say something with a smile or frown: ")
    sentence = sentence.replace(":)", "\U0001F642")
    sentence = sentence.replace(":(", "\U0001F641")#Replaces smiles and frowns with actually emojis
    print(sentence)

main()