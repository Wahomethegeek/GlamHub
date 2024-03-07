import requests
import base64
from datetime import datetime
from django.conf import settings


def initiate_stk_push(phone_number):
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    shortcode = settings.MPESA_SHORTCODE_TYPE
    lipa_na_mpesa = settings.MPESA_PASSKEY

    # Access token
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    auth = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode())
    headers = {"Authorization": f"Basic {auth.decode()}"}
    response = requests.get(url, headers=headers)
    access_token = response.json()["access_token"]

    # Online payment
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    request = {
        "BusinessShortCode": shortcode,
        "Password": base64.b64encode(
            f"{shortcode}{lipa_na_mpesa}{datetime.now().strftime('%Y%m%d%H%M%S')}".encode()).decode(),
        "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": phone_number, 
        "PartyB": shortcode,
        "PhoneNumber": phone_number,  # The one paying
        "CallBackURL": "http://127.0.0.1:8000/",
        "AccountReference": "Test",
        "TransactionDesc": "Test"

    }
    # Print the phone number
    print(f'Phone number: {phone_number}')
    print(f'Request payload: {request}')

    response = requests.post(url, json=request, headers=headers)
    return response
