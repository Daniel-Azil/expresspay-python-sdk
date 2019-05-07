import exceptions

from api import Api, default

class Expresspay():
    default_api = default()

    def submit(self, **kwargs):
        data = kwargs.get('data', None)
        if data == None:
            raise Exception('''
                Must provide data: 
                    Example: submit({})
            ''')

        response = self.default_api.post("/submit.php", data = data)
        return response

    def create_invoice(self, **kwargs):
        data = kwargs.get('data', None)
        return self.default_api.post('/invoice.php', data=data)

    def query(self, **kwargs):
        data = kwargs.get('data', None)
        return self.default_api.post('/query.php', data=data)


