import pandas as pd

df = pd.read_csv('data.csv')

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