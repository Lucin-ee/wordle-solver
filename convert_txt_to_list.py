
def extract_words_from_txt_files(): 
    list_answers = []
    list_guesses = []
    with open('nyt-answers.txt') as f:
        for line in f:
            list_answers.append(line.strip())

    list_guesses = []
    with open('nyt-guesses.txt') as f:
        for line in f:
            list_guesses.append(line.strip())

    return list_answers, list_guesses

