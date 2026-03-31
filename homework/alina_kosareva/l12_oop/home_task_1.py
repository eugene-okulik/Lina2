class Flowers:
    def __init__(self, name, freshness, color, stem_length, price, life_time):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_time = life_time

    def __repr__(self):
        return (
            f"\n {self.name}, {self.color}, {self.price} рубля, {self.life_time} дней"
        )


class Astra(Flowers):
    def __init__(self, name, freshness, color, stem_length, price, life_time):
        super().__init__(name, freshness, color, stem_length, price, life_time)


class Gypsophila(Flowers):
    def __init__(self, name, freshness, color, stem_length, price, life_time):
        super().__init__(name, freshness, color, stem_length, price, life_time)


class Carnation(Flowers):
    def __init__(self, name, freshness, color, stem_length, price, life_time):
        super().__init__(name, freshness, color, stem_length, price, life_time)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def get_average_lifespan(self):
        return sum(flower.life_time for flower in self.flowers) / len(self.flowers)

    def sort_freshness(self):
        return sorted(self.flowers, key=lambda x: x.freshness)

    def sort_color(self):
        return sorted(self.flowers, key=lambda x: x.color)

    def sort_stem_length(self):
        return sorted(self.flowers, key=lambda x: x.stem_length)

    def sort_price(self):
        return sorted(self.flowers, key=lambda x: x.price)

    def search_by_life_time(self, min_life_time):
        return [flower for flower in self.flowers if flower.life_time >= min_life_time]

    def total_price(self):
        return sum(flower.price for flower in self.flowers)


astra1 = Astra("астра1", "свежие", "красные", "короткий", 1.50, 14)
astra2 = Astra("астра2", "свежие", "белые", "средний", 1.20, 11)
astra3 = Astra("астра3", "несвежие", "розовые", "длинный", 2, 17)

gypsophila1 = Gypsophila("гипсофила1", "свежие", "белые", "короткий", 2, 20)
gypsophila2 = Gypsophila("гипсофила2", "несвежие", "желтые", "длинный", 1.50, 19)
gypsophila3 = Gypsophila("гипсофила3", "свежие", "фиолетовые", "длинный", 3.50, 22)

сarnation1 = Carnation("гвоздика1", "несвежие", "красные", "длинный", 5, 7)
сarnation2 = Carnation("гвоздика2", "несвежие", "розовые", "средний", 4.45, 5)
сarnation3 = Carnation("гвоздика3", "несвежие", "лиловык", "длинный", 2.50, 6)

bouquet = Bouquet([astra1, astra2, astra3, сarnation2, gypsophila3])

print(bouquet.get_average_lifespan())
print(bouquet.sort_freshness())
print(bouquet.sort_color())
print(bouquet.search_by_life_time(2))
print(bouquet.sort_price())
print(bouquet.total_price())
print(bouquet.sort_stem_length())
