# Text Analyzer program.

delated_words = ('a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would',
                 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'etc', 'to', 'the', 'in', 'be',
                 'no', 'for', 'that')
punctuation = [".", ",", ":", ";", "'", '!', '"', '-']


def lower(pretext):
    pretext_2 = pretext.lower().split()
    return pretext_2


def pretext_conversion(pretext_2):
    text_1 = []
    for word in pretext_2:
        if not word in delated_words:
            text_1.append(word)
    return text_1


def delite_punctuation(text_1):
    text = []
    for word in text_1:
        if not word in punctuation:
            text.append(word)
    return text


# Calculate words quantity;

def count_words(text):
    '''
    The function subtracts one list from another and returns the result.
    :param list1: custom user list
    :type list1: list
    :return: the result of lists' subtracts
    '''
    return len(text)


# Extract text dictionary - unique words;

def count_unique_words(text):
    '''
    The function subtracts one list from another and returns the result.
    :param list1: custom user list
    :type list1: list
    :return: the result of lists' subtracts
    '''
    list = []
    for word in text:
        if not word in list:
            list.append(word)
    return list


# Find keywords - top 3 most frequent words;
def count_top_3_words(text):
    '''
    The function subtracts one list from another and returns the result.
    :param list1: custom user list
    :type list1: list
    :return: the result of lists' subtracts
    '''
    text_dictionary = {i: text.count(i) for i in text}
    return text_dictionary


# Calculate frequency for each word - word quantity / all words quantity * 100.

def freq(text):
    str_list = text
    unique_words = set(str_list)
    for words in unique_words:
        print('Frequency of ', words, 'is :', int((str_list.count(words) / len(str_list)) * 100), '%')


pretext = ('Lion cubs play-fight to learn social skills . Rats play to learn emotional skills . '\
           'Monkeys play to learn cognitive skills . '\
           'And yet, in the last century, we humans have convinced ourselves that play is useless, '\
           'and learning is supposed to be boring. Gosh, no wonder we’re all so miserable. '\
           'Welcome to Explorable Explanations, a hub for learning through play!')

pretext_2 = lower(pretext)
text1 = pretext_conversion(pretext_2)
text = delite_punctuation(text1)

words_quantity = count_words(text)
print(words_quantity)

count_unique_words = count_unique_words(text)
print(count_unique_words)

count_top_3_words = count_top_3_words(text)
j = 0
for key, value in sorted(count_top_3_words.items(), key=lambda item: item[1], reverse=True):
    print("%s - %s" % (key, value))
    j += 1
    if j >= 3:
        break

freq = freq(text)
print(freq)