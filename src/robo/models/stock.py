class Stock(object):
    def __init__(self, codigo, url):
        self.codigo = codigo
        self.url = url

    @staticmethod
    def create_for_json(obj):
        return Stock(obj['codigo'], obj['url'])

    @staticmethod
    def create_for_list_json(dict):
        result = []

        for obj in dict:
            result.append(Stock(obj['codigo'], obj['url']))

        return result