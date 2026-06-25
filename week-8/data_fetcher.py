import os
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Puudub SUPABASE_URL või SUPABASE_KEY .env failis.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def fetch_all_rows(table_name: str, batch_size: int = 1000) -> pd.DataFrame:
    """
    Pärib Supabase tabelist kõik read pagination'iga.
    """
    try:
        all_rows = []
        start = 0

        while True:
            end = start + batch_size - 1
            print(f"Loen {table_name}: read {start}-{end}")

            response = (
                supabase.table(table_name)
                .select("*")
                .range(start, end)
                .execute()
            )

            rows = response.data

            if not rows:
                break

            all_rows.extend(rows)

            if len(rows) < batch_size:
                break

            start += batch_size

        return pd.DataFrame(all_rows)

    except Exception as e:
        print(f"Viga tabeli '{table_name}' pärimisel: {e}")
        return pd.DataFrame()


def fetch_sales(start_date: str, end_date: str, batch_size: int = 1000) -> pd.DataFrame:
    """
    Pärib müügiandmed tabelist sales kuupäevavahemiku järgi.
    """
    try:
        all_rows = []
        start = 0

        while True:
            end = start + batch_size - 1
            print(f"Loen sales: read {start}-{end}")

            response = (
                supabase.table("sales")
                .select("*")
                .gte("sale_date", start_date)
                .lte("sale_date", end_date)
                .range(start, end)
                .execute()
            )

            rows = response.data

            if not rows:
                break

            all_rows.extend(rows)

            if len(rows) < batch_size:
                break

            start += batch_size

        return pd.DataFrame(all_rows)

    except Exception as e:
        print(f"Viga müügiandmete pärimisel: {e}")
        return pd.DataFrame()


def fetch_customers() -> pd.DataFrame:
    """
    Pärib kliendiandmed tabelist customers.
    """
    try:
        return fetch_all_rows("customers")
    except Exception as e:
        print(f"Viga kliendiandmete pärimisel: {e}")
        return pd.DataFrame()


def fetch_products() -> pd.DataFrame:
    """
    Pärib tooteandmed tabelist products.
    """
    try:
        return fetch_all_rows("products")
    except Exception as e:
        print(f"Viga tooteandmete pärimisel: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    sales_df = fetch_sales("2024-01-01", "2024-12-31")
    customers_df = fetch_customers()
    products_df = fetch_products()

    print("\nSALES")
    print(f"Ridu: {len(sales_df)}")
    print(sales_df.head())

    print("\nCUSTOMERS")
    print(f"Ridu: {len(customers_df)}")
    print(customers_df.head())

    print("\nPRODUCTS")
    print(f"Ridu: {len(products_df)}")
    print(products_df.head())