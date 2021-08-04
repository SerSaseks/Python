
from array import *


#Задача
#Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

#Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


#решение 1

# Определяю переменные
i = 0
summ3 = 0
summ5 = 0
total_summ = 0
x_array = array('i', [])

# Заполняю масив последовательности чисел необходимым количеством елементов масива
while i < 999:
    i = i + 1
    x_array.append(i)
    print(x_array)

# Путем перебора всех чисел в масиве нахожу числа кратные 3 и 5
for i in x_array:
    print('i = ',i)
    if i % 3 == 0:
        print('after if summ3 =',i)
        summ3 = summ3 + i
        print('summ3 =', summ3)
    if i % 5 == 0:
        print('after if summ5 =', i)
        summ5 = summ5 + i
        print('summ5 =', summ5)
    print('after iteration','summ3 =',summ3,'summ5 =',summ5)

# Сумирую результаты переборов для 3 и 5
total_summ = summ3 + summ5
# Вывожу результат
print('Сумма кратных 3 =',summ3,'Сумма кратных 5 =', summ5)
print('сумма всех чисел кратных 3 и 5 =',total_summ)


#решение 2

#Определяю переменные

y = 0
z = 0
s = 0

# Нахожу путем перебора всех числа кратных 3 и 5

for x in range(1,1000):
    print(x)
    if x % 3 == 0:
        y = y + x
        print('after if summ3 =', y)
    if x % 5 == 0:
        z = z + x
        print('after if summ5 =', z)
    s = y + z

print('after cicl summ3 =', y)
print('after cicl summ5 = ', z)
print( 'summ 3 and 5 = ',s)



