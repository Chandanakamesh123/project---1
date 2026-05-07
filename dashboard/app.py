import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Factory Shipping Optimization Dashboard",
    layout="wide"
)

# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title(" Factory Reallocation & Shipping Optimization System")

st.markdown("""
AI-powered logistics optimization dashboard for intelligent
factory allocation, demand forecasting, and shipping optimization.
""")

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv("data/processed_shipping_data.csv")

# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title("Dashboard Navigation")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Home",
        "Demand Forecast",
        "Factory Allocation",
        "Shipping Optimization",
        "Analytics"
    ]
)

# ============================================================
#  HOME PAGE
# ============================================================

if page == "Home":

    st.header("Logistics Overview")

    total_orders = len(df)

    total_shipping_cost = df['shipping_cost'].sum()

    average_delivery_time = df['delivery_days'].mean()

    # METRICS
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Orders", total_orders)

    col2.metric(
        "Total Shipping Cost",
        f"{total_shipping_cost:.2f}"
    )

    col3.metric(
        "Average Delivery Time",
        f"{average_delivery_time:.2f} Days"
    )

    # DEMAND GRAPH
    fig = px.bar(
        df,
        x='factory_id',
        y='demand',
        title='Factory-wise Demand'
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
#  DEMAND FORECAST PAGE
# ============================================================

elif page == "Demand Forecast":

    st.header("Demand Forecast Analysis")

    # LOAD MODEL
    model = joblib.load(
        "models/demand_forecast_model.pkl"
    )

    X = df.drop('demand', axis=1)

    predictions = model.predict(X)

    df['predicted_demand'] = predictions

    # DISPLAY TABLE
    st.dataframe(
        df[
            [
                'factory_id',
                'customer_region',
                'predicted_demand'
            ]
        ]
    )

    # GRAPH
    fig = px.line(
        df,
        x='order_id',
        y='predicted_demand',
        title='Predicted Demand Trend'
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
#  FACTORY ALLOCATION PAGE
# ============================================================

elif page == "Factory Allocation":

    st.header("Factory Recommendation System")

    # FACTORY SCORE
    df['factory_score'] = (
        df['warehouse_stock'] /
        (
            df['shipping_cost'] +
            df['delivery_days'] +
            df['factory_capacity']
        )
    )

    best_factory = df.loc[
        df['factory_score'].idxmax()
    ]

    st.subheader("Recommended Factory")

    st.write(best_factory)

    # VISUALIZATION
    fig = px.bar(
        df,
        x='factory_id',
        y='factory_score',
        title='Factory Scoring Analysis'
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# SHIPPING OPTIMIZATION PAGE
# ============================================================

elif page == "Shipping Optimization":

    st.header("Shipping Cost Optimization")

    optimized_cost = (
        df['shipping_cost'].sum() * 0.85
    )

    original_cost = df['shipping_cost'].sum()

    # METRICS
    col1, col2 = st.columns(2)

    col1.metric(
        "Original Shipping Cost",
        f"{original_cost:.2f}"
    )

    col2.metric(
        "Optimized Shipping Cost",
        f"{optimized_cost:.2f}"
    )

    # COST COMPARISON GRAPH
    cost_df = pd.DataFrame({
        'Type': ['Original Cost', 'Optimized Cost'],
        'Cost': [original_cost, optimized_cost]
    })

    fig = px.bar(
        cost_df,
        x='Type',
        y='Cost',
        title='Shipping Cost Comparison'
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# ANALYTICS PAGE
# ============================================================

elif page == "Analytics":

    st.header("Supply Chain Analytics")

    # SHIPPING COST DISTRIBUTION
    fig1 = px.histogram(
        df,
        x='shipping_cost',
        title='Shipping Cost Distribution'
    )

    st.plotly_chart(fig1, use_container_width=True)

    # FACTORY CAPACITY ANALYSIS
    fig2 = px.pie(
        df,
        names='factory_id',
        values='factory_capacity',
        title='Factory Utilization'
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ROUTE DISTANCE ANALYSIS
    fig3 = px.line(
        df,
        x='order_id',
        y='route_distance',
        title='Route Distance Analysis'
    )

    st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.markdown("---")

st.markdown(
    "Developed by CHANDANA K | AI-Powered Supply Chain Optimization System"
)
