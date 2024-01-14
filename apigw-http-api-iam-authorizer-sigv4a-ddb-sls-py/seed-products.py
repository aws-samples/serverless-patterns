import os

from dotenv import load_dotenv
import boto3

load_dotenv()

products_table = os.getenv('products_table')
default_results = os.getenv('default_results')

client = boto3.resource('dynamodb')
table = client.Table(products_table)
products = [
    {
        'code': "D0034PP",
        'name': "Product A",
        'itemPrice': "10",
        'inStockQty': "55",
        'category': ["kitchen"]
    },
    {
        'code': "A0034PX",
        'name': "Product B",
        'itemPrice': "15.99",
        'inStockQty': "12",
        'category': ["forever-stamps", "100 stamps"]
    },
    {
        'code': "C0034HG",
        'name': "Product C",
        'itemPrice': "12.33",
        'inStockQty': "44",
        'category': ["glass cups", "kitchen", "dinning"]
    },
    {
        'code': "L003KYT",
        'name': "Product D",
        'itemPrice': "75",
        'inStockQty': "12",
        'category': ["cosmetics"]
    },
    {
        'code': "LR03KPT",
        'name': "Product E",
        'itemPrice': "12.99",
        'inStockQty': "26",
        'category': ["toys", "kids", "toddler"]
    }
]

with table.batch_writer() as batch:
    for product in products:
        batch.put_item(Item=product)
