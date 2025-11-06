from icecream import ic
from src.schema import LaptopList
from src.utils import chunker, throttled_list_iterator
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

import json

with open('outputs/raw_products.json', 'r') as f:
    raw_data = json.load(f)


for product in raw_data:
    product['price']= int(product['price'].split(' ')[-1].replace(',',''))
    product['combined'] =f"""
    title:= {product['product_name']};
    listed categories:= {product['product_categories']};
    description:={product['description']};
    """

chunks = chunker(raw_data, 3)

sm = SystemMessage(content="""
    You are a data entry operator incharge of classifying raw marketplace data of used laptops.
     extract the info correctly from the product title, it's listed categories and the given description:
        """)

from dotenv import load_dotenv
load_dotenv()
import os
import getpass
# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite").with_structured_output(LaptopList)

#TODO UNCHUNK THE RESPONSES
unchunked = []
for chunk in throttled_list_iterator(chunks,15,60):
    concated_message = ''.join([f"==={i+1} START===\n"+x['combined']+f"\n===END===\n" for (i,x) in enumerate(chunk)])
    hm = HumanMessage(content= concated_message)
    response = llm.invoke([sm, hm])
    ls = response.model_dump()['laptops']
    for i, c in enumerate(chunk):
        ls[i]['price'] = c['price']
        ls[i]['product_url'] = c['product_url']
        ls[i]['time_loc'] = c['time_loc']
    unchunked = unchunked + ls

with open('outputs/structured.json', 'w') as f:
    json.dump(unchunked, f)
