#!/usr/bin/env python3

from contatos import Contatos


class Agenda:
    def __init__(self):
        self._contador: int = 1
        self._agenda = {}

    def adiciona(
        self,
        nome: str,
        telefone: str,
        email: str = "",
        aniversario: str = "",
        Id: int = 0,
    ):
        self._contato = Contatos()
        self._contato._set_nome(nome)
        self._contato._set_telefone(telefone)
        self._contato._set_email(email)
        self._contato._set_aniversario(aniversario)
        self._contato._set_id(Id)

        if (
            (nome == "")
            or (type(nome) != str)
            or (telefone == "")
            or (type(telefone) != str)
        ):
            print("Falta nome e/ou telefone, ou formato incorreto!")
        elif (type(email) != str) or (type(aniversario) != str) or (type(Id) != int):
            print("Email, aniversario ou Id: Formato incorreto!")
        else:
            self._agenda[self._contador] = self._contato
            self._contador += 1
            print("Contato adicionado!")

    def remove(self, entrada):
        del self._agenda[entrada]
        print("contato excluido!")

    def busca(self, padrao):
        try:
            resposta = next(
                item
                for item in self._agenda
                if (self._agenda[item]._get_nome() == padrao)
                or (self._agenda[item]._get_telefone() == padrao)
            )
            return [
                self._agenda[resposta]._get_nome(),
                self._agenda[resposta]._get_telefone(),
                self._agenda[resposta]._get_email(),
                self._agenda[resposta]._get_aniversario(),
                self._agenda[resposta]._get_id(),
            ]
        except StopIteration:
            print("Nome nao encontrado!")

    def exibe(self, entrada):
        return [
            self._agenda[entrada]._get_nome(),
            self._agenda[entrada]._get_telefone(),
            self._agenda[entrada]._get_email(),
            self._agenda[entrada]._get_aniversario(),
            self._agenda[entrada]._get_id(),
        ]
