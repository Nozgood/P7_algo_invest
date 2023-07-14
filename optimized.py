import csv 
import time

CSV_PATH = "./assets/dataset1_Python_P7.csv"
STOCK_NAME_INDEX = 0
STOCK_PRICE_INDEX = 1
STOCK_INTERESTS_INDEX = 2

def optimized(path: str):
    rows = from_csv_to_rows(path)
    rows.pop(0)
    stocks = []
    for row in rows:
        stocks.append(from_row_to_stock(row))
    for stock in stocks:
        if stock["price"] < 0:
            print(stock)
            print("OUUUUHOOO \n\n")
    start_optimized = time.time()
    solution = knapsack(500, stocks)
    end_optimized = time.time()
    price = 0
    benefits = 0
    all_names = ""
    for action in solution:
        price += action["price"]
        benefits += action["benefits"]
        all_names += action["name"] + ", "
    print(solution)
    print(price)
    print(benefits)
    print(all_names)
    time_spend = round(end_optimized - start_optimized, 2)
    print(f"he algorithm tooks {str(time_spend)} seconds to be done")

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
    # raw_interest = int(row[STOCK_INTERESTS_INDEX].split("%")[0])
    # interest = raw_interest / 100
    # benefits = float(row[STOCK_PRICE_INDEX]) * interest
    price = int(float(row[STOCK_PRICE_INDEX]))
    if price < 0:
        return {"name":row[STOCK_NAME_INDEX], "price": 0, "benefits": 0 }
    return {"name": row[STOCK_NAME_INDEX], "price": (int(float(row[STOCK_PRICE_INDEX]))), "benefits": float(row[STOCK_INTERESTS_INDEX])}

def knapsack(budget, stocks):
    num_stocks = len(stocks)
    value_matrix = [[0 for _ in range(budget + 1)] for _ in range(num_stocks + 1)]
    choice_matrix = [[0 for _ in range(budget + 1)] for _ in range(num_stocks + 1)]

    # Build value_matrix[][]
    for i in range(1, num_stocks + 1):
        for w in range(budget + 1):
            if stocks[i - 1]["price"] <= w:
                # If the stock can be bought
                without_i = value_matrix[i - 1][w]
                remaining_w = w - stocks[i - 1]["price"]
                if remaining_w >= 0:
                    test = i - 1
                    with_i = stocks[i - 1]["benefits"] + value_matrix[test][remaining_w]
                    value_matrix[i][w] = max(without_i, with_i)
                    # Store the choice made
                    if with_i > without_i:
                        choice_matrix[i][w] = 1
                else:
                    value_matrix[i][w] = without_i
            else:
                # If the stock cannot be bought
                value_matrix[i][w] = value_matrix[i - 1][w]

    # Retrieve the chosen stocks
    chosen_stocks = []
    w = budget
    for i in range(num_stocks, 0, -1):
        if choice_matrix[i][w]:
            chosen_stocks.append(stocks[i - 1]) 
            w -= stocks[i - 1]["price"]

    return chosen_stocks

optimized(CSV_PATH)