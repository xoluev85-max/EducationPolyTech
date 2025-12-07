numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = numbers.index(None)
total = 0
for n in numbers:
    if n is not None:
        total += n
average = total / len(numbers)
numbers[missing_index] = average
print("Измененный список:", numbers)
# TODO заменить значение пропущенного элемента средним арифметическим
