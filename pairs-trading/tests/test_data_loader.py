from src.data_loader import fetch_pair_data
def test_fetch_pair_data():
    df = fetch_pair_data("NVDA", "AMD", "2007-01-01", "2024-01-01")
    assert not df.empty, "DataFrame не должен быть пустым"
    assert list(df.columns) == ["NVDA", "AMD"]
    assert not df.isnull().values.any()