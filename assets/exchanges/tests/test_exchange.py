
import pytest

from exchanges import Exchange


@pytest.fixture(scope='session')
def exchange():
    return Exchange(
        'Bittrex',
        'a2cd9645fdb44078b1c18ca4581c747b',
        '83ca8a8e6a5440a5acbd26f9698c12b1'
    )


class TestExchange:

    def test_markets(self, exchange):
        keys_1 = ["market", "open", "high", "low", "close", "volume",
                  "base_volume", "time_stamp", "open_buy_orders",
                  "open_sell_orders"]
        keys_2 = exchange.markets()[0].keys()
        assert (
            all([k in keys_1 for k in keys_2]) and
            all([k in keys_2 for k in keys_1])
        )

    # def test_market_list(self, exchange):
    #     exchange.market_list()
    #     assert True is False

    # def test_market(self, exchange):
    #     exchange.market('ETH/BTC')
    #     assert True is False

    def test_assets(self, exchange):
        keys_1 = ["total", "asset", "available", "address"]
        keys_2 = exchange.assets()[0].keys()
        assert (
            all([k in keys_1 for k in keys_2]) and
            all([k in keys_2 for k in keys_1])
        )
