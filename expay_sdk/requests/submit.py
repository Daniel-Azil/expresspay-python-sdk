"""
Pull in packages
"""
import json
import inspect
import logging
from expay_sdk.utility import config

"""
Internal logging
"""
log = logging.getLogger(__name__)

"""
Submit invoice
"""
class SubmitInvoice:
  """
  Object containing request variables
  """
  request = None
  """
  Object containing formatted class output
  """
  params = {}
  """
  Reference to config class
  """
  config = None
  """
  Stored class name
  """
  whoami = None

  """
  Class initializer
  Args:
    - request: dictionary
    - config: instance of Config class dict
  """
  def __init__(self, request: dict, config: dict):
    self.config = config
    self.request = request
    self.whoami = type(self).__name__
  
  """
  Class object (developer)
  Args:
    - self: instance of itself
  """
  def __repr__(self) -> str:
    return "Submit Request: (%s)" % (json.dumps(self.request))

  """
  Class object (user)
  Args:
    - self: instance of itself
  """
  def __str__(self) -> str:
    return "Submit Request: %s" % (json.dumps(self.request))
  
  """
  Validate and create new request object
  Args:
    - self: instance of itself
  """
  def make(self) -> dict:
    if inspect.isclass(self.config) is not True and not self.request:
      log.info("Config not found: %s" % self.whoami)
      raise KeyError("Sorry, config cannot be empty")
    elif not self.request:
      log.info("Request not found: %s" % self.whoami)
      raise KeyError("Sorry, request cannot be empty")
    else:
      try:
        self.params.update({
          "merchant-id": self.config.get_merchant_id(),
          "api-key": self.config.get_merchant_key(),
          "currency": self.request.get("currency"),
          "amount": self.request.get("amount"),
          "order-id": self.request.get("order_id"),
          "order-desc": self.request.get("order_desc"),
          "accountnumber": self.request.get("account_number"),
          "redirect-url": self.request.get("redirect_url"),
          "order_img_url": self.request.get("order_img_url") if self.request.get("order_img_url") is not None else None,
          "firstname": self.request.get("first_name") if self.request.get("first_name") is not None else None,
          "lastname": self.request.get("last_name") if self.request.get("last_name") is not None else None,
          "phonenumber": self.request.get("phone_number") if self.request.get("phone_number") is not None else None,
          "email": self.request.get("email") if self.request.get("email") is not None else None
        })
      except Exception as e:
        log.info("Value error: %s" % self.whoami)
        raise ValueError(e)
    return self.params
