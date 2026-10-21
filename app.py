import io
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="NC Distributors Insights", page_icon="🍬", layout="wide")
st.title("🍬 NC Distributors Insights")
st.caption("Factory-to-customer route analytics • Sales • Shipping intervals • Data quality")

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

FACTORY_COORDS = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.11914, -96.18115),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.1175, -89.971107),
}

# Approximate state centroids for visualization only; not customer-level coordinates.
STATE_COORDS = {
    "Alabama": (32.806671, -86.791130), "Alaska": (61.370716, -152.404419),
    "Arizona": (33.729759, -111.431221), "Arkansas": (34.969704, -92.373123),
    "California": (36.116203, -119.681564), "Colorado": (39.059811, -105.311104),
    "Connecticut": (41.597782, -72.755371), "Delaware": (39.318523, -75.507141),
    "Florida": (27.766279, -81.686783), "Georgia": (33.040619, -83.643074),
    "Hawaii": (21.094318, -157.498337), "Idaho": (44.240459, -114.478828),
    "Illinois": (40.349457, -88.986137), "Indiana": (39.849426, -86.258278),
    "Iowa": (42.011539, -93.210526), "Kansas": (38.526600, -96.726486),
    "Kentucky": (37.668140, -84.670067), "Louisiana": (31.169546, -91.867805),
    "Maine": (44.693947, -69.381927), "Maryland": (39.063946, -76.802101),
    "Massachusetts": (42.230171, -71.530106), "Michigan": (43.326618, -84.536095),
    "Minnesota": (45.694454, -93.900192), "Mississippi": (32.741646, -89.678696),
    "Missouri": (38.456085, -92.288368), "Montana": (46.921925, -110.454353),
    "Nebraska": (41.125370, -98.268082), "Nevada": (38.313515, -117.055374),
    "New Hampshire": (43.452492, -71.563896), "New Jersey": (40.298904, -74.521011),
    "New Mexico": (34.840515, -106.248482), "New York": (42.165726, -74.948051),
    "North Carolina": (35.630066, -79.806419), "North Dakota": (47.528912, -99.784012),
    "Ohio": (40.388783, -82.764915), "Oklahoma": (35.565342, -96.928917),
    "Oregon": (44.572021, -122.070938), "Pennsylvania": (40.590752, -77.209755),
    "Rhode Island": (41.680893, -71.511780), "South Carolina": (33.856892, -80.945007),
    "South Dakota": (44.299782, -99.438828), "Tennessee": (35.747845, -86.692345),
    "Texas": (31.054487, -97.563461), "Utah": (40.150032, -111.862434),
    "Vermont": (44.045876, -72.710686), "Virginia": (37.769337, -78.169968),
    "Washington": (47.400902, -121.490494), "West Virginia": (38.491226, -80.954453),
    "Wisconsin": (44.268543, -89.616508), "Wyoming": (42.755966, -107.302490),
    "District of Columbia": (38.9072, -77.0369),
}
STATE_ABBR = {
    "AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado",
    "CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia","HI":"Hawaii","ID":"Idaho",
    "IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana",
    "ME":"Maine","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi",
    "MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey",
    "NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma",
    "OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota",
    "TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington",
    "WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming","DC":"District of Columbia"
}

@st.cache_data(show_spinner="Loading and validating dataset...")
def load_data(path_string, modified_time):
    data = pd.read_csv(path_string)
    data.columns = [str(c).strip() for c in data.columns]
    for col in ["Sales", "Units", "Gross Profit", "Cost"]:
        if col in data:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    if "Product Name" in data:
        data["Factory"] = data["Product Name"].map(FACTORY_MAP).fillna("Unmapped")
    else:
        data["Factory"] = "Unknown"
    for col in ["Order Date", "Ship Date"]:
        if col in data:
            # Preserve source values; parsed dates are separate derived columns.
            data[col + " (parsed)"] = pd.to_datetime(data[col], errors="coerce", dayfirst=True)
    if {"Order Date (parsed)", "Ship Date (parsed)"}.issubset(data.columns):
        data["Order-to-Ship Days"] = (
            data["Ship Date (parsed)"] - data["Order Date (parsed)"]
        ).dt.total_seconds() / 86400
    else:
        data["Order-to-Ship Days"] = float("nan")
    return data

