# TODO  Напишите функцию count_letters

# TODO Напишите функцию calculate_frequency

# TODO Распечатайте в столбик букву и её частоту в тексте
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

def count_letters(text):
    letters_count = {}

    for ch in text.lower():
        if ch.isalpha():
            if ch in letters_count:
                letters_count[ch] += 1
            else:
                letters_count[ch] = 1

    return letters_count


def calculate_frequency(letters_dict):
    frequency_dict = {}
    total_letters = 0

    for count in letters_dict.values():
        total_letters += count

    for letter, count in letters_dict.items():
        frequency_dict[letter] = count / total_letters

    return frequency_dict


letters = count_letters(main_str)
frequencies = calculate_frequency(letters)

for letter, freq in frequencies.items():
    print(f"{letter}: {freq:.2f}")

