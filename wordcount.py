import sys

# put your code here.

def count_word(sys.argv[0]):

    text_file = open(sys.argv[0])

    words = {}

  

    giant_word_list = []

    for line in text_file:
        line = line.strip()
        word_list = line.split(" ")
        # print word_list

        lower_list = [item.lower().strip(',?.') for item in word_list]
        # Is there a way to say "all punctuation" instead of listing them out?


        giant_word_list.extend(lower_list)
        # print giant_word_list

    for word in giant_word_list:
        if word in words:
            words[word] += 1

        else:
            words[word] = 1

    # print giant_word_list


    print words





count_word("test.txt")    

# for loop to split by space

# combine all the lists

# define dictionary of word, count

# for item in list
#     if word in dictionary.keys()
#         count += 1
#     else 
#         add the word to the dictionary

