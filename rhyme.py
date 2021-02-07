"""
@TODO: 
1. Write the final function that generates the final output.
2. Clean the code. 
3. Add clarifying comments.

@WHAT: Code that generates new content?
@WHY: ...
@ALTERNATIVES: ...
"""

from langdetect import DetectorFactory, detect, detect_langs
from gensim.parsing.preprocessing import remove_stopwords
import pronouncing

import re
import random


DetectorFactory.seed = 0
random.seed(0)




def get_parsed_tweet(tweet):
    """
    @WHAT: parses a tweet with a string dtype to an array dtype.
    @WHY: so that the tweet can be used for other functions more easily
    @ALTERNATIVES: ???

    tweet: a tweet from twitter. [array]
    """
    parsed_tweet = tweet.lower()
    parsed_tweet = re.sub("[^\w]", " ", tweet).split()
    return parsed_tweet


def get_filtered_tweet(tweet):
    """
    @WHAT: a function that removes the words with more than three letters from a parsed tweet.
    @WHY: so that I can search for rhyme_words without having to consider abbreviations or slang.
    @ALTERNATIVES: ???
    """

    tweet = remove_stopwords(tweet)
    filtered_tweet = [word for word in tweet.lower() if len(word) > 3]
    return filtered_tweet


def get_indexes(words_to_change, original_sentence):
    """
    Returns a list of indexes of words within the original tweet/sentence that 
    we want to change to rhyme_words.

    words_to_change: list of words that will change to rhyme_words.       [array]
    original_sentence: array of the original input sentence or tweet.     [array]

    """
    index_list = []
    for i in words_to_change:
        index = original_sentence.index(i)
        index_list.append(index)
    return index_list


def get_rhyme_words(sentence, index_list):
    """
    Takes a sentence (array) with words (elements) as input and 
    returns an array with words that rhyme with the original 
    elements of the sentence array.

    sentence: array
    """

    rhyme_words = []

    for word in sentence:
        rhyme_word = pronouncing.rhymes(word)
        # if there isn't a rhyme_word for word
        if rhyme_word == []:
        # @WHAT: removes this word from the index_list because it doesn't have a rhyme_word
        # @WHY: so that we can still use index_list to replace the original words with the rhyme_words.
        # @ALTERNATIVES: ??
            no_rhyme_word_index = index_list[sentence.index(word)]
            index_list.remove(no_rhyme_word_index)

            # removes the word from the input sentence array
            sentence.remove(word)

            print("no words found that rhyme with '{}'\n".format(word))
        else:
            chosen_rhyme_word = random.choice(rhyme_word)
            rhyme_words.append(chosen_rhyme_word)
            print("'{}' rhymes with '{}'\n\n".format(word, chosen_rhyme_word))

    return rhyme_words


# def rhyme_tweet(tweet):
#     """
#     WIP:
#     get_words_to_rhyme and parse_tweet need to be written.

#     @WHAT: This function is supposed to generate the final output.
#     """
    # words_to_rhyme = get_words_to_rhyme(tweet)  # Needs to be created
    # parsed_tweet = parse_tweet(tweet)           # Needs to be created

    # indexes = get_indexes(words_to_rhyme, parsed_tweet)
    # rhyme_words = get_rhyme_words(parsed_tweet)

    # # creating the new tweet by replacing the original words with the rhyme_words
    # for i in indexes:
    #     for n in range(0, len(rhyme_words)+1)
    #     parsed_tweet[i] = rhyme_words[n]
    
    # return parsed_tweet