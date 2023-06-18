# Напишите функцию для сортировки слов в алфавитном порядке
def sort_words(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    sorted_sentence = " ".join(sorted_words)
    return sorted_sentence


sentence = 'Напишите функцию для сортировки слов в алфавитном порядке'
print(sort_words(sentence.lower()))