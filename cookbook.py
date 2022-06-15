from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    with open("recipes.txt", 'r', encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish_name = line.strip()
            count_ingr = file_obj.readline()
            list_ingr = []
            for ingr in range(int(count_ingr)):
                info_ingr = file_obj.readline().strip()
                list_i = info_ingr.split(' | ')
                dict_i = {'ingredient_name': list_i[0], 'quantity': list_i[1], 'measure': list_i[2]}
                list_ingr.append(dict_i)
            file_obj.readline()

            cook_book[dish_name] = list_ingr

    pprint(cook_book)
    result = {}
    for dish in dishes:
        for rec_dish in cook_book:
            if rec_dish == dish:
                lists_of_igr = cook_book.get(rec_dish)
                for ingr in lists_of_igr:
                    if ingr.get('ingredient_name') in result:
                        ingredient_name = ingr.get('ingredient_name')
                        res_ingr = result.get(ingredient_name)
                        res_ingr['quantity'] = int(ingr.get('quantity')) + int(res_ingr.get('quantity'))
                    else:
                        result[ingr.get('ingredient_name')] = {'measure':ingr.get('measure'),'quantity':(int(ingr.get('quantity'))*person_count)}

    return result





# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
pprint(get_shop_list_by_dishes(['Омлет','Омлет'], 1))