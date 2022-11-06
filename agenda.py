#!/usr/bin/env python3

import contatos


class Agenda(contatos.Contatos):
    dicionario = {}
    _contador: int = 1

    def __init__(self, nome, telefone, email, aniversario, Id, contador):

        super().__init__(nome, telefone, email, aniversario, Id)
        contador = self._contador
        self.dicionario[contador][nome] = nome
        self.dicionario[contador][telefone] = telefone
        self.dicionario[contador][email] = email
        self.dicionario[contador][aniversario] = aniversario
        self.dicionario[contador][Id] = Id
