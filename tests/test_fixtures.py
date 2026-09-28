from pathlib import Path

from ledger.fixtures import load_fixtures

FIXTURES_PATH = Path(__file__).parent.parent / "fixtures.yaml"


def test_load_fixtures_returns_dict():
    data = load_fixtures(FIXTURES_PATH)
    assert isinstance(data, dict)


def test_load_fixtures_tiene_dos_cuentas():
    data = load_fixtures(FIXTURES_PATH)
    assert len(data["cuentas"]) == 2
