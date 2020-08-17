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

{'status': 1, 'order-id': '78HJU789UYTR', 'guest-checkout': 'TRUE', 'merchantservice-name': 'TEST', 'merchantservice-srvrtid': '089237783227', 'message': 'Success', 'token': '289$5f3ac84a3bf0e2.717335165f3ac84a3bf151.1979534132615f3ac84a3b', 'redirect-url': 'https://www.expresspaygh.com', 'user-key': None, 'merchant-name': 'TEST', 'merchant-mcc': '5411', $merchant-city': 'Accra', 'merchant-countrycode': 'GH'}
----------------------------------------
```
