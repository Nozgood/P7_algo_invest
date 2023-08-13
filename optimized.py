import csv 
import time

CSV_PATH = "./assets/dataset2_Python_P7.csv"
STOCK_NAME_INDEX = 0
STOCK_PRICE_INDEX = 1
STOCK_INTERESTS_INDEX = 2
INVESTMENT_BUDGET = 500

def main(path: str):
    """main receive a path (as string) to a csv file to convert it into a list of dictionaries
    Execute a function to find the best combination of dictionary, print it and the time maked to find it 

    Args:
        path (str): _description_
    """
    rows = from_csv_to_rows(path)
    rows.pop(0)
    stocks = [from_row_to_stock(row) for row in rows if float(row[STOCK_PRICE_INDEX]) > 0]
    start_optimized = time.time()
    best_combination = process_best_combination(stocks, INVESTMENT_BUDGET)
    end_optimized = time.time()
    print(f"The choosen stocks are {best_combination['name']} \nFor a price of {round(best_combination['price'], 2)} € \nAnd a benefice of {round(best_combination['benefits'], 2)} € on 2 years")
    time_spend = round(end_optimized - start_optimized, 4)
    print(f"The algorithm tooks {str(time_spend)} seconds to be done")

def from_csv_to_rows(path: str):
    """Receive the path of a csv file we want to extract, returns raw rows from this file

    Args:
        path (str): the path of the file we want to treat

    Returns:
        list: a list of rows (which is a list of list)
    """
    rows = []
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

def from_row_to_stock(row: list):
    """Receive a list of rows and transform it into a dictionary to use it with keys

    Args:
        row (list): the list of rows we want to transform

    Returns:
        dict: a dictionary with the keys we chose and the values associate to it (key corresponds to the header of each colum of the csv file)
    """
    price = float(row[STOCK_PRICE_INDEX])
    interests = float(row[STOCK_INTERESTS_INDEX]) / 100
    benefits = price * interests
    return {"name": row[STOCK_NAME_INDEX], "price": price, "interests": interests, "benefits": benefits}

def process_best_combination(stocks_list: list, budget: int):
    """process_best_combination receive a list of stocks and a budget, sort it by "interest" and add as more as possible in a new dictionary as long as it remains budget

    Args:
        stocks_list (list): list of stocks
        budget (int): an int which represents the budget we have to invest

    Returns:
        dict: the dictionary which represents the best combination of stocks to maximize profits for the given budget
    """
    stocks_list = sorted(stocks_list, key=lambda stock: stock["interests"], reverse=True)
    final_combination = {"name": "", "price": 0, "benefits": 0}

    for stock in stocks_list:
        if stock["price"] <= budget:
            final_combination["name"] += stock["name"] + "; "
            final_combination["price"] += stock["price"]
            final_combination["benefits"] += stock["benefits"]
            budget -= stock["price"]
    return final_combination


main(CSV_PATH)
