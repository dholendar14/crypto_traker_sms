from twilio.rest import Client
import requests
import time

# global variables
api_key = "api_key"
time_int = 20
twilio_id = "Twilio_sid"
twilio_token = "twilio_secret"
my_number = "+16785046452"
send_number = "verified_number"

client = Client(twilio_id, twilio_token)


def get_doge_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    doge_price = response_json['data'][6]
    return doge_price['quote']['USD']['price']


def send_message(body):
    client.messages.create(
        body=body,
        from_=my_number,
        to=send_number
    )


def main():
    price_list = []

    while True:
        price = get_doge_price()
        price_list.append(price)
        print(price_list)
        if len(price_list) != 1:
            threshold = price_list[len(price_list) - 2]
            if price < threshold:
                send_message(body=f"current Doge price: {price}")
        else:
            threshold = price_list[len(price_list) - 1]
            if price < threshold:
                send_message(body=f"current Doge price: {price}")
        time.sleep(time_int)


if __name__ == '__main__':
    main()
