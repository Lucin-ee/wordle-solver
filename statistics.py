from convert_txt_to_list import extract_words_from_txt_files

def statistics_on_answers():
    list_answers, _ = extract_words_from_txt_files()
    first_letters = {}
    second_letters = {}
    third_letters = {}
    fourth_letters = {}
    fifth_letters = {}
    all_letters = {}

    for word in list_answers : 
        first_letter = word[0]
        second_letter = word[1]
        third_letter = word[2]
        fourth_letter = word[3]
        fifth_letter = word[4]

        if first_letter in first_letters : 
            first_letters[first_letter] += 1
        else : 
            first_letters[first_letter] = 1

        if second_letter in second_letters : 
            second_letters[second_letter] += 1
        else : 
            second_letters[second_letter] = 1

        if third_letter in third_letters : 
            third_letters[third_letter] += 1
        else : 
            third_letters[third_letter] = 1

        if fourth_letter in fourth_letters : 
            fourth_letters[fourth_letter] += 1
        else : 
            fourth_letters[fourth_letter] = 1

        if fifth_letter in fifth_letters : 
            fifth_letters[fifth_letter] += 1
        else : 
            fifth_letters[fifth_letter] = 1

        for letter in word : 
            if letter in all_letters : 
                all_letters[letter] += 1
            else : 
                all_letters[letter] = 1

    return list_answers, first_letters, second_letters, third_letters, fourth_letters, fifth_letters, all_letters

def used_letters_percentage(list_answers: dict, first_letters: dict, second_letters: dict, third_letters: dict, fourth_letters: dict, fifth_letters: dict, all_letters: dict): 
    used_letters_percentage = {}
    first_letters_percentage = {}
    second_letters_percentage = {}
    third_letters_percentage = {}
    fourth_letters_percentage = {}
    fifth_letters_percentage = {}
    total_words = len(list_answers)
    total_letters = 5 * total_words

    for key, value in first_letters.items(): 
        first_letters_percentage[key] = value/total_words
    for key, value in second_letters.items(): 
        second_letters_percentage[key] = value/total_words
    for key, value in third_letters.items(): 
        third_letters_percentage[key] = value/total_words
    for key, value in fourth_letters.items(): 
        fourth_letters_percentage[key] = value/total_words
    for key, value in fifth_letters.items(): 
        fifth_letters_percentage[key] = value/total_words
        
    for key, value in all_letters.items(): 
        used_letters_percentage[key] = value/total_letters

    return first_letters_percentage, second_letters_percentage, third_letters_percentage, fourth_letters_percentage, fifth_letters_percentage, used_letters_percentage

def write_to_txt_file(list_of_statistics : list[dict], file_name : str):
    file = open(file_name + ".txt", "w") 
    orders = ["FIRST LETTERS", "SECOND LETTERS", "THIRD LETTERS", "FOURTH LETTERS", "FIFTH LETTERS", "ALL USED LETTERS"]
    for dict_idx in range(len(list_of_statistics)):
        print(f'type(list_of_statistics)', type(list_of_statistics))
        print(f'type(list_of_statistics[0])', type(list_of_statistics[0]))
        file.write("\n")
        file.write(orders[dict_idx])
        dicti = list_of_statistics[dict_idx]
        for key, value in dicti.items():
            file.write(f"", key, ": ", value)
    return 

def write_to_txt_file(header: str, list_of_statistics : list[dict], file_name : str):
    file = open(file_name + ".txt", "w") 
    orders = ["FIRST LETTERS", "SECOND LETTERS", "THIRD LETTERS", "FOURTH LETTERS", "FIFTH LETTERS", "ALL USED LETTERS"]

    for dict_idx in range(len(list_of_statistics)):
        
        file.write("\n")
        file.write(orders[dict_idx])
        dicti = list_of_statistics[dict_idx]

        write_one_dict_to_txt_file(file, dicti, file_name)

    file.close()
    
    return 

def write_one_dict_to_txt_file(file, dicti: dict, file_name: str): 

    for key, value in dicti.items():
        file.write("\n")
        file.write(str(key) + ": " + str(value))

    return 

list_answers, first_letters, second_letters, third_letters, fourth_letters, fifth_letters, all_letters = statistics_on_answers()
first_letters_percentage, second_letters_percentage, third_letters_percentage, fourth_letters_percentage, fifth_letters_percentage, used_letters_percentage = used_letters_percentage(list_answers, first_letters, second_letters, third_letters, fourth_letters, fifth_letters, all_letters)

list_counts = [first_letters, second_letters, third_letters, fourth_letters, fifth_letters, all_letters]
list_perc = [first_letters_percentage, second_letters_percentage, third_letters_percentage, fourth_letters_percentage, fifth_letters_percentage, used_letters_percentage]

write_to_txt_file("COUNTS", list_counts, "used_letters_count")
write_to_txt_file("PERCENTAGES", list_perc, "used_letters_percentage")

# count = open("used_letters_count.txt", "w") 
# percentage = open("used_letters_percentage.txt", "w") 

# first_letters, all_letters = statistics_on_answers()
# print("\n\nFIRST LETTERS")
# for key, value in first_letters.items():
#     print(f"{key}: {value}")

# print("\n\nALL LETTERS")
# for key, value in all_letters.items():
#     print(f"{key}: {value}")


# FIRST LETTERS
# a: 141
# b: 173
# c: 198
# d: 111
# e: 72
# f: 136
# g: 115
# h: 69
# i: 34
# j: 20
# k: 20
# l: 88
# m: 107
# n: 37
# o: 41
# p: 142
# q: 23
# r: 105
# s: 366
# t: 149
# u: 33
# v: 43
# w: 83
# y: 6
# z: 3


# ALL LETTERS
# a: 979
# b: 281
# c: 477
# k: 210
# s: 669
# e: 1233
# t: 729
# y: 425
# o: 754
# h: 389
# r: 899
# i: 671
# d: 393
# l: 719
# u: 467
# v: 153
# n: 575
# g: 311
# p: 367
# m: 316
# f: 230
# x: 37
# w: 195
# z: 40
# j: 27
# q: 29