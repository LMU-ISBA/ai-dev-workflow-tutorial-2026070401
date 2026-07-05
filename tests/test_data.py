import data

DF = data.load_data("data/sales-data.csv")


def test_load_data_row_count():
    assert len(DF) == 482


def test_total_orders():
    assert data.total_orders(DF) == 482


def test_total_sales_near_expected():
    total = data.total_sales(DF)
    assert 110_000 < total < 123_000


def test_sales_by_month_is_chronological():
    result = data.sales_by_month(DF)
    months = result["month"].tolist()
    assert months == sorted(months)
    assert len(result) == 12


def test_sales_by_category():
    result = data.sales_by_category(DF)
    assert len(result) == 5
    assert result.iloc[0]["category"] == "Electronics"
    sales = result["sales"].tolist()
    assert sales == sorted(sales, reverse=True)


def test_sales_by_region():
    result = data.sales_by_region(DF)
    assert len(result) == 4
    assert set(result["region"]) == {"North", "South", "East", "West"}
    sales = result["sales"].tolist()
    assert sales == sorted(sales, reverse=True)
