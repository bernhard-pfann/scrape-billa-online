import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_product_info(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    product_names = []
    product_prices = []

    products = soup.find_all('div', class_='product--tile')

    for product in products:
        product_name = product.find('div', class_='product--title').text.strip()
        product_names.append(product_name)

        product_price = product.find('div', class_='price--default').text.strip()
        product_prices.append(product_price)

    data = {'Product': product_names, 'Price': product_prices}
    df = pd.DataFrame(data)

    return df

url = 'https://shop.billa.at/sortiment/alles-fuer-ein-reines-zuhause'
result_df = get_product_info(url)
print(result_df)
