# Запрос показателей:
print('ВВЕДИТЕ ОБЩИЕ УСЛОВИЯ')
turbidity = int(input('Какая сейчас вода? \n 1 - прозрачная, 2 - мутная: '))
water_drink = int(input('Какая нужна вода? \n 1 - питьевая, 2 - техническая: '))
water_points = int(input('Кол-во точек водоразбора: '))
water_type = int(input('Тип воды? \n 1 - водопроводная, 2 - из скважины: '))
print()
print('ВВЕДИТЕ РЕЗУЛЬТАТ АНАЛИЗА ВОДЫ')
pH = float(input('Водород: '))
TDS = float(input('Минерализация: '))
TDH = float(input('Жесткость: '))
Fe = float(input('Железо: '))
N = float(input('Нитраты: '))
O = float(input('Органика: '))
Mn = float(input('Марганец: '))
F = float(input('Фториды: '))
P = float(input('Сероводород: '))
S = float(input('Сульфиды: '))

# Система водоподготовки:
prefilter = ''
waterboss = []
postfilter = ''
dwm = 'Не требуется'

# Функция проверки соответствия систем:
def waterboss_check():
  if (water_points <= 4 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 10 and Fe <= 3 and N <= 10 and O <= 3 and Mn <= 0.2 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('WaterBoss 400')
  if (water_points <= 5 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 20 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('WaterBoss 700')
  if (water_points <= 5 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 20 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('WaterBoss 800')
  if (water_points <= 6 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 25 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('WaterBoss 900')
  if (water_points <= 6 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 25 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('Aquaphor 1000')
  if (water_points <= 5 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 20 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('Aquaphor Pro 180')
  if (water_points <= 7 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 28 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P <= 0.003 and S <= 0.003):
    waterboss.append('Aquaphor ProPlus 380')
  if (water_points <= 4 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 10 and Fe <= 3 and N <= 10 and O <= 3 and Mn <= 0.2 and F <= 1 and P > 0.003 and S > 0.003):
    waterboss.append('WaterBoss 400 P')
  if (water_points <= 7 and 6 <= pH <= 9 and 200 <= TDS <= 1000 and TDH <= 28 and Fe <= 10 and N <= 10 and O <= 3 and 0.2 <= Mn <= 0.5 and F <= 1 and P > 0.003 and S > 0.003):
    waterboss.append('Aquaphor ProPlus 380 P')
  else:
    pass

# Подбор оборудования:
if turbidity != 2:
  waterboss_check()
if water_drink == 1:
  dwm = 'DWM 101S Морион'
if water_type == 1:
  prefilter = 'Полипропиленовый картридж'
else:
  prefilter = 'Угольный картридж'

# Результат:
if waterboss != []:
  print(f'''
  СИСТЕМА ВОДООЧИСТКИ.
  Предфильтрация: Гросс 20 + {prefilter};
  Очистка: {' или '.join(waterboss)};
  Постфильтрация: {postfilter};
  Дополнительно: {dwm}.
  ''')
else:
  print('Не удалось подобрать оборудование под ваши показатели.')