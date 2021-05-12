import requests
import argparse
from datetime import date
from time import time, sleep

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("--zipcode", help="Please give zip code.")

headers = {
    'accept': 'application/json',
    'Accept-Language': 'hi_IN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
}


def api_call(zipcode, today):
    try:
        result = requests.get(('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'), headers=headers, params={
            'pincode': zipcode,
            'date': today,
        })
        if result.status_code == 200:
            json_response = result.json()
            data = json_response['sessions']
            print(data)
            return None
    except:
        print("something went wrong pls try again")


if __name__ == "__main__":
    args = parser.parse_args()
    zipcode = args.zipcode
    today = date.today().strftime('%d-%m-%Y')
    print("Finding..... Near by Vaccine")
    # print(sleep(60 - time() % 60))
    # sleep(60 - time() % 60)
    api_call(zipcode, today)
