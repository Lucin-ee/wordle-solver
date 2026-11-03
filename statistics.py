from convert_txt_to_list import extract_words_from_txt_files

def statistics_on_answers():
    list_answers, _ = extract_words_from_txt_files()
    first_letters = {}
    all_letters = {}

    for word in list_answers : 
        first_letter = word[0]
        if first_letter in first_letters : 
            first_letters[first_letter] += 1
        else : 
            first_letters[first_letter] = 1
            
        for letter in word : 
            if letter in all_letters : 
                all_letters[letter] += 1
            else : 
                all_letters[letter] = 1

    return first_letters, all_letters

first_letters, all_letters = statistics_on_answers()
print("\n\nFIRST LETTERS")
for key, value in first_letters.items():
    print(f"{key}: {value}")

print("\n\nALL LETTERS")
for key, value in all_letters.items():
    print(f"{key}: {value}")


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