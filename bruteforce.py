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

for stock in all_stock:
    benefit_two_years = stock["price"] * stock["percentage"]
    stock["benefit_two_years"] = benefit_two_years

stock_sum = 0
all_stock_names = ""
stock_benefits = 0

def checkStockSum(value) -> bool:
    if value >= 500:
        return False
    return True

for stock in all_stock:
    stock_sum = stock["price"]
    all_stock_names = stock["name"] 
    if checkStockSum(stock_sum):
        stock_benefits = stock["benefit_two_years"]
    print(f"all stocks : {all_stock_names} total price: {stock_sum} total benefits: {stock_benefits}")


    for second_stock in all_stock:
        if second_stock["name"] == stock["name"]:
            continue
        stock_sum = stock["price"] + second_stock["price"]
        all_stock_names = stock["name"] + " " +  second_stock["name"] 
        if checkStockSum(stock_sum):
            stock_benefits = stock["benefit_two_years"] + second_stock["benefit_two_years"]
        print(f"all stocks : {all_stock_names} total price: {stock_sum} total benefits: {stock_benefits}")

        for third_stock in all_stock:
            if second_stock["name"] == third_stock["name"]:
                continue
            stock_sum = stock["price"] + second_stock["price"] + third_stock["price"]
            all_stock_names = stock["name"] + " " +  second_stock["name"] + " " + third_stock["name"]
            if checkStockSum(stock_sum):
                stock_benefits = stock["benefit_two_years"] + second_stock["benefit_two_years"] + third_stock["benefit_two_years"]
            print(f"all stocks : {all_stock_names} total price: {stock_sum} total benefits: {stock_benefits}")

            for fourth_stock in all_stock:
                if third_stock["name"] == fourth_stock["name"]:
                    continue
                stock_sum = stock["price"] + second_stock["price"] + third_stock["price"] + fourth_stock["price"]
                all_stock_names = stock["name"] + " " +  second_stock["name"] + " " + third_stock["name"] + fourth_stock["name"]
                if checkStockSum(stock_sum):
                    stock_benefits = stock["benefit_two_years"] + second_stock["benefit_two_years"] + third_stock["benefit_two_years"] + fourth_stock["benefit_two_years"]
                print(f"all stocks : {all_stock_names} total price: {stock_sum} total benefits: {stock_benefits}")

                for fifth_stock in all_stock:
                    if fifth_stock["name"] == fourth_stock["name"]:
                        continue
                    stock_sum = stock["price"] + second_stock["price"] + third_stock["price"] + fourth_stock["price"] + fifth_stock["price"]
                    if checkStockSum(stock_sum) is False:
                        continue
                    all_stock_names = stock["name"] + " " +  second_stock["name"] + " " + third_stock["name"] + fourth_stock["name"] + fifth_stock["name"]
                    stock_benefits = stock["benefit_two_years"] + second_stock["benefit_two_years"] + third_stock["benefit_two_years"] + fourth_stock["benefit_two_years"] + fifth_stock["benefit_two_years"]
                    print(f"all stocks : {all_stock_names} total price: {stock_sum} total benefits: {stock_benefits}")