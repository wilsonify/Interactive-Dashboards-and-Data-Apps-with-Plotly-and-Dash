import os

from parquet_table.app import app


def main():
    app.run_server(
        host=os.getenv("HOST", "127.0.0.1"),
        port=os.getenv("PORT", "8050"),
        debug=False
    )


if __name__ == "__main__":
    main()
