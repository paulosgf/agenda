#!/usr/bin/env python3


class Contatos:
    def __init__(
        self,
        nome: str = "",
        telefone: str = "",
        email: str = "",
        aniversario: str = "",
        Id: int = 0,
    ):
        self._id = (Id,)
        self._nome = (nome,)
        self._telefone = (telefone,)
        self._email = (email,)
        self._aniversario = aniversario

        if (nome == "") or (telefone == ""):
            print("Falta nome e/ou telefone!")
            exit(1)

    def _set_nome(self, nome: str):
        if (nome == "") or (type(nome) != str):
            print("Nome: valor vazio ou nao string!")
            exit(1)
        self._nome: str = nome

    def _get_nome(self):
        return self._nome

    def _set_telefone(self, telefone: str):
        if (telefone == "") or (type(telefone) != str):
            print("Telefone: valor vazio ou nao string!")
            exit(1)
        self._telefone: str = telefone

    def _get_telefone(self):
        return self._telefone

    def _set_email(self, email: str):
        if type(email) != str:
            print("Email: valor nao string!")
            exit(1)
        self._email: str = email

    def _get_email(self):
        return self._email

    def _set_aniversario(self, aniversario: str):
        if type(aniversario) != str:
            print("Aniversario: valor nao string!")
            exit(1)
        self._aniversario: str = aniversario

    def _get_aniversario(self):
        return self._aniversario

    def _set_id(self, Id: int):
        if type(Id) != int:
            print("Id: valor nao inteiro!")
            exit(1)
        self._id: int = Id

    def _get_id(self):
        return self._id
