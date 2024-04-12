# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} -> {self.next}"

num = int(input("How many numbers do you want to add?: "))

def add_value():
    head = None
    for i in range(num):
        number = int(input("Input number: "))
        new_node = Node(number)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                if current.data == number:
                    print(f"Number {number} already exists in the list. Skipping...")
                    break
                current = current.next

            else:
                if current.data == number:
                    print(f"Number {number} already exists in the list. Skipping...")
                    continue
                current.next = new_node

    return head

def delete(head, data):
    current = head
    prev = None

    while current is not None:
        if current.data == data:
            if prev is not None:
                prev.next = current.next
            else:
                head = current.next
            return head

        prev = current
        current = current.next

    return head

def is_in_list(head, value):
    current_value = head
    while current_value:
        if current_value.data == value:
            return True
        current_value = current_value.next
    return False

head = add_value()
head = delete(head, 2)
value_in_list = is_in_list(head, 3)
print(value_in_list)

current = head
print(current)





