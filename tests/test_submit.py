"""
Pull in packages
"""
import pytest
from expay_sdk.utility import config
from expay_sdk.requests import submit

"""
Init config setup
"""
config = config.Config("089237783227", "JKR91Vs1zEcuAj9LwMXQu-H3LPrDq1XCKItTKpmLY1-XsBgCnNpkDT1GER8ih9f-UTYoNINatMbreNIRavgu-89wPOnY6F7mz1lXP3LZ")

"""
Mock up request dict
"""
request = {
  "currency": "GHS",
  "amount": 20.00,
  "order_id": "78HJU789UYTR",
  "order_desc": "Buy Airtime",
  "account_number": "1234567890",
  "redirect_url": "https://www.expresspaygh.com",
  "order_img_url": "https://expresspaygh.com/images/logo.png",
  "first_name": "Jeffery",
  "last_name": "Osei",
  "phone_number": "233545512042",
  "email": "jefferyosei@expresspaygh.com"
}

"""
Init submit class
"""
submit_class = submit.SubmitInvoice(request, config)

"""
Test Object Representation
"""
def test_repr():
  _repr = repr(submit_class)
  assert _repr is not None
  assert type(_repr) is str

"""
Test String Representation
"""
def test_str():
  _str = str(submit_class)
  assert _str is not None
  assert type(_str) is str

"""
Test make request
"""
def test_make():
  maker = submit_class.make()
  assert maker is not None
  assert type(maker) is dict
  assert "merchant-id" in maker
  assert "api-key" in maker
  assert "currency" in maker and maker['currency'] == request['currency']
  assert "amount" in maker and maker['amount'] == request['amount'] and type(maker['amount']) is float
  assert "order-id" in maker and maker['order-id'] == request['order_id']
  assert "order-desc" in maker and maker['order-desc'] == request['order_desc']
  assert "accountnumber" in maker and maker['accountnumber'] == request['account_number']
  assert "redirect-url" in maker and maker['redirect-url'] == request['redirect_url']
  assert "order_img_url" in maker and maker['order_img_url'] == request['order_img_url']
  assert "firstname" in maker and maker['firstname'] == request['first_name']
  assert "lastname" in maker and maker['lastname'] == request['last_name']
  assert "phonenumber" in maker and maker['phonenumber'] == request['phone_number']
  assert "email" in maker and maker['email'] == request['email']
