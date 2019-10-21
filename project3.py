# Программа рассчитывает расходы за коммунальные услуги за год.
# Пользователь вводит данные об использовании газа,
# электроэнергии, воды, отопления, вывоза мусора.

print('Рассчитаем расходы за потребление газа.')
gas = input('У вас газовая плита? ')

if gas == 'да':
    name_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
                  'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    gaz_price = int(input('Введите цену за 1 кубометр газа: '))
    annual_gas_consumption = 0
    for month in range(12):
        print('Введите свой расход газа в кубометрах за', name_month[month], end=': ')
        gas_consumption = int(input())
        # Рассчитываем количество использованного газа за год.
        annual_gas_consumption += gas_consumption

    # Рассчитываем цену использованного газа за год.
    annual_gas = annual_gas_consumption * gaz_price
    print('Расходы за потребление газа за год:', annual_gas)
elif gas == 'нет':
    print()
    print('Тогда эти расходы входят в стоимость электроэнергии.')
print()

print('Рассчитаем расходы за потребление электроэнергии.')
name_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
              'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
electric_price = int(input('Введите цену за 1 киловатт-час электроэнергии: '))
annual_electric_consumption = 0

for month in range(12):
    print('Введите свой расход электроэнергии в киловатт-час за',
          name_month[month], end=': ')
    electric_consumption = int(input())
    # Рассчитываем количество использованной
    # электроэнергии за год.
    annual_electric_consumption += electric_consumption

# Рассчитываем цену использованной электроэнергии за год.
electric_annual_price = annual_electric_consumption * electric_price
print('Расходы за потребление электроэнергии за год:', electric_annual_price)
print()

print('Рассчитаем рассходы за вывоз мусора.')
# Стоимость вывоза мусора зависит от количества человек,
# проживающих в квартире.
people_number = int(input('Сколько человек живет в квартире? '))
garbage_price_month = int(input('Сколько стоит вывоз мусора? '))
month = 12
# Рассчитываем стоимость вывоза мусора за год.
garbage_annual_price = people_number * month * garbage_price_month
print('Расход за вывоз мусора за год:', garbage_annual_price)
print()

print('Рассчитаем рассходы за использованную воду.')
name_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
              'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
water_price = int(input('Введите цену за кубометр воды: '))
annual_water_consumption = 0

for month in range(12):
    print('Введите свой расход кубометров воды за', name_month[month], end=': ')
    water_consumption = int(input())
    # Рассчитываем количество использованной воды за год.
    annual_water_consumption += water_consumption

# Рассчитываем цену использованной воды за год.
water_annual_price = annual_water_consumption * water_price
print('Расходы за потребление воды за год:', water_annual_price)
print()

print('Рассчитаем рассходы на отопление.')
# Учитывается только в период отопительного сезона.
heating_season = input('Сейчас отопительный сезон? ')

if heating_season == 'да':
    heating_month = int(input('Сколько месяцев длится отопительный сезон? '))
    heating_price = int(input('Введите цену за 1 гигакалорий теплоэнергии: '))
    # Рассчитываем расход за отопление за сезон.
    annual_heating_consumption = heating_month * heating_price
    print('Расход за отопление за сезон', annual_heating_consumption)
elif heating_season == 'нет' and gas == 'нет':
    # Рассчитываем общий расход за коммунальные услуги за год.
    public_service = electric_annual_price + garbage_annual_price + water_annual_price
    print()
    print('Общий расход за коммунальные услуги за год:', public_service)
elif heating_season == 'нет' and gas == 'да':
    # Рассчитываем общий расход за коммунальные услуги за год.
    public_service = annual_gas + electric_annual_price + garbage_annual_price\
                     + water_annual_price
    print()
    print('Общий расход за коммунальные услуги за год:', public_service)

if gas == 'да' and heating_season == 'да':
    # Рассчитываем общий расход за коммунальные услуги за год.
    public_service = annual_gas + electric_annual_price + garbage_annual_price \
                     + water_annual_price + annual_heating_consumption
    print()
    print('Общий расход за коммунальные услуги за год:', public_service)
elif gas == 'нет' and heating_season == 'да':
    # Рассчитываем общий расход за коммунальные услуги за год.
    public_service = electric_annual_price + garbage_annual_price \
                     + water_annual_price + annual_heating_consumption
    print()
    print('Общий расход за коммунальные услуги за год:', public_service)