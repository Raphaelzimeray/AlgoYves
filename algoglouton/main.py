monnaie = [1, 2, 5, 10, 20, 50]
monnaie.reverse()

def return_monnaie(to_return:int)->dict:
    returned_dict = {
        "50": 0,
        "20": 0,
        "10": 0,
        "5": 0,
        "2": 0,
        "1": 0
    }

    index = 0
    while to_return > 0:
        if monnaie[index] <= to_return:
            number_of_current_monnaie = to_return // monnaie[index]
            returned_dict[str(monnaie[index])] = number_of_current_monnaie
            to_return = to_return - (monnaie[index] * number_of_current_monnaie)
        else:
            index +=1
    return returned_dict



rendue_monnaie = return_monnaie(152)

for key, value in rendue_monnaie.items():
    print(value, "X", key)


# Problème du voleur


objets = [(60, 10), (100, 20), (200, 30)]

def steal_the_max(objects:list, max_weight:int)-> int:
    objects.sort(key= lambda x: x[0] / x[1], reverse=True)
    print(objects)
    val_max = 0
    for value, weight in objects:
        if max_weight <= 0:
            break
        number_of_objects = max_weight // weight
        print(number_of_objects, "X", value, "pesant", weight)
        val_max += number_of_objects * value
        max_weight -= number_of_objects * weight
    return val_max

max_val = steal_the_max(objets, 70)

print(max_val)
