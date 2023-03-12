#A simple Python program to test the usage of RegEx.
import re

def CpfTester(cpf):

    if bool(re.search(r'\b[0-9]{3}\.+[0-9]{3}\.+[0-9]{3}-+[0-9]{2}\b', cpf)) == True:
        return True
    else:
        return False

cpf = ""
cpfList = []

cpf = input("Write a sentence containing any CPF(Cadastro de Pessoa Física) with the dots and slashes (e.g., 123.456.789-01):")

if CpfTester(cpf):
    cpfList = re.findall(r'\b[0-9]{3}\.+[0-9]{3}\.+[0-9]{3}-+[0-9]{2}\b', cpf)
    print("The CPF is valid, and it is: " + cpfList[0])
else:
    print("The CPF is invalid.")

#NOTE: This program does NOT verify the validation of the CPF numbers, only it's structure, wich means that you can write any numbers that apply for that structure without it necessarily being a possible CPF.