if not DATA_PATH.exists():
    st.error("Dataset not found. Place `Nassau Candy Distributor.csv` in the same folder as `app.py`.")
    st.info("This starter ZIP intentionally does not include the source CSV. Copy your existing CSV into this folder; the app reads it without writing to or modifying it.")
    st.stop()

try:
    df_all = load_data(str(DATA_PATH), DATA_PATH.stat().st_mtime)
except Exception as exc:
    st.error(f"Could not read the CSV: {exc}")
    st.stop()

required_cols = {"Product Name", "Sales", "Units", "Gross Profit", "Cost"}
missing_cols = sorted(required_cols - set(df_all.columns))
if missing_cols:
    st.error("Missing required columns: " + ", ".join(missing_cols))
    st.stop()

if "State/Province" not in df_all.columns:
    df_all["State/Province"] = "Unknown"
if "Region" not in df_all.columns:
    df_all["Region"] = "Unknown"
if "Ship Mode" not in df_all.columns:
    df_all["Ship Mode"] = "Unknown"
if "Order ID" not in df_all.columns:
    df_all["Order ID"] = "Row " + df_all.index.astype(str)
if "City" not in df_all.columns:
    df_all["City"] = "Unknown"

# Normalized derived state label for mapping. Original State/Province remains untouched.
def normalize_state(value):
    if pd.isna(value):
        return None
    raw = str(value).strip()
    if raw in STATE_COORDS:
        return raw
    if raw.upper() in STATE_ABBR:
        return STATE_ABBR[raw.upper()]
    return raw.title()

df_all["State (normalized)"] = df_all["State/Province"].map(normalize_state)
df_all["State Latitude"] = df_all["State (normalized)"].map(
    lambda x: STATE_COORDS.get(x, (None, None))[0]
)
df_all["State Longitude"] = df_all["State (normalized)"].map(
    lambda x: STATE_COORDS.get(x, (None, None))[1]
)

# Sidebar controls
st.sidebar.header("Dashboard filters")
date_col = "Order Date (parsed)"
valid_dates = df_all[date_col].dropna() if date_col in df_all else pd.Series(dtype="datetime64[ns]")
if not valid_dates.empty:
    min_date, max_date = valid_dates.min().date(), valid_dates.max().date()
    date_range = st.sidebar.date_input("Order date range", value=(min_date, max_date),
                                        min_value=min_date, max_value=max_date)
else:
    date_range = None
region_options = sorted(df_all["Region"].dropna().astype(str).unique().tolist())
region_sel = st.sidebar.multiselect("Region", region_options, default=region_options)
state_options = sorted(df_all["State/Province"].dropna().astype(str).unique().tolist())
state_sel = st.sidebar.multiselect("State / Province", state_options, default=state_options)
mode_options = sorted(df_all["Ship Mode"].dropna().astype(str).unique().tolist())
mode_sel = st.sidebar.multiselect("Ship mode", mode_options, default=mode_options)
factory_options = sorted(df_all["Factory"].dropna().astype(str).unique().tolist())
factory_sel = st.sidebar.multiselect("Factory", factory_options, default=factory_options)
max_lead_observed = df_all["Order-to-Ship Days"].where(df_all["Order-to-Ship Days"] >= 0).dropna()
slider_max = int(min(2000, max(30, max_lead_observed.quantile(0.95)))) if not max_lead_observed.empty else 365
delay_threshold = st.sidebar.slider("Flag intervals longer than (days)", 1, slider_max, min(30, slider_max))
st.sidebar.caption("Date filter uses parsed Order Date. Lead-time threshold is an investigation flag, not a confirmed delivery SLA.")
if st.sidebar.button("Reset filters"):
    st.rerun()

df = df_all.copy()
if date_range and isinstance(date_range, (tuple, list)) and len(date_range) == 2 and date_col in df:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1]) + pd.Timedelta(days=1) - pd.Timedelta(microseconds=1)
    df = df[df[date_col].between(start, end) | df[date_col].isna()]
df = df[df["Region"].astype(str).isin(region_sel)]
df = df[df["State/Province"].astype(str).isin(state_sel)]
df = df[df["Ship Mode"].astype(str).isin(mode_sel)]
df = df[df["Factory"].astype(str).isin(factory_sel)]

