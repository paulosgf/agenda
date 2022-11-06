#!/usr/bin/env python3

import contatos


class Agenda(contatos.Contatos):
    _dicionario = {}
    _contador: int = 1

    def __init__(self, nome, telefone, email, aniversario, Id, contador):

        super().__init__(nome, telefone, email, aniversario, Id)
        contador = self._contador
        self._dicionario[contador][nome] = nome
        self._dicionario[contador][telefone] = telefone
        self._dicionario[contador][email] = email
        self._dicionario[contador][aniversario] = aniversario
        self._dicionario[contador][Id] = Id
