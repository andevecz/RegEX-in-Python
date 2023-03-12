#A simple Python program to test the usage of RegEx.
import re

def CpfTester(cpf):

    if bool(re.search(r'\b[0-9]{3}\.+[0-9]{3}\.+[0-9]{3}-+[0-9]{2}\b', cpf)) == True:
        return True
    else:
        return False

cpf = ""
cpfList = []
i = 0

cpf = input("Write a sentence containing any CPF(Cadastro de Pessoa Física) with the dots and slashes (e.g., 123.456.789-01):")

if CpfTester(cpf):
    cpfList = re.findall(r'\b[0-9]{3}\.+[0-9]{3}\.+[0-9]{3}-+[0-9]{2}\b', cpf)
    if len(cpfList) == 1:
        print("1 valid CPF was found, and it is: " + cpfList[0])
    else:
        print(str(len(cpfList)) + " valid CPFs were found, and they are: ")
        while i < len(cpfList):
            print(cpfList[i])
            i += 1
else:
    print("No valid CPF was found.")

input("Press 'ENTER' to continue.")

#NOTE: This program does NOT verify the validation of the CPF numbers, only it's structure, wich means that you can write any numbers that apply for that structure without it necessarily being a possible CPF.