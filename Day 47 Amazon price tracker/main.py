import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Shark-HP201-Antimicrobial-Protection-particles/dp/B09V1T3QMN?pf_rd_r=MWK06PNGQ0JW7342N6E2&pf_rd_t=Events&pf_rd_i=deals&pf_rd_p=d37727eb-8359-4bb9-8cdd-80840c17c300&pf_rd_s=slot-15&ref=dlx_deals_gd_dcl_img_1_753cb598_dt_sl15_00"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(_class="a-price-whole").text()
try:
    price = soup.find(name="span", class_="a-price-whole").get_text()

except AttributeError:
    try:
        price = soup.find(name="span", id="price",
                        class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").get_text()
    except AttributeError:
        price = soup.find(name="span", class_="a-price priceToPay").get_text().strip()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)