#!/usr/bin/env python3

import contatos


class Agenda(contatos.Contatos):
    _contador: int = 1
    _agenda = {}

    def __init__(self, nome, telefone, email, aniversario, Id):
        super().__init__(nome, telefone, email, aniversario, Id)
        self._agenda[self._contador] = []
        self._agenda[self._contador].append(nome)
        self._agenda[self._contador].append(telefone)
        self._agenda[self._contador].append(email)
        self._agenda[self._contador].append(aniversario)
        self._agenda[self._contador].append(Id)
        self._contador += 1

    def adiciona(self, nome, telefone, email, aniversario, Id):
        self._agenda[self._contador] = []
        self._agenda[self._contador].append(super()._set_nome(nome))
        self._agenda[self._contador].append(super()._set_telefone(telefone))
        self._agenda[self._contador].append(super()._set_email(email))
        self._agenda[self._contador].append(super()._set_aniversario(aniversario))
        self._agenda[self._contador].append(super()._set_id(Id))
        self._contador += 1

    def remove(self):
        pass

    def busca(self):
        pass

    def exibe(self, entrada):
        return self._agenda[entrada]