# Shared helper
def safe_pct(numerator, denominator):
    return (numerator / denominator * 100) if denominator else 0.0

sales = df["Sales"].sum(skipna=True)
profit = df["Gross Profit"].sum(skipna=True)
units = df["Units"].sum(skipna=True)
margin = safe_pct(profit, sales)
valid_intervals = df["Order-to-Ship Days"].dropna()
valid_nonnegative = valid_intervals[valid_intervals >= 0]
flagged = valid_nonnegative[valid_nonnegative > delay_threshold]
mean_days = valid_nonnegative.mean() if not valid_nonnegative.empty else float("nan")

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Records", f"{len(df):,}")
k2.metric("Sales", f"${sales:,.2f}")
k3.metric("Gross profit", f"${profit:,.2f}")
k4.metric("Units", f"{units:,.0f}")
k5.metric("Avg. order-to-ship interval", f"{mean_days:,.1f} days" if pd.notna(mean_days) else "N/A")
st.caption(f"Gross margin: {margin:.2f}% • {len(flagged):,} non-negative intervals exceed the selected {delay_threshold}-day investigation threshold.")

tabs = st.tabs(["Overview", "Route efficiency", "US map", "Ship mode", "Route drill-down", "Data quality"])

with tabs[0]:
    st.subheader("Factory performance")
    factory_summary = df.groupby("Factory", dropna=False).agg(
        Records=("Factory", "size"), Units=("Units", "sum"), Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    ).reset_index()
    factory_summary["Gross Margin (%)"] = factory_summary.apply(
        lambda r: safe_pct(r["Gross_Profit"], r["Sales"]), axis=1
    )
    factory_summary = factory_summary.sort_values("Sales", ascending=False)
    a, b = st.columns(2)
    with a:
        fig = px.bar(factory_summary, x="Factory", y="Sales", title="Sales by factory",
                     labels={"Sales": "Sales ($)"})
        st.plotly_chart(fig, use_container_width=True)
    with b:
        fig = px.bar(factory_summary, x="Factory", y="Gross_Profit", title="Gross profit by factory",
                     labels={"Gross_Profit": "Gross profit ($)"})
        st.plotly_chart(fig, use_container_width=True)
    st.dataframe(factory_summary, use_container_width=True, hide_index=True)
    st.subheader("Product performance")
    product_summary = df.groupby("Product Name", dropna=False).agg(
        Records=("Product Name", "size"), Units=("Units", "sum"), Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    ).reset_index().sort_values("Sales", ascending=False)
    st.dataframe(product_summary, use_container_width=True, hide_index=True)
    st.download_button("Download factory summary CSV", factory_summary.to_csv(index=False).encode("utf-8"),
                       "factory_summary.csv", "text/csv")

with tabs[1]:
    st.subheader("Factory → customer state / region routes")
    route_dimension = st.radio("Route destination level", ["State / Province", "Region"], horizontal=True)
    dest_col = "State (normalized)" if route_dimension == "State / Province" else "Region"
    route_source = df.copy()
    route_source["Route destination"] = route_source[dest_col].fillna("Unknown").astype(str)
    route_source["Valid non-negative interval"] = route_source["Order-to-Ship Days"].where(
        route_source["Order-to-Ship Days"] >= 0
    )
    routes = route_source.groupby(["Factory", "Route destination"], dropna=False).agg(
        Shipments=("Order ID", "size"),
        Avg_Interval_Days=("Valid non-negative interval", "mean"),
        Median_Interval_Days=("Valid non-negative interval", "median"),
        Interval_Std_Days=("Valid non-negative interval", "std"),
        Sales=("Sales", "sum"), Gross_Profit=("Gross Profit", "sum")
    ).reset_index()
    routes["Delay Count"] = route_source.assign(
        _flag=route_source["Order-to-Ship Days"].gt(delay_threshold)
    ).groupby(["Factory", "Route destination"], dropna=False)["_flag"].sum().to_numpy()
    routes["Delay Rate (%)"] = routes.apply(lambda r: safe_pct(r["Delay Count"], r["Shipments"]), axis=1)
    route_median = routes["Avg_Interval_Days"].median()
    if pd.isna(route_median) or route_median <= 0:
        route_median = 1
    routes["Efficiency Score (relative)"] = (
        100 * (1 - routes["Avg_Interval_Days"] / max(routes["Avg_Interval_Days"].max(), 1))
    ).clip(0, 100)
    st.caption("Lower average order-to-ship interval ranks faster. The relative score is descriptive and is not an SLA or validated delivery score. Routes with missing/invalid dates may have no interval.")
    min_shipments = st.slider("Minimum route shipment count", 1, max(1, int(routes["Shipments"].max())), 1)
    eligible = routes[(routes["Shipments"] >= min_shipments) & routes["Avg_Interval_Days"].notna()].copy()
    fast = eligible.sort_values("Avg_Interval_Days", ascending=True).head(10)
    slow = eligible.sort_values("Avg_Interval_Days", ascending=False).head(10)
    l, r = st.columns(2)
    with l:
        st.markdown("**10 fastest routes by observed interval**")
        st.dataframe(fast, use_container_width=True, hide_index=True)
    with r:
        st.markdown("**10 slowest routes by observed interval**")
        st.dataframe(slow, use_container_width=True, hide_index=True)
    st.markdown("**All route metrics**")
    st.dataframe(routes.sort_values("Avg_Interval_Days"), use_container_width=True, hide_index=True)
    st.download_button("Download route analysis CSV", routes.to_csv(index=False).encode("utf-8"),
                       "route_efficiency.csv", "text/csv")

