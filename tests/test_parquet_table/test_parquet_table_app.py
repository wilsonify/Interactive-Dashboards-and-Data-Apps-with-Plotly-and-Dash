from parquet_table.app import path_to_this_file, path_to_this_folder, path_to_data


def test_smoke():
    pass


def test_path_to_this_file():
    assert path_to_this_file == "/home/thom/repos/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash/parquet-table/parquet_table/app.py"
    assert path_to_this_folder == "/home/thom/repos/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash/parquet-table/parquet_table"
    assert path_to_data == "/home/thom/repos/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash/parquet-table/data"