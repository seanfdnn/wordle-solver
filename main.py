
from email.utils import collapse_rfc2231_value


ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

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
    word_scores = {word: sum(map(letter_frequency_dict.__getitem__, word)) for word in word_list} 
    # Sort in reverse order, with the higest score at the top
    return dict(sorted(word_scores.items(), key=lambda item: item[1],reverse=True))

def has_no_letter_repetitions(word):
    """Returns `false` if a word repeats a letter more than once"""
    for l in word:
        count = 0
        for j in word:
            if l == j:
                count += 1
        if count > 1:
            return False
    return True

def load_words():
    with open ('dict2.txt','r') as f:
        words = [x.upper() for x in f.read().splitlines()]

    word_length = 5

    five_letter_words = list(filter(lambda w: len(w) == word_length, words))
    return five_letter_words

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

def does_word_not_have_any_letters_at_forbidden_position(word, letter_position_dict):
    """Returns True if the word does not have any letters at forbidden positions in the word"""
    for l, pos in letter_position_dict.items():
        if word[pos] == l:
            return False
    return True

def does_word_have_letters_at_required_position(word, letter_position_dict):
    """Returns True if the word has all letters in the required positions"""
    for l, pos in letter_position_dict.items():
        if word[pos] != l:
            return False
    return True

def eliminate_words_with_rejected_letters(word_list, letters):
    return list(filter(lambda word: does_word_not_contain_any_letters(word, letters),word_list))

def eliminate_words_without_required_letters(word_list, letters):
    return list(filter(lambda word: does_word_contain_all_letters(word, letters), word_list))

def eliminate_words_with_letters_in_forbidden_positions(word_list, letter_position_dict):
    return list(filter(lambda word: does_word_not_have_any_letters_at_forbidden_position(word, letter_position_dict), word_list))

def eliminate_words_without_letters_in_required_positions(word_list, letter_position_dict):
    return list(filter(lambda word: does_word_have_letters_at_required_position(word, letter_position_dict), word_list))

def main():
    words = load_words()
    words_without_letter_repetitions = list(filter(has_no_letter_repetitions, words))
    letter_frequency_dict = calculate_letter_frequency(words)
    words_with_scores = calculate_letter_frequency_score_for_words(letter_frequency_dict, words_without_letter_repetitions)
    #print(words_with_scores)

    w = eliminate_words_with_rejected_letters(words_without_letter_repetitions,"ROSEDTL")
    w = eliminate_words_without_required_letters(w, "AINC")
    w = eliminate_words_with_letters_in_forbidden_positions(w, {"A": 0, "I":1, "A": 3})
    w = eliminate_words_without_letters_in_required_positions(w, {"I": 3})

    w = {k:v for k,v in words_with_scores.items() if k in w}
    print(w)


if __name__ == '__main__':
    main()