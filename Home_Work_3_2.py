import random
def get_numbers_ticket(min, max, quantity):
    list_numbers = []
    for number in range(int(min),int(max)):
        list_numbers.append(number)
    random_list = sorted(random.sample(list_numbers,int(quantity)))
    return f"Ваші лотарейні числа : {random_list}"
print(get_numbers_ticket("1",1000,6))