t = (5, 3, 1, 7, 9, 4, 6, 8, 2)

# Сначала преобразуем кортеж в список
t_list = list(t)

# Используем метод sort() для сортировки списка в обратном порядке
t_list.sort(reverse=True)

# Преобразуем отсортированный список обратно в кортеж
sorted_t = tuple(t_list)

# Выводим результат
print(sorted_t)
