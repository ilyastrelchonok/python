
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases): # сумма всех проданных товаров
    sum = 0
    for i in purchases:
        sum += i.get("price") * i.get("quantity") # прибавляем каждую продажу у общей сумме
    return sum

def items_by_category(purchases):
    category_dict = {} # создаем пустой словарь для новых значений
    for purchase in purchases:
        category = purchase['category'] # достаем каждую категорию и сравниваем с новым словарем
        if category not in category_dict:
            category_dict[category]=[] # если нет, добавляем новый ключ с пустым значением
        if purchase['item'] not in category_dict[category]:
            category_dict[category].append(purchase['item'])# проверям есть ли пустые значения, если нет, добавляем в список
    return category_dict

def expensive_purchases(purchases, min_price):
    new_cat = []
    for purchase in purchases:
        if purchase['price']>=min_price:
            new_cat.append(purchase) # так как минимальная цена у нас 0.5, проверяем все значения, и выводим те, которые меньше 1.0
    return new_cat

def average_price_by_category(purchases):
    category_dict = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in category_dict:
            category_dict[category] = []
        if purchase['price'] not in category_dict[category]:
            category_dict[category].append(purchase['price'])# 2 функция с измененным обращением к цене
    for category in category_dict:
        category_dict[category] = sum(category_dict[category])/len(category_dict[category]) # среднее значение по каждому продукту
    return category_dict

def most_frequent_category(purchases):
    category_dict = {}
    for purchase in purchases:
        category = purchase['category']
        if category not in category_dict:
            category_dict[category] = []
        if purchase['quantity'] not in category_dict[category]:
            category_dict[category].append(purchase['quantity'])
    for category in category_dict:
        category_dict[category] = sum(category_dict[category])/len(category_dict[category]) #функция 4
    mx = 0
    mn=''
    for category in category_dict:
        if category_dict[category]>mx:
            mx=category_dict[category]
            mn=category
    return mn #расчет максимального значения и вывод категории

print('Общая выручка: ', total_revenue(purchases))
print('Товары по категориям: ', items_by_category(purchases))
print('Покупки дороже 1.0: ', expensive_purchases(purchases, 1.0))
print('Средняя цена по категориям: ', average_price_by_category(purchases))
print('Категория с наибольшим количеством проданных товаров: ', most_frequent_category(purchases))