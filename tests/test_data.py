import data

DF = data.load_data("data/sales-data.csv")


def test_load_data_row_count():
    assert len(DF) == 482


def test_total_orders():
    assert data.total_orders(DF) == 482


def test_total_sales_near_expected():
    total = data.total_sales(DF)
    assert 110_000 < total < 123_000
