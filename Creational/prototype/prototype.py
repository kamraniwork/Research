class Book:
    def __init__(self, title, price, contant=None):
        self.title = title
        self.price = price
        self.contant = contant if contant != None else self.fetch_content_from_db()

    def fetch_content_from_db(self):
        # contant = Book.objects.get(title=self.title).contant
        contant = "The book contatnt"
        return contant

    def clone(self):
        clone_obj = self.contant + '(cached)'
        return Book(title=self.title, price=self.price, contant=clone_obj)

    def __str__(self):
        return f"title={self.title}, price={self.price}, contant={self.contant}"


if __name__ == "__main__":
    book = Book('django two scoope', 30000)
    cloned = book.clone()
    print(book)
    print("*****************")
    print(cloned)
