
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
    """Returns a dict of words with the values being a score of how """

def has_letter_repititions(word):
    """Returns `true` if a word repeats a letter more than once"""
    for l in word:
        for j in word:
            if l == j:
                return True
    return False

def load_words():
    with open ('dict.txt','r') as f:
        words = f.read().splitlines()

    word_length = 5

    five_letter_words = list(filter(lambda w: len(w) == word_length, words))
    return five_letter_words

def main():
    words = load_words()
    words_without_letter_repetitions = list(filter(has_letter_repititions, words))
    print(calculate_letter_frequency(words))

if __name__ == '__main__':
    main()