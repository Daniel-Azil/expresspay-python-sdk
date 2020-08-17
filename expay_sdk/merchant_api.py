"""
Pull in packages
"""
import json
import logging
import requests
from expay_sdk.utility import config
from expay_sdk.requests import (query, submit)

"""
Internal logging
"""
log = logging.getLogger(__name__)

"""
Merchant Api
"""
class MerchantApi:
  """
  Object to contain package config
  """
  config = None
  """
  Environment to work with
  """
  env = None
  """
  Base url based on environment
  """
  base_url = None
  """
  List of allowed environments
  """
  allowed_envs = {"sandbox", "production"}
  """
  Stored class name
  """
  whoami = None
  """
  Ephemeral request storage
  """
  request = None
  """
  Merchant unique id
  """    
  merchant_id = None
  """
  Merchant api key
  """    
  merchant_key = None

  """
  Class initializer
  Args:
    - merchant_id: Unique id for merchant
    - merchant_key: Unique api key for merchant
    - environment: Environment developer is integrating on
  """
  def __init__(self, merchant_id: str, merchant_key: str, environment: str):
    self.whoami = type(self).__name__
    self.env = environment
    self.merchant_id = merchant_id
    self.merchant_key = merchant_key
    self.config = config.Config(merchant_id, merchant_key)
    # set base url and run initial checks
    self.init()
  
  """
  Class object (developer)
  """
  def __repr__(self) -> str:
    return "Merchant credentials: (%s, %s) and Merchant environment: (%s)" % (self.merchant_id, self.merchant_key, self.env)

  """
  Class object (user)
  """
  def __str__(self) -> str:
    return "Merchant ID: %s | Merchant Env: %s" % (self.merchant_id, self.env)
  
  """
  Initialize required variables
  Args:
    - self: Instance of current class
  """
  def init(self) -> int:
    if self.env not in self.allowed_envs:
      raise AttributeError("Sorry, (" + self.env + ") is not allowed, expecting (sandbox) or (production)")
    elif self.env == "sandbox":
      self.base_url = self.config.get_sandbox_url()
    elif self.env == "production":
      self.base_url = self.config.get_production_url()
    return 0
  
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
  def submit(self, currency: str, amount: float, order_id: str, order_desc: str, redirect_url: str, account_number: str, order_img_url: str = None, first_name: str = None, last_name: str = None, phone_number: str = None, email: str = None) -> dict:
    try:
      self.request = {
        "currency": currency,
        "amount": amount,
        "order_id": order_id,
        "order_desc": order_desc,
        "redirect_url": redirect_url,
        "account_number": account_number,
        "order_img_url": order_img_url,
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email
      }

      requestAccessor = submit.SubmitInvoice(self.request, self.config)
      requestData = requestAccessor.make()
      requestHeaders = {"Content-Type": "application/x-www-form-urlencoded"}
      requestUrl = self.base_url + "submit.php"

      response = requests.post(url=requestUrl, data=requestData, headers=requestHeaders)

      if response.status_code is not 200:
        raise ValueError("Response is not formatted right: " + json.dumps(response.text))
      
      return response.json()
    except Exception as e:
      log.info(e)
      raise ConnectionError("Something Bad Happened: " + e)
  
  """
  Generate checkout url
  Args:
    - token: string,
  """
  def checkout(self, token: str) -> str:
    try:
      return "%scheckout.php?token=%s" % (self.base_url, token)
    except Exception as e:
      log.info(e)
      raise ValueError("Something Bad Happened: " + e)
  
  """
  Query invoice payment status
  Args:
    - token: string
  """
  def query(self, token: str) -> dict:
    try:
      self.request = {
        "token": token
      }

      requestAccessor = query.QueryInvoice(self.request, self.config)
      requestData = requestAccessor.make()
      requestHeaders = {"Content-Type": "application/x-www-form-urlencoded"}
      requestUrl = self.base_url + "query.php"

      response = requests.post(url=requestUrl, data=requestData, headers=requestHeaders)

      if response.status_code is not 200:
        raise ValueError("Response is not formatted right: " + json.dumps(response.text))
      
      return response.json()
    except Exception as e:
      log.info(e)
      raise ConnectionError("Something Bad Happened: " + e)
