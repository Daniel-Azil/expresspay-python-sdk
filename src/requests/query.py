"""
Pull in packages
"""
import json
import inspect
import logging

"""
Internal logging
"""
log = logging.getLogger(__name__)

"""
Query invoice
"""
class QueryInvoice:
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
    return "Query Request: (%s)" % (json.dumps(self.request))

  """
  Class object (user)
  Args:
    - self: instance of itself
  """
  def __str__(self) -> str:
    return "Query Request: %s" % (json.dumps(self.request))
  
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
          "token": self.request.get("token")
        })
      except Exception as e:
        log.info("Value error: %s" % self.whoami)
        raise ValueError(e)
    return self.params
