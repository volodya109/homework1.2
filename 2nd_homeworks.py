import pprint

cook_book = {}
ingredient_dict = {}

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        recipe_name = line.strip()
        recipe_quantity = int(f.readline().strip())

        ingredients_list = []
        for i in range(recipe_quantity, 0, -1):
            ingredient_line = f.readline().strip()
            ingredient_name, quantity, measure = ingredient_line.split(' | ')
            ingredients_list.append({
                'ingredient_name': ingredient_name.strip(' '),
                'quantity': quantity.strip(' '),
                'measure': measure.strip(' ')
            })
        f.readline()

        cook_book[recipe_name] = ingredients_list

# pprint.pprint(cook_book)
# print(cook_book.keys())


def get_shop_list_by_dishes(dishes, person_count):

    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:

                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']

                if ingredient_name not in shopping_list:
                    shopping_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shopping_list[ingredient_name]['quantity'] += quantity
        else:
            print('No such dish')

    return shopping_list

pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))