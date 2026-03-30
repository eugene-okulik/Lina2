class Book:
    page_material = "бумага"
    text_presence = True

    def __init__(
        self,
        book_title,
        author,
        number_pages,
        isbn=None,
        reserved_flag=False,
    ):
        self.book_title = book_title
        self.author = author
        self.number_pages = number_pages
        self.page_material = Book.page_material
        self.text_presence = Book.text_presence
        self.isbn = isbn
        self.reserved_flag = reserved_flag

    def description(self):
        if self.reserved_flag:
            description = f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_pages},материал:  {self.page_material}, зарезервирована"
            print(description)
        else:
            description = f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_pages},материал:  {self.page_material}, незарезервирована"
            print(description)


book1 = Book("Идиот", "Достоевский", 500, reserved_flag=True)
book2 = Book(
    "Мастер и Маргарита", "Булгаков", 480, reserved_flag=False
)  # можем передавать в открытую
book3 = Book(
    "Преступление и наказание", "Достоевский", 430
)  # можем не передавать значение по дефолту будет false
book4 = Book("Война и мир", "Толстой", 900, reserved_flag=False)
book5 = Book("Герой нашего времени", "Лермонтов", 250)

book1.description()
book2.description()
book3.description()
book4.description()
book5.description()


class SchoolTextbooks(Book):
    def __init__(
        self,
        book_title,
        author,
        number_pages,
        subject,
        school_class,
        tasks=False,
        isbn=None,
        reserved_flag=False,
    ):
        super().__init__(
            book_title,
            author,
            number_pages,
            isbn,
            reserved_flag,
        )
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def description(self):
        if self.tasks:
            description = f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_pages}, предмет: {self.subject}, класс: {self.school_class}, зарезервирована"
            print(description)
        else:
            description = f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_pages}, предмет: {self.subject}, класс: {self.school_class}"
            print(description)


textbook1 = SchoolTextbooks("Алгебра", "Иванов", 200, "Математика", 9, tasks=True)
textbook2 = SchoolTextbooks(
    "История мира", "Петров", 180, "История", 8, tasks=False
)  # можем передавать в открытую
textbook3 = SchoolTextbooks(
    "География", "Иванов", 220, "География", 7
)  # можем не передавать значение по дефолту будет false
textbook4 = SchoolTextbooks("Физика", "Сидоров", 210, "Физика", 10, tasks=False)
textbook5 = SchoolTextbooks("Биология", "Смирнова", 190, "Биология", 6)

textbook1.description()
textbook2.description()
textbook3.description()
textbook4.description()
textbook5.description()
