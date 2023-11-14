import requests


class Regioes:
    def __init__(self):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
        uf = requests.get(url=url)
        self.uf = uf.json()
        self.cidades = ''

    def pegar_cidades(self, uf):
        url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios'
        cidades = requests.get(url=url)
        self.cidades = cidades.json()
        return self.cidades


if __name__ == '__main__':
    regioes = Regioes()
    cidades = regioes.pegar_cidades('sp')
    print(cidades)
