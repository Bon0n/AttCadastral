import requests


def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resp = requests.get(url).json()
    return resp


if __name__ == '__main__':
    buscar_cep('13054215')
