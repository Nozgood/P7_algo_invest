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
    stock_three
]

for stock in all_stock:
    benefit_two_years = stock["price"] * stock["percentage"]
    stock["benefits_two_years"] = benefit_two_years

def checkStockSum(value: int) -> bool:
    if value > 500:
        return False
    return True

def stock_recursive(stock, stock_list, final_list:None):
    if final_list is None:
        final_list = []

    if len(stock_list) > 0:
        stock_to_process = stock_list.pop(0)
        if stock["name"] == stock_to_process["name"]:
            return stock_recursive(stock, stock_list, final_list)
        stock_process_price = stock["price"] + stock_to_process["price"]
        if checkStockSum(stock_process_price) is False:
            return stock_recursive(stock, stock_list, final_list)
        stock_process_name = stock["name"] + " " + stock_to_process["name"]
        stock_process_price = stock["price"] + stock_to_process["price"]
        stock_process_benefits = stock["benefits_two_years"] + stock_to_process["benefits_two_years"]
        stock_process = {
            "final_name": stock_process_name,
            "final_price": stock_process_price,
            "final_benefits": stock_process_benefits
            }
        final_list.append(stock_process)
        return stock_recursive(stock, stock_list, final_list)
    else:
        return final_list



for stock_test in all_stock:
    all_stock_copy = all_stock.copy()
    process = stock_recursive(stock_test, all_stock_copy, None)
    print(process)