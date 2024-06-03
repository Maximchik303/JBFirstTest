from enum import Enum
import pandas as pd
from Helper import Average_Price,Carat_Avg,Highest_Price,How_Many_Colors,How_Many_Ideal,Premium_Carat_Median,Price_Per_Color

df = pd.read_csv('data.csv')

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