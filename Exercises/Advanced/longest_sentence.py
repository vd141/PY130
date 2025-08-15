# Write a program that prints the longest sentence in a string based on the 
# number of words. You should also print the number of words in the longest 
# sentence.

# Sentences may end with periods (.), exclamation points (!), or question marks 
# (?). You should treat any sequence of characters that are not spaces or 
# sentence-ending characters as a word. Thus, -- should count as a word. Log the 
# longest sentence and its word count. Pay attention to the expected output, and 
# be sure you preserve the punctuation from the end of the sentence.

# Note that this problem is about manipulating and processing strings. As such, 
# every detail about the string matters (e.g., case, punctuation, tabs, 
# spaces, etc.).

long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

# store each sentence in a dictionary with the sentence as the key and the word count as the value
# not necessarily space efficient, so i could use two varibles to store the longest sentence and its word count
# if there is a longer sentence, update the longest sentence and its word count

# detect a word
# if a letter follows no character, it is at the start of a sentence
# if a letter follows a space preceded by punctuation, it is at the start of a sentence
# if a letter is followed by a space or by punctuation, it is at the end of a sentence
# words in a sentence are split by spaces
# sentences are split by punctuation
# first, split the paragraph by punctuation
# then, split each sentence by white space
# count the length of each sentence
# use regular expressions

import re

# detect a sentence
PUNCTUATION = r'[!.?]+'

def longest_sentence(text):

    # split text into sentences
    sentences = re.split(PUNCTUATION, text)
    max_sentence = ""
    max_count = 0
    for sentence in sentences:
        chopped_sentence = sentence.split()
        if len(chopped_sentence) > max_count:
            max_sentence = sentence
            max_count = len(chopped_sentence)

    print(max_sentence)
    print(f'The longest sentence has {max_count} words.')


longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.