import pytest
from app import main


def test_sell_with_float(monkeypatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.20)
    assert main.cryptocurrency_action(1.50) == "Buy more cryptocurrency"


def test_buy_with_int(monkeypatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1)
    assert main.cryptocurrency_action(0.8) == "Sell all your cryptocurrency"


def test_do_nothing(monkeypatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.25)
    assert main.cryptocurrency_action(1.25) == "Do nothing"
