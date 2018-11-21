# https://py.checkio.org/blog/design-patterns-part-1/


class Author:
    def __init__(self):
        self._info = None
        self._observers = set()

    def add_bookshop(self, observer):
        if not isinstance(observer, Bookshop):
            raise TypeError()
        self._observers.add(observer)

    def del_bookshop(self, observer):
        self._observers.remove(observer)

    def set_info(self, info):
        self._info = info
        self.notify(info)

    def notify(self, info):
        for observer in self._observers:
            observer.update(info)


class Bookshop:
    def __init__(self, name):
        self._name = name

    def update(self, info):
        print(self._name, 'has got the notification: ', info)


author = Author()
bookshop_1 = Bookshop("'Bookworm'")
bookshop_2 = Bookshop("'McCandall and the sons'")
author.add_bookshop(bookshop_1)
author.add_bookshop(bookshop_2)
author.set_info('New book will be available from 29.07.2018')
