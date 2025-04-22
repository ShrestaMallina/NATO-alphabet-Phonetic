student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

#
# student_data_frame = pandas.DataFrame(student_dict)




#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas
data= pandas.read_csv("nato_phonetic_alphabet.csv")
# alpha_words = pandas.DataFrame(data)
# new_dict = {letter:code for (letter,code) in alpha_words.iterrows()}#{row.letter:row.code for(letter,code) in alpha_words.iterrows()}
# n_dict = {letter:code for (letter,code) in new_dict.values()}
phonetic_dict ={row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic():
    user = input(f"enter a word:").upper()
    try:
        # final_list = [n_dict[word] for word in user if word in n_dict.keys()]
    # {new_dict[letter]for letter in user}
        final_list = [phonetic_dict[letter] for letter in user]
    except  KeyError:
        print("Sorry,only letters in alphabetS, PLEASE..")
        generate_phonetic()
    else:
         print(final_list)
generate_phonetic()




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

