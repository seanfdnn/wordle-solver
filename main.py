"""
A small Python application to solve Wordle puzzles.

Licensed under CreativeCommons Attribution-NonCommercial-ShareAlike 4.0 2022 Sean Dunn
"""
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def main():
    print("""
    Sean's Wordle Bot

    Respond reply with unmatched letters with an asterisk, "*",
    letters matched, but not in the correct position as lowercase, 
    letters matched and in the correct position as uppercase.

    I.e. 
        Guess:    PANIC
        Response  *anI*
    """)

    words = load_words()

    rejected_letters = set()
    required_letters = set()
    letters_rejected_in_positions = set() # Array of tuple of (letter, position)
    letters_required_in_positions = set() # Set of tuple of (letter, position)

    while True:
        # Pick the highst-ranked word to guess
        guessed_word = generate_guess(words)

        rejected_letters, required_letters, letters_rejected_in_positions, letters_required_in_positions = prompt_and_parse_response(
            guessed_word,
            rejected_letters,
            required_letters,
            letters_rejected_in_positions,
            letters_required_in_positions)

        words = filter(lambda word: does_word_not_contain_any_letters(word, rejected_letters),words)
        words = filter(lambda word: does_word_contain_all_letters(word, required_letters), words)
        words = filter(lambda word: does_word_not_have_any_letters_at_forbidden_position(word, letters_rejected_in_positions), words)
        words = filter(lambda word: does_word_have_letters_at_required_position(word, letters_required_in_positions), words)
        words = list(words)

def generate_guess(word_list):
    letter_freq = calculate_letter_frequency(word_list)
    sorted_word_list = calculate_letter_frequency_score_for_words(letter_freq, word_list)
    print(f'\n Next best guesses: {[w[0] for w in sorted_word_list[0:5]]}\n')
    return sorted_word_list[0][0]

def calculate_letter_frequency(word_list):
    """Calculates a dictionary with each letter being the key, and the value being the frequency of that letter in the dictionary"""
    letter_dict = {l:0 for l in ALPHABET}
    for word in word_list:
        for letter in word:
            letter_dict[letter] += 1

    # Normalize the frequency
    factor=1.0/sum(letter_dict.values())
    normalised_letter_dict = {k: v*factor for k, v in letter_dict.items() }
    return normalised_letter_dict

def calculate_letter_frequency_score_for_words(letter_frequency_dict, word_list):
    """Returns a sorted dict of words with the values being a score of the sum of letter frequencies"""

    # Cast word into a set of characters so that scores aren't inflated by duplicate characters
    word_scores = [(word, sum(map(letter_frequency_dict.__getitem__, set(word)))) for word in word_list]
    # Sort in reverse order, with the higest score at the top
    return sorted(word_scores, key=lambda item: item[1],reverse=True)

def load_words():
    """Loads words from a dictionary file, and filters to just 5-letter words"""
    with open ('dict.txt','r') as f:
        # Read the dictionary and convert to all uppercase
        words = [x.upper() for x in f.read().splitlines()]

    # If using a dictionary that contains words longer than length 5, limit to only 5-letter words
    word_length = 5

    words_of_required_length = list(filter(lambda w: len(w) == word_length, words))
    return words_of_required_length

def does_word_not_contain_any_letters(word, letters):
    """Returns True if none of the letters are contained in the word, otherwise False"""
    for l in word:
        for j in letters:
            if l == j:
                return False
    return True

def does_word_contain_all_letters(word, letters):
    """Returns True if all the letters are contained within the word"""
    for l in letters:
        if not l in word:
            return False
    return True

def does_word_not_have_any_letters_at_forbidden_position(word, letter_position):
    """Returns True if the word does not have any letters at forbidden positions in the word"""
    for l, pos in letter_position:
        if word[pos] == l:
            return False
    return True

def does_word_have_letters_at_required_position(word, letter_position):
    """Returns True if the word has all letters in the required positions"""
    for l, pos in letter_position:
        if word[pos] != l:
            return False
    return True

def prompt_and_parse_response(word, rejected_letters, required_letters, letters_rejected_in_positions, letters_required_in_positions):
    print('Guess:    ' + word)
    print('Response: ', end='') 
    response = input()

    if response == word:
        print('Congratulations!')
        exit(0)

    for i, l in enumerate(response):
        if l.islower():
            l_upper = l.upper()
            required_letters.add(l_upper)
            letters_rejected_in_positions.add((l_upper,i))
        elif l.isupper():
            required_letters.add(l)
            letters_required_in_positions.add((l,i))
        else:
            rejected_letters.add(word[i])
    
    return rejected_letters, required_letters, letters_rejected_in_positions, letters_required_in_positions
    


if __name__ == '__main__':
    main()