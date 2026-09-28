from pathlib import Path

from ledger.config import load_config

CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"


def test_load_config_returns_dict():
    cfg = load_config(CONFIG_PATH)
    assert isinstance(cfg, dict)


def test_load_config_has_moneda():
    cfg = load_config(CONFIG_PATH)
    assert cfg["moneda"] == "USD"


def test_load_config_has_limite_diario():
    cfg = load_config(CONFIG_PATH)
    assert cfg["limite_diario"] == 1000