with tabs[2]:
    st.subheader("US state-level shipping interval map")
    st.caption("Map uses approximate state centroids, not customer addresses. States with unrecognized names/abbreviations are excluded from the map.")
    map_df = df[df["State Latitude"].notna() & df["State Longitude"].notna()].copy()
    map_df["Valid interval"] = map_df["Order-to-Ship Days"].where(map_df["Order-to-Ship Days"] >= 0)
    state_summary = map_df.groupby(["State (normalized)", "State Latitude", "State Longitude"], dropna=False).agg(
        Shipments=("Order ID", "size"), Avg_Interval_Days=("Valid interval", "mean"),
        Sales=("Sales", "sum")
    ).reset_index()
    if not state_summary.empty:
        fig = px.scatter_geo(
            state_summary, lat="State Latitude", lon="State Longitude", size="Shipments",
            color="Avg_Interval_Days", hover_name="State (normalized)",
            hover_data={"Shipments": True, "Avg_Interval_Days": ":.1f", "Sales": ":,.2f",
                        "State Latitude": False, "State Longitude": False},
            scope="usa", color_continuous_scale="YlOrRd",
            title="State shipment volume and average order-to-ship interval"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(state_summary.sort_values("Avg_Interval_Days", ascending=False),
                     use_container_width=True, hide_index=True)
    else:
        st.warning("No recognizable US state names or abbreviations were found in the current filter selection.")

    st.markdown("**Factory locations**")
    fdf = pd.DataFrame([{"Factory": k, "Latitude": v[0], "Longitude": v[1]} for k, v in FACTORY_COORDS.items()])
    fig = px.scatter_geo(fdf, lat="Latitude", lon="Longitude", hover_name="Factory", scope="usa",
                         title="Supplied factory coordinates")
    st.plotly_chart(fig, use_container_width=True)

with tabs[3]:
    st.subheader("Shipping method comparison")
    mode = df.copy()
    mode["Valid interval"] = mode["Order-to-Ship Days"].where(mode["Order-to-Ship Days"] >= 0)
    mode_summary = mode.groupby("Ship Mode", dropna=False).agg(
        Shipments=("Order ID", "size"), Avg_Interval_Days=("Valid interval", "mean"),
        Median_Interval_Days=("Valid interval", "median"), Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum")
    ).reset_index()
    mode_summary["Flagged intervals"] = mode.groupby("Ship Mode", dropna=False)["Order-to-Ship Days"].apply(
        lambda x: int((x > delay_threshold).sum())
    ).to_numpy()
    mode_summary["Flagged rate (%)"] = mode_summary.apply(
        lambda r: safe_pct(r["Flagged intervals"], r["Shipments"]), axis=1
    )
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(px.bar(mode_summary, x="Ship Mode", y="Avg_Interval_Days",
                               title="Average order-to-ship interval by ship mode"), use_container_width=True)
    with c2:
        st.plotly_chart(px.bar(mode_summary, x="Ship Mode", y="Flagged rate (%)",
                               title=f"Intervals above {delay_threshold} days"), use_container_width=True)
    st.dataframe(mode_summary, use_container_width=True, hide_index=True)
    st.info("The dataset has no explicit shipping-charge field or confirmed delivery date. This is a descriptive interval comparison, not proof of transit time, shipping-cost trade-offs, or late-delivery frequency.")

with tabs[4]:
    st.subheader("Inspect route and order records")
    available_factories = sorted(df["Factory"].dropna().astype(str).unique())
    chosen_factory = st.selectbox("Factory to inspect", available_factories)
    factory_rows = df[df["Factory"].astype(str) == chosen_factory]
    available_states = sorted(factory_rows["State/Province"].dropna().astype(str).unique())
    chosen_state = st.selectbox("Destination state / province", ["All"] + available_states)
    detail = factory_rows if chosen_state == "All" else factory_rows[factory_rows["State/Province"].astype(str) == chosen_state]
    if "Order Date (parsed)" in detail and "Ship Date (parsed)" in detail:
        detail = detail.copy()
        detail["Order Date (display)"] = detail["Order Date (parsed)"].dt.strftime("%Y-%m-%d")
        detail["Ship Date (display)"] = detail["Ship Date (parsed)"].dt.strftime("%Y-%m-%d")
    preferred = [c for c in ["Order ID", "Customer ID", "Factory", "City", "State/Province", "Region",
                              "Ship Mode", "Order Date (display)", "Ship Date (display)",
                              "Order-to-Ship Days", "Product Name", "Sales", "Units", "Gross Profit"] if c in detail.columns]
    st.write(f"{len(detail):,} order line records match this selection.")
    st.dataframe(detail[preferred].sort_values("Order-to-Ship Days", na_position="last") if "Order-to-Ship Days" in preferred else detail[preferred],
                 use_container_width=True, hide_index=True)
    st.download_button("Download selected order records CSV", detail[preferred].to_csv(index=False).encode("utf-8"),
                       "selected_order_records.csv", "text/csv")

with tabs[5]:
    st.subheader("Data quality and validation")
    quality = pd.DataFrame({
        "Check": [
            "Rows in source", "Columns in source", "Exact duplicate rows",
            "Missing cells (all columns)", "Missing Order Date values after parsing",
            "Missing Ship Date values after parsing", "Negative order-to-ship intervals",
            "Non-negative intervals above threshold", "Intervals over 365 days",
            "Unmapped products", "Rows with unknown state centroid"
        ],
        "Result": [
            len(df_all), len(df_all.columns), int(df_all.duplicated().sum()),
            int(df_all.isna().sum().sum()),
            int(df_all["Order Date (parsed)"].isna().sum()) if "Order Date (parsed)" in df_all else "Date column missing",
            int(df_all["Ship Date (parsed)"].isna().sum()) if "Ship Date (parsed)" in df_all else "Date column missing",
            int((df_all["Order-to-Ship Days"] < 0).sum()),
            int((df_all["Order-to-Ship Days"] > delay_threshold).sum()),
            int((df_all["Order-to-Ship Days"] > 365).sum()),
            int((df_all["Factory"] == "Unmapped").sum()),
            int(df_all["State Latitude"].isna().sum())
        ]
    })
    st.dataframe(quality, use_container_width=True, hide_index=True)
    st.warning(
        "Critical interpretation note: earlier analysis found a median order-to-ship interval near 1,274 days. "
        "That is implausibly large for ordinary shipping. The app preserves source date values and calculates a separate parsed interval, "
        "but date format and business meaning must be confirmed before these values are described as actual shipping or delivery delays."
    )
    st.markdown("**Date sample for manual validation**")
    date_cols = [c for c in ["Order ID", "Order Date", "Order Date (parsed)", "Ship Date", "Ship Date (parsed)", "Order-to-Ship Days"] if c in df_all]
    st.dataframe(df_all[date_cols].head(25), use_container_width=True, hide_index=True)
    st.download_button("Download full data-quality report CSV", quality.to_csv(index=False).encode("utf-8"),
                       "data_quality_report.csv", "text/csv")

st.markdown("---")
st.caption("Project analysis is descriptive. State map points are approximate centroids; factory coordinates are supplied project inputs. Validate dates and confirm field definitions before operational decisions.")
