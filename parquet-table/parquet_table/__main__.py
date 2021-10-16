from parquet_table.app import ParquetTableApp


def main():
    parquet_table_instance = ParquetTableApp()
    parquet_table_instance.app.run_server(debug=True)


if __name__ == "__main__":
    main()
