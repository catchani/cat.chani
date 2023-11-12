# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, coma=','):
    list_1 = first_group.split(coma)
    list_2 = second_group.split(coma)

    all_participants = list(set(list_1).intersection(list_2))
    all_participants.sort()
    return all_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)


# TODO Провеьте работу функции с разделителем отличным от запятой
