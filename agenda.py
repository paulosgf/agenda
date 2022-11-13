#!/usr/bin/env python3

from contatos import Contatos


class Agenda:
    _contador: int = 1
    _contato = Contatos()
    _agenda = {}

    def __init__(self):
        pass

    def adiciona(self, nome: str, telefone: str, email: str = "", aniversario: str = "", Id: int = 0):
        self._agenda[self._contador] = []
        self._contato._set_nome(nome)
        self._contato._set_telefone(telefone)
        self._contato._set_email(email)
        self._contato._set_aniversario(aniversario)
        self._contato._set_id(Id)
        self._agenda[self._contador].append(self._contato)

        if (nome == "") or (telefone == ""):
            print("Falta nome e/ou telefone!")
            exit(1)

        self._contador += 1

    def remove(self):
        pass

    def busca(self):
        pass

    def exibe(self, entrada):
        return self._contato[entrada]
