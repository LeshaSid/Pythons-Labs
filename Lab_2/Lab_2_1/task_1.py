text = input("Введите текст: ")

words = text.split()

word_count = {}
for word in words:
    cleaned_word = word.lower().strip('.,!?;:"')
    if cleaned_word:
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

sorted_word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))

print("Словарь {слово: количество} (отсортированный по частоте):")
for word, count in sorted_word_count.items():
    print(f"'{word}': {count}")

print(f"Количество уникальных слов: {len(sorted_word_count)}")