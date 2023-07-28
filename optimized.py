import csv 
import time

CSV_PATH = "./assets/dataset1_Python_P7.csv"
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
    stocks = [from_row_to_stock(row) for row in rows]
    start_optimized = time.time()
    chosen_stocks = compute_best_combination(INVESTMENT_BUDGET, stocks)
    end_optimized = time.time()
    best_combination = process_best_combination(chosen_stocks)
    print(f"The choosen stocks are {best_combination['name']} \nFor a price of {best_combination['price']} € \nAnd a benefice of {best_combination['benefits']} € on 2 years")
    time_spend = round(end_optimized - start_optimized, 2)
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
    price = round(float(row[STOCK_PRICE_INDEX]), 2)
    print(price)
    interests = float(row[STOCK_INTERESTS_INDEX])
    benefits = price * (interests / 100)
    if price < 0:
        return {"name":row[STOCK_NAME_INDEX], "price": 0, "benefits": 0 }
    return {"name": row[STOCK_NAME_INDEX], "price": price, "benefits": benefits}

def compute_best_combination(budget, stocks):
    number_of_stocks = len(stocks)
    stocks_combination_matrix = [[0 for _ in range(budget + 1)] for _ in range(number_of_stocks + 1)]
    choiced_stocks_matrix = [[0 for _ in range(budget + 1)] for _ in range(number_of_stocks + 1)]

    for stock_index in range(1, number_of_stocks + 1):
        stock_to_compute_index = stock_index - 1
        for budget_value in range(budget + 1):
            if stocks[stock_to_compute_index]["price"] <= budget_value:
                combination_without_new_stock = stocks_combination_matrix[stock_to_compute_index][budget_value]
                remaining_budget = budget_value - stocks[stock_to_compute_index]["price"]
                if remaining_budget >= 0:
                    combination_with_new_stock = stocks[stock_to_compute_index]["benefits"] + stocks_combination_matrix[stock_to_compute_index][remaining_budget]
                    stocks_combination_matrix[stock_index][budget_value] = max(combination_without_new_stock, combination_with_new_stock)
                    if combination_with_new_stock > combination_without_new_stock:
                        choiced_stocks_matrix[stock_index][budget_value] = 1
                else:
                    stocks_combination_matrix[stock_index][budget_value] = combination_without_new_stock
            else:
                stocks_combination_matrix[stock_index][budget_value] = stocks_combination_matrix[stock_index - 1][budget_value]

    chosen_stocks = []
    budget_value = budget
    for stock_index in range(number_of_stocks, 0, -1):
        if choiced_stocks_matrix[stock_index][budget_value]:
            chosen_stocks.append(stocks[stock_index - 1]) 
            budget_value -= stocks[stock_index - 1]["price"]

    return chosen_stocks


def process_best_combination(stocks_combination: list):
    """process_best_combination receive a list of stocks and returns a dictionary based on the sum of all the stocks in the received list

    Args:
        stocks_combination (list): list of stocks

    Returns:
        dict: the dictionary which represents the sum of all the stocks in the received list
    """
    final_combination = {"name": "", "price": 0, "benefits": 0}
    for chosen_stock in stocks_combination:
        final_combination["name"] += chosen_stock["name"] + ";"
        final_combination["price"] += chosen_stock["price"]
        final_combination["benefits"] += chosen_stock["benefits"]
    return final_combination


main(CSV_PATH)