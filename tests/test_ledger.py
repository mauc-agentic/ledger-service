from ledger.ledger import Ledger


def test_registrar_y_consultar_saldo():
    libro = Ledger()
    libro.registrar("Caja", 100)
    libro.registrar("Caja", -30)
    assert libro.saldo("Caja") == 70


def test_saldo_de_cuenta_sin_movimientos_es_cero():
    libro = Ledger()
    assert libro.saldo("Bancos") == 0
