"""
Package config
"""
class Config:
  """
  Merchant unique id
  """    
  merchant_id = None
  """
  Merchant api key
  """    
  merchant_api_key = None
  """
  Expresspay Ghana production url
  """
  production_url = None
  """
  Expresspay Ghana sandbox url
  """
  sandbox_url = None

  """
  Class construct
  """
  def __init__(self, merchant_id: str, merchant_api_key: str):
    self.merchant_id = merchant_id
    self.merchant_api_key = merchant_api_key

    self.production_url = "https://expresspaygh.com/api/"
    self.sandbox_url = "https://sandbox.expresspaygh.com/api/"
  
  """
  Class object (developer)
  """
  def __repr__(self) -> str:
    return "Merchant credentials: (%s)" % (self.merchant_id)

  """
  Class object (user)
  """
  def __str__(self) -> str:
    return "Merchant ID: %s" % (self.merchant_id)

  """
  Get sandbox url
  """
  def get_sandbox_url(self) -> str:
    return "%s" % (self.sandbox_url)
  
  """
  Get production url
  """
  def get_production_url(self) -> str:
    return "%s" % (self.production_url)
  
  """
  Get merchant id
  """
  def get_merchant_id(self) -> str:
    return "%s" % (self.merchant_id)
  
  """
  Get merchant api key
  """
  def get_merchant_key(self) -> str:
    return "%s" % (self.merchant_api_key)
