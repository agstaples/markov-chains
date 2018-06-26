"""Generate Markov text from text files."""

from random import choice
import sys


def place_to_end(text_string):
    words = text_string.split()
    return (words[-3], words[-2])


def open_and_read_file(file_paths):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    new_string = ""
    # your code goes here
    for file_path in file_paths:
        with open(file_path) as file:
            new_string += file.read().rstrip()
    
    return new_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words = text_string.split()
    chains = {}

    for i in range(len(words) - 1):

        bigram = (words[i], words[i + 1])
        if i + 3 > len(words):
            return chains
        if bigram not in chains:
            chains[bigram] = []
            chains[bigram].append(words[i+2])
        else:
            chains[bigram].append(words[i+2])

    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    bigram = choice(list(chains))
    word1, word2 = bigram[0], bigram[1]
    word3 = choice(chains[bigram])

    words.append(word1)
    words.append(word2)
    words.append(word3)

    while bigram != (place_to_end(input_text)):
        bigram = (word2, word3)
        new_word = choice(chains[bigram])
        words.append(new_word)
        word2 = word3
        word3 = new_word

    return " ".join(words)


input_path = sys.argv[1:]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)
print(random_text)
