from parquet_table.app import app


def main():
    app.run_server(debug=False)


if __name__ == "__main__":
    main()
