# Функция для поиска общих участников
def find_common_participants(group1, group2, separator=','):
    list1 = group1.split(separator)
    list2 = group2.split(separator)

    common = []

    for name in list1:
        if name in list2 and name not in common:
            common.append(name)

    common.sort()
    return common


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# Проверка работы функции
result = find_common_participants(participants_first_group, participants_second_group)
print(result)

# Проверка с другим разделителем
participants_first_group_alt = "Иванов|Петров|Сидоров"
participants_second_group_alt = "Петров|Сидоров|Смирнов"

result_alt = find_common_participants(
    participants_first_group_alt,
    participants_second_group_alt,
    separator="|"
)
print(result_alt)

