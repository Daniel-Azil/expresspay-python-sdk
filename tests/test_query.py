"""
Pull in packages
"""
import pytest
from expay_sdk.utility import config
from expay_sdk.requests import query

"""
Init config setup
"""
config = config.Config("089237783227", "JKR91Vs1zEcuAj9LwMXQu-H3LPrDq1XCKItTKpmLY1-XsBgCnNpkDT1GER8ih9f-UTYoNINatMbreNIRavgu-89wPOnY6F7mz1lXP3LZ")

"""
Mock up request dict
"""
request = {
  "token": "JKR91Vs1zEcuAj9LwMXQu.H3LPrDq1XCKItTKpmLY1.XsBgCnNpkDT1GER8ih9f"
}

"""
Init query class
"""
query_class = query.QueryInvoice(request, config)

"""
Test Object Representation
"""
def test_repr():
  _repr = repr(query_class)
  assert _repr is not None
  assert type(_repr) is str

"""
Test String Representation
"""
def test_str():
  _str = str(query_class)
  assert _str is not None
  assert type(_str) is str

"""
Test make request
"""
def test_make():
  maker = query_class.make()
  assert maker is not None
  assert type(maker) is dict
  assert "merchant-id" in maker
  assert "api-key" in maker
  assert "token" in maker
