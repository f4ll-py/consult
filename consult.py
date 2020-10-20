#!usr/bin/env python3


# Imports
from requests import get
from sys import argv
from modules.ascii import ascii
from rich import print

import argparse
from os import system, name
import time


# Clear the screen
def clearTerminal():
    system('cls' if name == 'nt' else 'clear')


# Main
def main():

    clearTerminal()
    print(ascii())
    print('[bold magenta][1] - CEP\n[2] - CNPJ [/bold magenta]\n')
    user_input = input('[#] - ')

    if (user_input == '1'):
        cep_consult()
    elif (user_input == '2'):
        cnpj_consult()
    else:
        print('\n[bold red]~> Invalid option[/bold red]')
        time.sleep(2)
        main()


# CEP Consult
def cep_consult():

    separator = '[bold white]. . . . . . . . . . . . . . . . . . . [/bold white]'

    try:
        cepInput = input('[#] - CEP Number ~> ')
        cepWebsite = get(f'https://viacep.com.br/ws/{cepInput}/json/')
        cepResult = cepWebsite.json()

        print('\n')
        print(separator)
        print(f'[bold green]- CEP ~> {cepResult["cep"]} [/bold green]')
        print(f'[bold green]- State ~> {cepResult["uf"]} [/bold green]')
        print(f'[bold green]- City ~> {cepResult["localidade"]} [/bold green]')
        print(f'[bold green]- Neighborhood ~> {cepResult["bairro"]} [/bold green]')
        print(f'[bold green]- Streetname ~> {cepResult["logradouro"]} [/bold green]')
        print(separator)

    except Exception:
        print("\n[bold red]~> Invalid or non-existent CEP number[/bold red]")


# CNPJ Consult
def cnpj_consult():

    separator = '[bold white]. . . . . . . . . . . . . . . . . . . [/bold white]'

    print("\n[bold yellow]WARNING ~> The CNPJ number cannot have points or bars [/bold yellow]") # Warning message

    cnpjInput = input('[#] - CNPJ Number ~> ')
    cnpjWebsite = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpjInput}')
    cnpjResult = cnpjWebsite.json()

    try:
        if (cnpjResult["status"] == "ERROR"):
            print("\n[bold red]~> Invalid or non-existent CNPJ number[/bold red]")
        else:
            print('\n' + separator)
            print(f'[bold green]- CNPJ ~> {cnpjResult["cnpj"]} [/bold green]')
            print(f'[bold green]- Name ~> {cnpjResult["nome"]} [/bold green]')
            print(f'[bold green]- Email ~> {cnpjResult["email"]} [/bold green]')
            print(f'[bold green]- Phone ~> {cnpjResult["telefone"]} [/bold green]')
            print(f'[bold green]- CEP ~> {cnpjResult["cep"]} [/bold green]')
            print(f'[bold green]- State ~> {cnpjResult["uf"]} [/bold green]')
            print(f'[bold green]- City ~> {cnpjResult["municipio"]} [/bold green]')
            print(f'[bold green]- Streetname ~> {cnpjResult["logradouro"]} [/bold green]')
            print(f'[bold green]- Situation ~> {cnpjResult["situacao"]} [/bold green]')
            print(f'[bold green]- Capital ~> {cnpjResult["capital_social"]} [/bold green]')
            print(f'[bold green]- Legal Nature ~> {cnpjResult["natureza_juridica"]} [/bold green]')
            print(separator)

    except Exception:
        print("\n[bold red]~> Unexpected error wait some minutes. [/bold red]")


# Call main
try:
    main()
except KeyboardInterrupt:
    pass