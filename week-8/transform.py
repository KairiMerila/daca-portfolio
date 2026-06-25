import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Puhastab andmed: eemaldab duplikaadid, käsitleb NULL-e
    ja teisendab sale_date veeru datetime formaati.
    """
    try:
        df_clean = df.copy()

        df_clean = df_clean.drop_duplicates()

        if "sale_date" in df_clean.columns:
            df_clean["sale_date"] = pd.to_datetime(
                df_clean["sale_date"],
                errors="coerce"
            )

        df_clean = df_clean.dropna()

        return df_clean

    except Exception as e:
        print(f"Viga andmete puhastamisel: {e}")
        return pd.DataFrame()


def calculate_weekly_aggregates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Arvutab nädalased koondnäitajad:
    nädalane tulu, tellimuste arv ja keskmine tellimus.
    """
    try:
        df = df.copy()
        df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

        weekly = (
            df.resample("W", on="sale_date")
            .agg(
                weekly_revenue=("total_price", "sum"),
                order_count=("total_price", "count"),
                avg_order_value=("total_price", "mean")
            )
            .reset_index()
        )

        weekly["weekly_revenue"] = weekly["weekly_revenue"].round(2)
        weekly["avg_order_value"] = weekly["avg_order_value"].round(2)

        return weekly

    except Exception as e:
        print(f"Viga nädalaste koondnäitajate arvutamisel: {e}")
        return pd.DataFrame()


def calculate_kpis(df: pd.DataFrame) -> dict:
    """
    Arvutab peamised KPI-d:
    kogukäive, unikaalsed kliendid ja keskmine tellimuse väärtus.
    """
    try:
        kpis = {
            "total_revenue": float(round(df["total_price"].sum(), 2)),
            "unique_customers": int(df["customer_id"].nunique()),
            "avg_order_value": float(round(df["total_price"].mean(), 2))
        }

        return kpis

    except Exception as e:
        print(f"Viga KPI-de arvutamisel: {e}")
        return {}


def merge_datasets(
    df_sales: pd.DataFrame,
    df_customers: pd.DataFrame
) -> pd.DataFrame:
    """
    Liidab müügi- ja kliendiandmed customer_id veeru järgi.
    """
    try:
        merged = pd.merge(
            df_sales,
            df_customers,
            on="customer_id",
            how="left"
        )

        return merged

    except Exception as e:
        print(f"Viga andmestike liitmisel: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    sample_sales = pd.DataFrame({
        "sale_id": [1, 2, 2, 3],
        "customer_id": [101, 102, 102, 103],
        "sale_date": [
            "2024-01-05",
            "2024-01-06",
            "2024-01-06",
            "2024-01-15"
        ],
        "total_price": [100, 200, 200, 150]
    })

    sample_customers = pd.DataFrame({
        "customer_id": [101, 102, 103],
        "customer_name": ["Mari", "Jüri", "Kati"],
        "city": ["Tallinn", "Tartu", "Pärnu"]
    })

    clean_sales = clean_data(sample_sales)
    weekly = calculate_weekly_aggregates(clean_sales)
    kpis = calculate_kpis(clean_sales)
    merged = merge_datasets(clean_sales, sample_customers)

    print("\nPUHASTATUD ANDMED")
    print(clean_sales)

    print("\nNÄDALASED KOONDNÄITAJAD")
    print(weekly)

    print("\nKPI-D")
    print(kpis)

    print("\nLIIDETUD ANDMED")
    print(merged)