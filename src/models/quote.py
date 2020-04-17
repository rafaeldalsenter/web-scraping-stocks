class Quote(object):
    def __init__(self, codigo, date, value):
        self.codigo = codigo
        self.date = date
        self.value = value

    @staticmethod
    def create_for_json(obj):
        return Quote(obj['codigo'], obj['date'], obj['value'])