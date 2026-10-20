import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Nassau Candy Analytics", page_icon="🍬", layout="wide")
st.title("🍬 Nassau Candy Distributor — Data Analytics Dashboard")
st.caption("Internship project | Factory, product, sales, and gross-profit analysis")

DATA_PATH = Path(__file__).parent / "Nassau Candy Distributor.csv"

FACTORY_MAP = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Kazookles": "The Other Factory",
}

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    return df

if not DATA_PATH.exists():
    st.error("Dataset not found. Add `Nassau Candy Distributor.csv` to the same folder as app.py before deploying.")
    st.info("Keep your original source CSV unchanged. Use a project copy if you need to clean or transform data.")
    st.stop()

try:
    df = load_data(DATA_PATH)
except Exception as exc:
    st.error(f"Could not read the CSV: {exc}")
    st.stop()

required = {"Product Name", "Sales", "Units", "Gross Profit", "Cost"}
missing = required - set(df.columns)
if missing:
    st.error("The CSV is missing expected columns: " + ", ".join(sorted(missing)))
    st.stop()

for col in ["Sales", "Units", "Gross Profit", "Cost"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

if "Factory" not in df.columns:
    df["Factory"] = df["Product Name"].map(FACTORY_MAP).fillna("Unmapped")

if "Region" in df.columns:
    region_options = ["All"] + sorted(df["Region"].dropna().astype(str).unique().tolist())
    selected_region = st.sidebar.selectbox("Region", region_options)
    if selected_region != "All":
        df = df[df["Region"].astype(str) == selected_region]

if "Division" in df.columns:
    division_options = ["All"] + sorted(df["Division"].dropna().astype(str).unique().tolist())
    selected_division = st.sidebar.selectbox("Division", division_options)
    if selected_division != "All":
        df = df[df["Division"].astype(str) == selected_division]

st.sidebar.markdown("---")
st.sidebar.caption("Figures are calculated from the filtered dataset.")

total_sales = df["Sales"].sum()
total_profit = df["Gross Profit"].sum()
total_units = df["Units"].sum()
margin = (total_profit / total_sales * 100) if total_sales else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"${total_sales:,.2f}")
c2.metric("Gross Profit", f"${total_profit:,.2f}")
c3.metric("Units Sold", f"{total_units:,.0f}")
c4.metric("Gross Margin", f"{margin:.2f}%")

st.subheader("Factory Performance")
factory = df.groupby("Factory", dropna=False).agg(
    Records=("Factory", "size"),
    Units=("Units", "sum"),
    Sales=("Sales", "sum"),
    Gross_Profit=("Gross Profit", "sum"),
).reset_index()
factory["Gross Margin (%)"] = factory.apply(
    lambda r: (r["Gross_Profit"] / r["Sales"] * 100) if r["Sales"] else 0, axis=1
)
factory = factory.sort_values("Sales", ascending=False)

left, right = st.columns(2)
with left:
    st.markdown("**Sales by factory**")
    fig, ax = plt.subplots()
    ax.bar(factory["Factory"].astype(str), factory["Sales"])
    ax.set_ylabel("Sales ($)")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
with right:
    st.markdown("**Gross profit by factory**")
    fig, ax = plt.subplots()
    ax.bar(factory["Factory"].astype(str), factory["Gross_Profit"])
    ax.set_ylabel("Gross profit ($)")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.dataframe(factory, use_container_width=True, hide_index=True)

st.subheader("Product Performance")
product = df.groupby("Product Name", dropna=False).agg(
    Units=("Units", "sum"),
    Sales=("Sales", "sum"),
    Gross_Profit=("Gross Profit", "sum"),
).reset_index().sort_values("Sales", ascending=False)
st.dataframe(product, use_container_width=True, hide_index=True)

if {"City", "State/Province"}.issubset(df.columns):
    st.subheader("Destination Summary")
    destinations = df.groupby(["City", "State/Province"], dropna=False).agg(
        Records=("Order ID", "size") if "Order ID" in df.columns else ("Sales", "size"),
        Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
    ).reset_index().sort_values("Sales", ascending=False)
    st.dataframe(destinations.head(20), use_container_width=True, hide_index=True)

st.subheader("Data Preview")
st.dataframe(df.head(100), use_container_width=True)

csv = factory.to_csv(index=False).encode("utf-8")
st.download_button("Download filtered factory summary (CSV)", data=csv,
                   file_name="factory_summary.csv", mime="text/csv")

st.markdown("---")
st.caption("Data-quality note: previously calculated order-to-ship date intervals were implausibly large (median about 1,274 days). Validate date interpretation with the data owner before using shipping-duration results.")
