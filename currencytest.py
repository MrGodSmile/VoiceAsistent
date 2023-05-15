import requests
from bs4 import BeautifulSoup


class Currency():
    # full_page_dollar = requests.get(DOLLAR_BUN, headers=headers)
    # soup_dollar = BeautifulSoup(full_page_dollar.content, 'html.parser')
    # full_page_rub = requests.get(RUB_BUN, headers=headers)
    # soup_rub = BeautifulSoup(full_page_rub.content, 'html.parser')

    @classmethod
    def currency_soup(cls, currency_url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        full_page = requests.get(currency_url, headers=headers)
        return BeautifulSoup(full_page.content, 'html.parser')

    @classmethod
    def currency_usd(cls):
        DOLLAR_BUN = 'https://www.google.by/search?q=курс+доллара+&sxsrf=APwXEdfluDW-LRIG3J2YfnMV_D7XsxuX9A%3A1684086414892&source=hp&ei=jh5hZM-eM8aM9u8P9eyzyAk&iflsig=AOEireoAAAAAZGEsnhZVb1-dJhVLyB300sQf9lSQkzzM&ved=0ahUKEwjPnZzkrvX-AhVGhv0HHXX2DJkQ4dUDCAk&uact=5&oq=курс+доллара+&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAEIAEELEDMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEOgcIIxDqAhAnOggIABCPARDqAjoICC4QjwEQ6gI6CwgAEIoFELEDEIMBOg4ILhCKBRCxAxCDARDUAjoOCAAQgAQQsQMQgwEQyQM6DggAEIAEELEDEIMBEJIDUMcJWJYyYOQ9aAJwAHgAgAGsAYgBzAqSAQQxMi4ymAEAoAEBsAEK&sclient=gws-wiz'
        convert = Currency.currency_soup(DOLLAR_BUN).findAll("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
        return convert[0].text

    @classmethod
    def currency_rub(cls):
        RUB_BUN = 'https://www.google.by/search?q=курс+рубля&sxsrf=APwXEdfg26YNygnwvIva9NmX64eKvpkdQQ%3A1684148019264&source=hp&ei=Mw9iZMzvDIaF9u8P5PSPsAE&iflsig=AOEireoAAAAAZGIdQ4ZxDKL8tZppf6yFKlHHnxgzK_Di&oq=курс+&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQigUQJzIHCCMQigUQJzIHCCMQigUQJzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQ6BwgjEOoCECc6CwgAEIoFELEDEIMBOg4ILhCABBCxAxCDARDUAjoFCC4QgAQ6CAguEIAEENQCOggILhDUAhCABDoKCAAQgAQQyQMQCjoICAAQigUQkgM6CAgAEIAEELEDOg4IABCABBCxAxCDARDJAzoOCAAQgAQQsQMQgwEQkgNQb1iZDGDBFWgBcAB4AYABwgGIAZwFkgEDNi4xmAEAoAEBsAEK&sclient=gws-wiz'
        convert = Currency.currency_soup(RUB_BUN).findAll("span", {"class": "DFlfde SwHCTb", "data-precision": 3})
        return convert[0].text


choiceUSD = ['к доллару', 'доллару', 'давай доллару']
choiceRUB = ['к рублю', 'рублю', 'к российскому рублю']
print("К какой валюте хотите узнать курс? (к доллару или к российскому рублю?)")
choice = input()

с = Currency()
print()

for i in choiceRUB:
    if i == choice:
        print(f"1 российский рубль = {с.currency_rub()}")
    else:
        print("не понял")


for i in choiceUSD:
    if i == choice:
        print(f"1 доллар = {с.currency_usd()}")
    else:
        print("не понял")
