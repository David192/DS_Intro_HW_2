def reverse(sentence, reverse_word):
    check_string = isinstance(reverse_word, str)
    if check_string == False:
        return "invalid input"
    elif reverse_word not in sentence:
        return "The word was not found"
    else:
        reverse = reverse_word[::-1]
        new_sentence = sentence.replace(reverse_word, reverse, 1)
        return new_sentence


