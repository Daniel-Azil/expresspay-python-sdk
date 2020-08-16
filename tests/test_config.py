"""
Pull in packages
"""
import pytest
from src.utility import config

"""
Init config setup
"""
config = config.Config("089237783227", "JKR91Vs1zEcuAj9LwMXQu-H3LPrDq1XCKItTKpmLY1-XsBgCnNpkDT1GER8ih9f-UTYoNINatMbreNIRavgu-89wPOnY6F7mz1lXP3LZ")

"""
Test Object Representation
"""
def test_repr():
  _repr = repr(config)
  assert _repr is not None
  assert type(_repr) is str

"""
Test String Representation
"""
def test_str():
  _str = str(config)
  assert _str is not None
  assert type(_str) is str

"""
Test Get Sandbox Url
"""
def test_get_sandbox_url():
  sandbox = config.get_sandbox_url()
  assert sandbox is not None
  assert type(sandbox) is str

"""
Test Get Production Url
"""
def test_get_production_url():
  production = config.get_production_url()
  assert production is not None
  assert type(production) is str

"""
Test Get Merchant ID
"""
def test_get_merchant_id():
  merchant_id = config.get_merchant_id()
  assert merchant_id is not None
  assert type(merchant_id) is str

"""
Test Get Merchant Api Key
"""
def test_get_merchant_key():
  merchant_key = config.get_merchant_key()
  assert merchant_key is not None
  assert type(merchant_key) is str
