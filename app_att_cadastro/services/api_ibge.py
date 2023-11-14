import requests


class Regioes:
    def __init__(self):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
        uf = requests.get(url=url)
        self.uf = uf.json()
        self.cidades = ''

    def pega_cidades(self, uf):
        url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios'
        cidades = requests.get(url=url)
        self.cidades = cidades.json()