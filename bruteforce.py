stock_one = {"name": "stock_one", "price": 20, "percentage": 5/100}
stock_two = {"name": "stock_two", "price": 30, "percentage": 10/100}
stock_three = {"name": "stock_three","price": 50, "percentage": 15/100}
stock_four = {"name": "stock_four","price": 70, "percentage": 20/100}
stock_five = {"name": "stock_five","price": 60, "percentage": 17/100}
stock_six = {"name": "stock_six","price": 80, "percentage": 25/100}
stock_seven = {"name": "stock_seven", "price": 22, "percentage": 7/100}
stock_eight = {"name": "stock_eight", "price": 26, "percentage": 11/100}
stock_nine = {"name": "stock_nine","price": 48, "percentage": 13/100}
stock_ten = {"name": "stock_ten", "price": 34, "percentage": 27/100}
stock_eleven = {"name": "stock_eleven", "price": 42, "percentage": 17/100}
stock_twelve = {"name": "stock_twelve", "price": 110, "percentage": 9/100}
stock_thirteen = {"name": "stock_thirteen","price": 38, "percentage": 23/100}
stock_fourteen = {"name": "stock_fourteen", "price": 14, "percentage": 1/100}
stock_fifteen = {"name": "stock_fifteen", "price": 18, "percentage": 3/100}
stock_sixteen = {"name": "stock_sixteen", "price": 8, "percentage": 8/100}
stock_seventeen = {"name": "stock_seventeen", "price": 4, "percentage": 12/100}
stock_eighteen = {"name": "stock_eighteen", "price": 10, "percentage": 14/100}
stock_nineteen = {"name": "stock_nineteen", "price": 24, "percentage": 21/100}
stock_twenty = {"name": "stock_twenty", "price": 114, "percentage": 18/100}

all_stock = [
    stock_one,
    stock_two,
    stock_three,
    stock_four,
    stock_five,
    stock_six,
    stock_seven,
    stock_eight,
    stock_nine,
    stock_ten,
    stock_eleven,
    stock_twelve,
    stock_thirteen,
    stock_fourteen,
    stock_fifteen,
    stock_sixteen,
    stock_seventeen,
    stock_eighteen,
    stock_nineteen,
    stock_twenty
]

stock_prices = []
stock_names = []
stock_benefits = []
for stock in all_stock:
    benefit_two_years = stock["price"] * stock["percentage"]
    stock["benefits_two_years"] = benefit_two_years
    stock_prices.append(stock["price"])
    stock_names.append(stock["name"])
    stock_benefits.append(stock["benefits_two_years"])

def checkStockSum(value: int) -> bool:
    if value > 500:
        return False
    return True

def sum_stock_recursive(stock_prices, all_combinations=None, combo=0):    
    for i in range (len(stock_prices)):
        if all_combinations is None:
            all_combinations = []

        new_combo = combo + stock_prices[i]
        all_combinations.append(new_combo)
        remaining_prices = stock_prices[i+1:]

        sum_stock_recursive(remaining_prices, all_combinations, new_combo)    
    return all_combinations

def name_stock_recursive(stock_names, all_combinations=None, combo=""):    
    for i in range (len(stock_names)):
        if all_combinations is None:
            all_combinations = []

        new_combo = combo + " " + stock_names[i]
        all_combinations.append(new_combo)
        remaining_names = stock_names[i+1:]

        name_stock_recursive(remaining_names, all_combinations, new_combo)    
    return all_combinations

all_prices = sum_stock_recursive(stock_prices)
all_benefits = sum_stock_recursive(stock_benefits)
all_names = name_stock_recursive(stock_names)

all_stocks_processed = []
count = 0 
for i in range (len(all_names)):
    count += 1
    if checkStockSum(all_prices[i]) is False:
        continue
    stock_processed = {"name": all_names[i], "price": all_prices[i], "benefits": all_benefits[i]}
    all_stocks_processed.append(stock_processed)

all_stocks_processed = sorted(all_stocks_processed, key= lambda combination: combination["benefits"], reverse= True)

print(count)
print(f"and the winner is : {all_stocks_processed[0]}")
