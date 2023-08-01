    # 1
class Man:
    fio = ""
    birthd = ""
    number = ""
    city = ""
    county = ""
    adress = ""
    def __init__(self, fio, birthd, number, city, county, adress):
        self.fio = fio
        self.birthd = birthd
        self.number = number
        self.city = city
        self.country = county
        self.adress = adress
    def __str__(self):
        return (f'ФИО: {self.fio} \n'
              f'Дата рождения: {self.birthd} \n'
              f'Номер телефона: {self.number} \n'
              f'Город: {self.city}'
              f'\nСтрана: {self.country}'
              f'\nАдрес: {self.adress} ')

manObj = Man("Иванов Иван Иванович", "16 октября 2000г", "8(999)999-99 99", "Пермь", "Россия", "ул. Пушкина")
print(manObj)

while True:
    choice = input('Хотите изменить данные? (Y/N): ')
    if choice.upper() == 'N':
        break
    elif choice.upper() == 'Y':
        print('1 - Изменить ФИО;\n'
                '2 - Изменить дату рождения;\n'
                '3 - Изменить номер телефона;\n'
                '4 - Изменить город;\n'
                '5 - Изменить страну;\n'
                '6 - Изменить адрес;\n'
                '0 - Выход.')
        value = int(input('Что необходимо изменить: '))
        if value == 0:
            break
        elif value == 1:
            fio = input('Введите ФИО: ')
            if fio:
                manObj.fio = fio
        elif value == 2:
            birthd = input('Введите дату рождения: ')
            if birthd:
                manObj.birthd = birthd
        elif value == 3:
            number = input('Введите номер телефона: ')
            if number:
                manObj.number = number
        elif value == 4:
            city = input('Введите город: ')
            if city:
                manObj.city = city
        elif value == 5:
            county = input('Введите страну: ')
            if county:
                manObj.county = county
        elif value == 6:
            adress = input('Введите адрес: ')
            if adress:
                manObj.adress = adress
        else:
            print('Введена неверная команда!!!')
        print(f'Обновленные данные о человеке: \n{manObj}')
print(f'Данные о человеке: \n{manObj}')

    # 2
class City:
    nameCity = ""
    region = ""
    country = ""
    population = 0
    index = 0
    codeCity = 0
    def __init__(self, nameCity, region, country, population, index, codeCity):
        self.nameCity = nameCity
        self.region = region
        self.country = country
        self.population = population
        self.index = index
        self.codeCity = codeCity
    def __str__(self):
        return (f'Название города: {self.nameCity} \n'
              f'Название региона: {self.region} \n'
              f'Страна: {self.country} \n'
              f'Кол-во жителей: {self.population}'
              f'\nПочтовый индекс: {self.index}'
              f'\nТелефонный код города: {self.codeCity} ')

cityObj = City("Пермь", "Пермский край", "Россия", "1000000", "614113", "8952")
print(cityObj)

while True:
    choice = input('Хотите изменить данные? (Y/N): ')
    if choice.upper() == 'N':
        break
    elif choice.upper() == 'Y':
        print('1 - Изменить название города;\n'
                '2 - Изменить название региона;\n'
                '3 - Изменить страну;\n'
                '4 - Изменить кол-во жителей;\n'
                '5 - Изменить почтовый индекс;\n'
                '6 - Изменить телефонный код;\n'
                '0 - Выход.')
        value = int(input('Что необходимо изменить: '))
        if value == 0:
            break
        elif value == 1:
            nameCity = input('Введите название города: ')
            if nameCity:
                cityObj.nameCity = nameCity
        elif value == 2:
            region = input('Введите название региона: ')
            if region:
                cityObj.region = region
        elif value == 3:
            country = input('Введите страну: ')
            if country:
                cityObj.country = country
        elif value == 4:
            population = input('Введите кол-во жителей: ')
            if population:
                cityObj.population = population
        elif value == 5:
            index = input('Введите почтовый индекс: ')
            if index:
                cityObj.index = index
        elif value == 6:
            codeCity = input('Введите телефонный код: ')
            if codeCity:
                cityObj.codeCity = codeCity
        else:
            print('Введена неверная команда!!!')
        print(f'Обновленные данные о городе: \n{cityObj}')
print(f'Данные о городе: \n{cityObj}')

    # 3
