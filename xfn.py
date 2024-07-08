def mid(word):
    length_of_word = len(word)
    modulo_value = length_of_word % 2
    if modulo_value == 1:
        middle_index = int(length_of_word / 2)
        letter = word[middle_index]
        return(letter)
    else:
        return("")


