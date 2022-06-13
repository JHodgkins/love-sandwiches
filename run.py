import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches_cli_project')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()

# print(data)


def get_sales_data():
    """
    Get sales data from user input through the terminal
    """
    print("Please enter the sales data from the last market day.")
    print("Data should be 6 numbers seperated by commas ','")
    print("Use the example below for reference.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Please enter your sales data numbers:")
    print(f"The data provided was: {data_str}")


get_sales_data()
