from pandas import read_csv
# Create NATO dictionary from csv file
nato_alphabet = read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

# Ask user for a word and return each letter as NATO alphabet
input_word = input("Enter a word: ")
output_list = [nato_dict[letter.upper()] for letter in input_word]
print(output_list)


