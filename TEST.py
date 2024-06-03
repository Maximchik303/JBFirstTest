from enum import Enum
import pandas as pd

df = pd.read_csv('data.csv')
max_price = df['price'].max()

class Menu(Enum):
    Highest_Price=1
    Average_Price=2
    How_Many_Ideal=3
    How_Many_Colors=4
    Premium_Carat_Median=5
    Carat_Avg=6
    Price_Per_Color=7
    EXIT=8

def display_menu():
    try:
      for action in Menu:
        print (f'{action.value} - {action.name}')
      return Menu(int(input("Whats your choice? ")))
    except (ValueError, KeyError):
        print("Invalid choice, please try again.")
        return display_menu()

def Highest_Price():
    max_price = df['price'].max()
    print(f"The most expensive diamond is: {max_price} money")

def Average_Price():
    average_price = df['price'].mean()
    print(f"The average price of the diamonds is: {average_price:.2f} money")

def How_Many_Ideal():
    ideal_cut_count = df[df['cut'] == 'Ideal'].shape[0]
    print(f"The number of diamonds with 'Ideal' cut is: {ideal_cut_count}")

def How_Many_Colors():
    unique_colors = df['color'].unique()
    number_of_colors = len(unique_colors)
    print(f"The number of different color options is: {number_of_colors}")
    print(f"The color options are: {unique_colors}")

def Premium_Carat_Median():
    median_carat_premium = df[df['cut'] == 'Premium']['carat'].median()
    print(f"The median carat value for diamonds with a 'Premium' cut is: {median_carat_premium}")

def Carat_Avg():
    average_carat_by_cut = df.groupby('cut')['carat'].mean()
    print("The average carat value for each type of cut is:")
    for cut, avg_carat in average_carat_by_cut.items():
        print(f"{cut}: {avg_carat} Carat average")

def Price_Per_Color():
    average_price_by_color = df.groupby('color')['price'].mean().to_dict()
    print("The average price for each type of color is:")
    for color, avg_price in average_price_by_color.items():
        print(f"{color}: {avg_price:.2f} Money")

if __name__ == "__main__":
    while True:
        user_selection = display_menu()
        if user_selection==Menu.Highest_Price:
            Highest_Price()
        if user_selection==Menu.Average_Price:
            Average_Price()
        if user_selection==Menu.How_Many_Ideal:
            How_Many_Ideal()
        if user_selection==Menu.How_Many_Colors:
            How_Many_Colors()
        if user_selection==Menu.Premium_Carat_Median:
            Premium_Carat_Median()
        if user_selection==Menu.Carat_Avg:
            Carat_Avg()
        if user_selection==Menu.Price_Per_Color:
            Price_Per_Color()
        if user_selection==Menu.EXIT:
            break