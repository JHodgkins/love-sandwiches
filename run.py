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
    
    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(value):
    """
    Validate data entered by the user
    try converts all string values to int
    ValueError will be raised if cannot convert to int or
    data entered is not 6 numbers.
    """
    try:
        if len(value) != 6:
            raise ValueError(f"6 numbers are required, you entered {len(value)}")
        # elif value != int:
        #     raise ValueError(f"Numbers are only allowed to be entered, you entered {value}")
    except ValueError as e:
        print(f"Error: {e}, \nPlease re-enter the sales data\n")

get_sales_data()
