import json
with open('outputs/output.json', 'r') as f:
   urls = json.load(f)

from seleniumbase import sb_cdp

sb = sb_cdp.Chrome()
products = []
def scrape_data(url:str):
    sb.open("https://bikroy.com"+url)
    sb.solve_captcha()
    price = sb.find_element('//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[1]').text
    #print(price)
    sb.click('/html/body/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[5]/div/div[2]/div/div[2]/button', 2)
    return {
        "product_name" : sb.find_element('//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/h1').text,
        "product_url": "https://bikroy.com"+url,
        "time_loc" : sb.find_element('//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div/span/div/div[1]').text,
        "product_categories" : sb.find_element('//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[2]').text,
        "description" : sb.find_element('//*[@id="app-wrapper"]/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div[5]/div/div[2]').text,
        "price": price
    }

for url in urls[0:20]:
    try:
        products.append(scrape_data(url))
    except:
        pass

with open('outputs/raw_products.json', 'w') as f:
    json.dump(products, f, ensure_ascii=False)
