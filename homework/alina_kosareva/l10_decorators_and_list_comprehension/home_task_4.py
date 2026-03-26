PRICE_LIST = """тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р"""

price_dict = {
    name: int(price[:-1])
    for name, price in (item.split() for item in PRICE_LIST.split("\n"))
}
print(price_dict)