class County:
    nameCountry = ""
    continent = ""
    population = 0
    codeCountry = 0
    capital = ""
    nameCity = ""
    def __init__(self, nameCountry, continent, population, codeCountry, capital, nameCity):
        self.nameCountry = nameCountry
        self.continent = continent
        self.population = population
        self.codeCountry = codeCountry
        self.capital = capital
        self.nameCity = nameCity
    def __str__(self):
        return (f'Название страны: {self.nameCountry} \n'
              f'Название континента: {self.continent} \n'
              f'Кол-во жителей: {self.population} \n'
              f'Телефонный код страны: {self.codeCountry}'
              f'\nНазвание столицы: {self.capital}'
              f'\nНазвание городов страны: {self.nameCity} ')

countyObj = County("Россия", "Евразия", 150000000, 7, "Москва", "Самара, Тюмень, Пермь, Омск, Белогорск")
print(countyObj)

while True:
    choice = input('Хотите изменить данные? (Y/N): ')
    if choice.upper() == 'N':
        break
    elif choice.upper() == 'Y':
        print('1 - Изменить название страны;\n'
                '2 - Изменить название континента;\n'
                '3 - Изменить кол-во жителей;\n'
                '4 - Изменить телефонный код страны;\n'
                '5 - Изменить название столицы;\n'
                '6 - Изменить название городов страны;\n'
                '0 - Выход.')
        value = int(input('Что необходимо изменить: '))
        if value == 0:
            break
        elif value == 1:
            nameCountry = input('Введите название страны: ')
            if nameCountry:
                countyObj.nameCountry = nameCountry
        elif value == 2:
            continent = input('Введите название континента: ')
            if continent:
                countyObj.continent = continent
        elif value == 3:
            population = input('Введите кол-во жителей: ')
            if population:
                countyObj.population = population
        elif value == 4:
            codeCountry = input('Введите телефонный код страны: ')
            if codeCountry:
                countyObj.codeCountry = codeCountry
        elif value == 5:
            capital = input('Введите название столицы: ')
            if capital:
                countyObj.capital = capital
        elif value == 6:
            nameCity = input('Введите название городов страны: ')
            if nameCity:
                countyObj.nameCity = nameCity
        else:
            print('Введена неверная команда!!!')
        print(f'Обновленные данные о стране: \n{countyObj}')
print(f'Данные о стране: \n{countyObj}')

    # 4
class Drob:
    def __init__(self, ch, z):
        self.ch = ch
        self.z = z
    # Умножение
    def multiplication(self, ch2, z2, ch, z):
        self.ch *= ch2
        self.z *= z2
        print(f'Операция: {ch}/{z} * {ch2}/{z2} = {drobObject.ch}/{drobObject.z}')
    # Деление
    def division(self, ch2, z2, ch, z):
        self.ch *= z2
        self.z *= ch2
        print(f'Операция: {ch}/{z} / {ch2}/{z2} = {drobObject.ch}/{drobObject.z}')
    # Сложение
    def addition(self, ch2, z2, ch, z):
        self.ch = self.ch*z2+self.z*ch2
        self.z = self.z*z2
        print(f'Операция: {ch}/{z} + {ch2}/{z2} = {drobObject.ch}/{drobObject.z}')
    # Вычитание
    def subtraction(self, ch2, z2, ch, z):
        self.ch = self.ch*z2 - self.z*ch2
        self.z = self.z *z2
        print(f'Операция: ({ch}/{z}) / ({ch2}/{z2}) = {drobObject.ch}/{drobObject.z}')


ch, z = int(input("Введите числитель: ")), int(input("Введите знаменталь: "))
print(f'Ваша дробь: {ch}/{z}')
drobObject = Drob(ch, z)
print(" 1. Умножение \n 2. Деление \n 3. Сложение \n 4. Вычитание")
choice = int(input('Введит операцию для выполнения: '))
if (choice == 1):
    ch2, z2 = int(input("Введите числительно второй дроби: ")), int(input("Введите знаменатель второй дроби: "))
    drobObject.multiplication(ch2,z2, ch, z)
elif (choice == 2):
    ch2, z2 = int(input("Введите числительно второй дроби: ")), int(input("Введите знаменатель второй дроби: "))
    drobObject.division(ch2, z2, ch, z)

elif (choice == 3):
    ch2, z2 = int(input("Введите числительно второй дроби: ")), int(input("Введите знаменатель второй дроби: "))
    drobObject.addition(ch2, z2, ch, z)
elif (choice == 4):
    ch2, z2 = int(input("Введите числительно второй дроби: ")), int(input("Введите знаменатель второй дроби: "))
    drobObject.subtraction(ch2, z2, ch, z)
else:
    print('Пока')