"""
Pull in packages
"""
import pytest
from expay_sdk import merchant_api
from expay_sdk.utility import config

"""
Init keys
"""
environment = "sandbox"
merchant_id = "089237783227"
merchant_key = "JKR91Vs1zEcuAj9LwMXQu-H3LPrDq1XCKItTKpmLY1-XsBgCnNpkDT1GER8ih9f-UTYoNINatMbreNIRavgu-89wPOnY6F7mz1lXP3LZ"

"""
Init config setup
"""
config = config.Config(merchant_id, merchant_key)

"""
Init import classes
"""
merchant_api_class = merchant_api.MerchantApi(merchant_id, merchant_key, environment)

"""
Token reference for checkout and query request
"""
_token = ""

"""
Test Object Representation
"""
def test_repr():
  _repr = repr(merchant_api_class)
  assert _repr is not None
  assert type(_repr) is str

"""
Test String Representation
"""
def test_str():
  _str = str(merchant_api_class)
  assert _str is not None
  assert type(_str) is str

"""
Test init
"""
def test_init():
  assert type(merchant_api_class.allowed_envs) is set and not None
  assert merchant_api_class.base_url is not None

"""
Test submit request
"""
def test_submit():
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

  global _token
  _token = merchant_submit['token']

  assert type(merchant_submit) is dict
  assert "token" in merchant_submit
  assert merchant_submit['status'] == 1
  assert merchant_submit['message'] == "Success"
  assert merchant_submit['token'] == _token

"""
Test checkout request
"""
def test_checkout():
  merchant_checkout = merchant_api_class.checkout(_token)

  assert type(merchant_checkout) is str
  assert merchant_checkout is not None

"""
Test query request
"""
def test_query():
  merchant_query = merchant_api_class.query(_token)
  
  assert type(merchant_query) is dict
  assert merchant_query['token'] == _token
  assert type(merchant_query['result']) is int
  assert merchant_query['result'] == 3
  assert "order-id" in merchant_query
  assert "currency" in merchant_query
  assert "amount" in merchant_query
