import random 

def get_numbers_ticket(min, max, quantity):
    if min >=1 and max <=1000 and min<=quantity<=max:
        populations=[]
        
        for x in range(min,max + 1):
            populations.append(x)
        while True: 
            
            lottery_numbers = random.choices(population=populations,k=quantity)
            
            if len(set(lottery_numbers)) == quantity:
                return sorted(lottery_numbers)
    else: 
        return []



print(get_numbers_ticket(1, 49, 6))


