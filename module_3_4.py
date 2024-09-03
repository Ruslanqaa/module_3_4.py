def single_root_words(root_word, *other_words):
    same_words = []  # Инициализируем пустой список для подходящих слов
    root_word_lower = root_word.lower()  # Приводим root_word к нижнему регистру для сравнения

    for word in other_words:
        word_lower = word.lower()  # Приводим слово к нижнему регистру
        # Проверяем, содержит ли одно слово другое
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполнено

    return same_words  # Возвращаем список найденных слов


# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)