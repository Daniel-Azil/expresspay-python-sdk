<p align="center">
  <img src="https://expresspaygh.com/images/logo.png" />
</p>
<br/>

# Expresspay Python SDK

A simple library for Python integrators

------------------

# Install

* Install python3 and pip for your environment - [Python](https://www.python.org/downloads/) and [Pip](https://pypi.org/project/pip/#description)
* Import package via pip using the command below
```php
pip install expresspay-python-sdk
```

-------------------

# Demo / Test

* Browser Demo: [https://github.com/expresspaygh/exp-demos/tree/master/exp-python-sdk-demo]
* Unit Test: 
  - Install [Pytest](https://docs.pytest.org/en/stable/getting-started.html)
  - Run `pytest` in the root of this project

-------------------

# How to use

## Allowed Environments

* Sandbox - "sandbox"
* Production - "production"

-------------------

## Submit request

This request creates a new invoice to process a payment, below you will find an example request and response.

```python
from expay_sdk import merchant_api

"""
Init import classes
Args:
  - merchant_id = Your expressPay merchant id
  - merchant_key = Your expressPay merchant api key
  - environment = Your preferred environment, allowed params ('sandbox' or 'production')
"""
merchant_api_class = merchant_api.MerchantApi(merchant_id, merchant_key, environment)

"""
Submit new invoice
Args:
  - currency: string,
  - amount: float,
  - order_id: string,
  - order_desc: string,
  - redirect_url: string,
  - account_number: string,
  - order_img_url: string or None,
  - first_name: string or None,
  - last_name: string or None,
  - phone_number: string or None,
  - email: string or None,
"""
merchant_submit = merchant_api_class.submit(
  currency="GHS",
  amount=20.00,
  order_id="78HJU789UYTR",
  order_desc="Buy Airtime",
  redirect_url="https://www.expresspaygh.com",
  account_number="1234567890",
  order_img_url="https://expresspaygh.com/images/logo.png",
  first_name="Jeffery",
  last_name="Osei",
  phone_number="233545512042",
  email="jefferyosei@expresspaygh.com"
)

print("----------------------------------------")
print("MERCHANT SUBMIT:\n")
print(merchant_submit)
print("----------------------------------------")
print("\n")

```

```
----------------------------------------
MERCHANT SUBMIT:

{'status': 1, 'order-id': '78HJU789UYTR', 'guest-checkout': 'TRUE', 'merchantservice-name': 'TEST', 'merchantservice-srvrtid': '089237783227', 'message': 'Success', 'token': '43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte', 'redirect-url': 'https://www.expresspaygh.com', 'user-key': None, 'merchant-name': 'TEST', 'merchant-mcc': '5411', $merchant-city': 'Accra', 'merchant-countrycode': 'GH'}
----------------------------------------
```

--------------------

## Checkout request

This request creates a checkout url for a customer to make payment on expressPay, below you will find an example request and response.


```python
from expay_sdk import merchant_api

"""
Init import classes
Args:
  - merchant_id = Your expressPay merchant id
  - merchant_key = Your expressPay merchant api key
  - environment = Your preferred environment, allowed params ('sandbox' or 'production')
"""
merchant_api_class = merchant_api.MerchantApi(merchant_id, merchant_key, environment)

"""
Token returned from your "Submit" request
"""
_token = "43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte"

"""
Get checkout url
Args:
  - token: string,
"""
merchant_checkout = merchant_api_class.checkout(_token)

print("----------------------------------------")
print("MERCHANT CHECKOUT:\n")
print(merchant_checkout)
print("----------------------------------------")
print("\n")

```
```
----------------------------------------
MERCHANT CHECKOUT: (The checkout url is based on your selected environment)

https://sandbox.expresspaygh.com/api/checkout.php?token=43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte
----------------------------------------
```

-------------------

## Query request - Before payment

This request checks the payment status for an invoice on expressPay, below you will find an example request and response for 
an unpaid invoice.

```python
from expay_sdk import merchant_api

"""
Init import classes
Args:
  - merchant_id = Your expressPay merchant id
  - merchant_key = Your expressPay merchant api key
  - environment = Your preferred environment, allowed params ('sandbox' or 'production')
"""
merchant_api_class = merchant_api.MerchantApi(merchant_id, merchant_key, environment)

"""
Token returned from your "Submit" request
"""
_token = "43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte"

"""
Query invoice payment status
Args:
  - token: string
"""
merchant_query = merchant_api_class.query(_token)

print("----------------------------------------")
print("MERCHANT QUERY:\n")
print(merchant_query)
print("----------------------------------------")
print("\n")
```

```
----------------------------------------
MERCHANT QUERY:

{'result': 3, 'result-text': 'No transaction data available', 'order-id': '78HJU789UYTR', 'token': '43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte', 'currency':
 'GHS', 'amount': '20.0'}
----------------------------------------
```

-------------------

## Query request - After payment

This request checks the payment status for an invoice on expressPay, below you will find an example request and response for 
a paid invoice.

```python
from expay_sdk import merchant_api

"""
Init import classes
Args:
  - merchant_id = Your expressPay merchant id
  - merchant_key = Your expressPay merchant api key
  - environment = Your preferred environment, allowed params ('sandbox' or 'production')
"""
merchant_api_class = merchant_api.MerchantApi(merchant_id, merchant_key, environment)

"""
Token returned from your "Submit" request
"""
_token = "43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte"

"""
Query invoice payment status
Args:
  - token: string
"""
merchant_query = merchant_api_class.query(_token)

print("----------------------------------------")
print("MERCHANT QUERY:\n")
print(merchant_query)
print("----------------------------------------")
print("\n")
```

```
----------------------------------------
MERCHANT QUERY:

{'result': 1, 'result-text': 'Success', 'order-id': '78HJU789UYTR', 'token': '43165f2bcf90eef856.514313495f2bcf90eef8b1.85035432516432mjhyte', 'currency': 'GHS', 'amount': '20.0', 'auth-code': '831000', 'transaction-id': '2bc92127xd0cc', 'date-processed': '2020-08-17 21:28:31', 'paid_from': '411111******1111', 'payment_type': 'XPAY_USD_GW', 'payment_reference': '831000', 'payment_option': 'VISA', 'payment_option_type': 'CARDNET', 'payment_option_type_name': 'Visa, Mastercard, Amex or Discover'}
----------------------------------------
```

----------------------

Copyright 2020, All rights reserved. Expresspay Ghana Limited [https://expresspaygh.com]
