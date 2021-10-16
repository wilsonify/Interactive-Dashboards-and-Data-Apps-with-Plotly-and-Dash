from parquet_table.app import app


def main():
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
