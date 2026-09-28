"""Un libro contable mínimo en memoria."""

from collections import defaultdict


class Ledger:
    def __init__(self):
        self._saldos = defaultdict(int)

    def registrar(self, cuenta, monto):
        self._saldos[cuenta] += monto

    def saldo(self, cuenta):
        return self._saldos[cuenta]
