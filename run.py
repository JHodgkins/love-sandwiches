import gspread
from google.oauth2.service_account import Credentials
# from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches_cli_project')


def get_sales_data():
    """
    Get sales data from user input through the terminal which must be a string of 6 numbers seperated with commas.
    While loop will be True if valid data are entered or will return False and loop will continue and request data from the user until valid inputs are provided.
    """
    while True:
        print("Please enter the sales data from the last market day.")
        print("Data should be 6 numbers seperated by commas ','")
        print("Use the example below for reference.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Please enter your sales data numbers:")
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("\nSales data logged")
            break
    return sales_data


def validate_data(values):
    """
    Validate data entered by the user
    try converts all string values to int
    ValueError will be raised if cannot convert to int or
    data entered is not 6 numbers.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as err:
        print(f"Invalid entry: {err}\nPlease re-enter your sales data again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Data passed in will be used to add data to a specified worksheet
    worksheet variable will desiginate which worksheet to update.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully!.\n")


def calculate_surplus_stock(sales_row):
    """
        Compare sales with stock and calculate the surplus for each item type.
        The surplus is defined as the sales figure subtracted from the stock:
        - Positive surplus indicates waste.
        - Negative surplus indicates, extra stock made when item was out of stock.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data


def main():
    """
    Run main programme functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_stock(sales_data)
    update_worksheet(new_surplus_data, "surplus")


print("Welcome to Love Sandwiches - Data managment tool \n")
main()
