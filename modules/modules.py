from requests import get

def consultCEP(cep):
    try:
        response = get(f'https://viacep.com.br/ws/{cep}/json/')
        data = response.json()
        print('\n')
        print('\033[31m='*50, '\033[m')
        print(f'\033[34m[+] CEP: \033[31m{data["cep"]}\033[m')
        print('\033[31m='*50, '\033[m')
        print(f'\033[34m[+] State: \033[31m{data["uf"]}\033[m')
        print(f'\033[34m[+] City: \033[31m{data["localidade"]}\033[m')
        print(f'\033[34m[+] Neighborhood: \033[31m{data["bairro"]}\033[m')
        print(f'\033[34m[+] Street Name: \033[31m{data["logradouro"]}\033[m')
        print(f'\033[34m[+] IBGE Code: \033[31m{data["ibge"]}\033[m')
        print('\033[31m='*50, '\033[m\n')
    except Exception:
        print('\n\033[31m[-] Invalid/Nonexistant CEP.\033[m')
    

def consultCNPJ(cnpj):
    try:
        response = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')
        data = response.json()
        ma = data["atividade_principal"][0]
        sa = data["atividades_secundarias"][0]
        if 'message' in data:
            print('\n\033[31m[+] Invalid/Nonexistant CNPJ.\033[m')
        else:
            print('\n')
            print('\033[31m='*50, '\033[m')
            print(f'\033[34m[+] CNPJ: \033[31m{data["cnpj"]}\033[m')
            print('\033[31m='*50, '\033[m')
            print(f'\033[34m[+] Name: \033[31m{data["nome"]}\033[m')
            print(f'\033[34m[+] Main activity: \033[31m{ma["text"]}\033[m')
            print(f'\033[34m[+] Secundary activity: \033[31m{sa["text"]}\033[m')
            print(f'\033[34m[+] Registration date: \033[31m{data["abertura"]}\033[m')
            print(f'\033[34m[+] Phone: \033[31m{data["telefone"]}\033[m')
            print(f'\033[34m[+] E-mail: \033[31m{data["email"]}\033[m')
            print(f'\033[34m[+] Situation: \033[31m{data["situacao"]}\033[m')
            print(f'\033[34m[+] State: \033[31m{data["uf"]}\033[m')
            print(f'\033[34m[+] Neighborhood: \033[31m{data["bairro"]}\033[m')
            print(f'\033[34m[+] Street Name: \033[31m{data["logradouro"]}\033[m')
            print(f'\033[34m[+] Number: \033[31m{data["numero"]}\033[m')
            print(f'\033[34m[+] CEP: \033[31m{data["cep"]}\033[m')
            print(f'\033[34m[+] City: \033[31m{data["municipio"]}\033[m')
            print(f'\033[34m[+] Legal Nature: \033[31m{data["natureza_juridica"]}\033[m')
            print(f'\033[34m[+] Social Capital: \033[31m{data["capital_social"]}\033[m')
            print('\033[31m='*50, '\033[m\n')
    except Exception:
        print('\n\033[31m[-] Invalid/Nonexistant CEP.\033[m')
