#!/usr/bin/env python3
import sys

from agenda import Agenda


def main():

    obj = Agenda()
    nome: str
    telefone: str
    email: str
    aniversario: str
    id: int
    num: int

    while True:
        escolha: int = int(
            input(
                "Escolha uma opçao:\n1 - Novo contato: \n2 - Remover contato\n3 - Buscar contato\n4 - Exibir contato\n5 -Sair: "
            )
        )

        if escolha == 1:
            nome, telefone, email, aniversario, id = input(
                "Contato separado por espaço na forma: nome, telefone, email, aniversario, ID: "
            ).split()
            obj.adiciona(nome, telefone, email, aniversario, int(id))
        elif escolha == 2:
            num = int(input("Informe o numero do contato a remover: "))
            obj.remove(num)
        elif escolha == 3:
            nome = input("Informe o nome ou telefone do contato a buscar: ")
            print(obj.busca(nome))
        elif escolha == 4:
            num = int(input("Informe o numero do contato a exibir: "))
            print(obj.exibe(num))
        else:
            print("Saindo...")
            sys.exit(0)


if __name__ == "__main__":
    main()
