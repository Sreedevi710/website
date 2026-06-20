def add_book(c, i, t, a, y): c[i] = (t, a, y)

def borrow_book(c, b, i):
    if i in c and i not in b: b.append(i)

def return_book(b, i):
    if i in b: b.remove(i)

def register_member(m, i): m.add(i)

def show_available(c, b):
    for i, d in c.items():
        if i not in b:
            print(i, d)

def main():
    catalog, borrowed_books, members = {}, [], set()

    add_book(catalog, 1, "Python", "Guido", 1991)
    add_book(catalog, 2, "Java", "Gosling", 1995)
    add_book(catalog, 3, "C++", "Stroustrup", 1985)
    add_book(catalog, 4, "DSA", "Author", 2020)

    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 101)  # duplicate
    register_member(members, 103)

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 2)

    return_book(borrowed_books, 1)

    show_available(catalog, borrowed_books)

main()
