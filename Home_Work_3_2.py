import random
def get_numbers_ticket(min, max, quantity):
    list_numbers = []
    try:
        for number in range(int(min),int(max)):
            list_numbers.append(number)
        random_list = sorted(random.sample(list_numbers,int(quantity)))
        return random_list
    except:
        return []
print(get_numbers_ticket(10,4,6))