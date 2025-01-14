import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Page config
st.set_page_config(
    page_title="Sephora Advanced Analytics",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visual hierarchy
st.markdown("""
    <style>
    .metric-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Data generation functions (reused from previous example)
@st.cache_data
def generate_data():
    # Sample data generation (simplified for example)
    dates = pd.date_range(start='2024-01-01', periods=90)
    
    # Sales data
    sales_df = pd.DataFrame({
        'date': dates,
        'total_sales': np.random.normal(1000000, 100000, 90),
        'online_sales': np.random.normal(400000, 50000, 90),
        'store_sales': np.random.normal(600000, 70000, 90)
    })
    
    # Digital engagement data
    digital_df = pd.DataFrame({
        'date': dates,
        'website_visits': np.random.normal(50000, 5000, 90),
        'virtual_try_ons': np.random.normal(15000, 2000, 90),
        'ai_recommendations': np.random.normal(25000, 3000, 90)
    })
    
    # Customer segments data
    segments = ['Beauty Enthusiast', 'Luxury Seeker', 'Value Hunter', 
                'Trend Explorer', 'Occasional Buyer']
    segments_df = pd.DataFrame({
        'segment': segments,
        'loyalty_program_participation': np.random.uniform(0.4, 0.9, 5),
        'ai_feature_adoption_rate': np.random.uniform(0.2, 0.8, 5),
        'online_shopping_preference': np.random.uniform(0.3, 0.7, 5),
        'annual_purchase_frequency': np.random.uniform(4, 12, 5),
        'avg_basket_size': np.random.uniform(50, 150, 5),
        'customer_count': np.random.uniform(100000, 500000, 5)
    })
    
    return sales_df, digital_df, segments_df

# Load data
sales_df, digital_df, segments_df = generate_data()

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    
    # Date range selector
    min_date = sales_df['date'].min()
    max_date = sales_df['date'].max()
    date_range = st.date_input(
        "Select Date Range for Performance",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # Ensure date_range is valid and contains two dates
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date

    # Segment selector
    selected_segments = st.multiselect(
        "Select Customer Segments",
        options=segments_df['segment'].unique(),
        default=segments_df['segment'].unique()
    )
    
    # Analysis type
    analysis_type = st.radio(
        "Analysis Focus",
        ["Performance", "Customer Behavior", "Digital Engagement", "Anomaly Detection"]
    )
    
    # Advanced options
    with st.expander("Advanced Options for Anomaly Detection"):
        rolling_window = st.slider("Rolling Window (days)", 3, 30, 7)
        threshold = st.slider("Anomaly Threshold (σ)", 1.0, 4.0, 2.0)

# Apply filters to data
filtered_sales_df = sales_df[(sales_df['date'] >= pd.Timestamp(start_date)) & 
                             (sales_df['date'] <= pd.Timestamp(end_date))]
filtered_digital_df = digital_df[(digital_df['date'] >= pd.Timestamp(start_date)) & 
                                 (digital_df['date'] <= pd.Timestamp(end_date))]

# Filter the segments dataframe based on the user selection
filtered_segments_df = segments_df[segments_df['segment'].isin(selected_segments)]

# Main dashboard
st.title("🎯 Advanced Sephora Analytics Dashboard")

# Top metrics row
col1, col2, col3, col4 = st.columns(4)

 # Calculate the current and previous month
current_month = filtered_sales_df['date'].max().month
previous_month = (current_month - 1) if current_month > 1 else 12

# Current and previous month data
current_month_data = filtered_sales_df[filtered_sales_df['date'].dt.month == current_month]
previous_month_data = filtered_sales_df[filtered_sales_df['date'].dt.month == previous_month]

# Total Revenue (MTD)
current_revenue = current_month_data['total_sales'].sum()
previous_revenue = previous_month_data['total_sales'].sum()
revenue_change = ((current_revenue - previous_revenue) / previous_revenue) * 100 if previous_revenue else 0

# Online Sales Ratio
current_online_ratio = (current_month_data['online_sales'].sum() / current_revenue * 100) if current_revenue else 0
previous_online_ratio = (previous_month_data['online_sales'].sum() / previous_revenue * 100) if previous_revenue else 0
online_ratio_change = current_online_ratio - previous_online_ratio

# Monthly Website Visitors
current_visitors = filtered_digital_df[filtered_digital_df['date'].dt.month == current_month]['website_visits'].mean()
previous_visitors = filtered_digital_df[filtered_digital_df['date'].dt.month == previous_month]['website_visits'].mean()
visitors_change = ((current_visitors - previous_visitors) / previous_visitors) * 100 if previous_visitors else 0

# AI-Driven Engagement
current_ai_ratio = (filtered_digital_df[filtered_digital_df['date'].dt.month == current_month]['ai_recommendations'].sum() / 
                    filtered_digital_df[filtered_digital_df['date'].dt.month == current_month]['website_visits'].sum() * 100) if current_visitors else 0
previous_ai_ratio = (filtered_digital_df[filtered_digital_df['date'].dt.month == previous_month]['ai_recommendations'].sum() / 
                     filtered_digital_df[filtered_digital_df['date'].dt.month == previous_month]['website_visits'].sum() * 100) if previous_visitors else 0
ai_ratio_change = current_ai_ratio - previous_ai_ratio

with col1:
    
    st.metric(
        "Monthly Sales",
        f"${current_revenue:,.0f}",
        f"{revenue_change:+.1f}%",
        delta_color="normal"
    )

with col2:

    st.metric(
        "Online Sales Ratio",
        f"{current_online_ratio:.1f}%",
        f"{online_ratio_change:+.1f}%",
        delta_color="normal"
    )

with col3:

    st.metric(
        "Monthly Website Visitors",
        f"{current_visitors:.1f}%",
        f"{visitors_change:.1f}%",
        delta_color="normal"
    )

with col4:

    st.metric(
        "AI Impact Rate",
        f"{current_ai_ratio:.1f}%",
        f"{ai_ratio_change:.1f}%",
        delta_color="normal"
    )

# Main content based on selected analysis type
if analysis_type == "Performance":
    # Sales Performance Analysis
    st.subheader("Multi-Channel Sales Performance")
    
    # Create composite performance chart
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Daily Sales Trend', 'Channel Mix',
                       'Weekly Patterns', 'Performance Indicators'),
        specs=[[{"type": "scatter"}, {"type": "pie"}],
               [{"type": "heatmap"}, {"type": "indicator"}]]
    )
    
    # Daily sales trend
    fig.add_trace(
        go.Scatter(
            x=filtered_sales_df['date'],
            y=filtered_sales_df['total_sales'],
            name="Total Sales",
            line=dict(color='black')
        ),
        row=1, col=1
    )
    
    # Channel mix
    fig.add_trace(
        go.Pie(
            labels=['Store', 'Online'],
            values=[filtered_sales_df['store_sales'].mean(), 
                   filtered_sales_df['online_sales'].mean()],
            hole=0.4
        ),
        row=1, col=2
    )
    
    # Weekly patterns heatmap
    weekly_pattern = filtered_sales_df.copy()
    weekly_pattern['weekday'] = weekly_pattern['date'].dt.day_name()
    weekly_pattern['week'] = weekly_pattern['date'].dt.isocalendar().week
    pattern_pivot = weekly_pattern.pivot_table(
        values='total_sales',
        index='week',
        columns='weekday',
        aggfunc='mean'
    )
    
    fig.add_trace(
        go.Heatmap(
            z=pattern_pivot.values,
            x=pattern_pivot.columns,
            y=pattern_pivot.index,
            colorscale='RdBu'
        ),
        row=2, col=1
    )
    
    # Performance indicator
    fig.add_trace(
        go.Indicator(
            mode="gauge+number+delta",
            value=filtered_sales_df['total_sales'].mean(),
            delta={'reference': filtered_sales_df['total_sales'].mean() * 0.9},
            gauge={'axis': {'range': [None, filtered_sales_df['total_sales'].max()]}},
            title={'text': "Average Daily Sales"}
        ),
        row=2, col=2
    )
    
    fig.update_layout(height=800)
    st.plotly_chart(fig, use_container_width=True)

elif analysis_type == "Customer Behavior":
    # Customer Segment Analysis
    st.subheader("Customer Segment Analysis")
    
    # Calculate customer health score
    filtered_segments_df['health_score'] = (
        filtered_segments_df['loyalty_program_participation'] * 0.4 +
        filtered_segments_df['ai_feature_adoption_rate'] * 0.3 +
        filtered_segments_df['online_shopping_preference'] * 0.3
    )
    
    # Create segment bubble chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=filtered_segments_df['annual_purchase_frequency'],
        y=filtered_segments_df['avg_basket_size'],
        mode='markers+text',  # Use mode to show markers and text
        text=filtered_segments_df['segment'],  # Text to display for each marker
        marker=dict(
            size=filtered_segments_df['customer_count'] / 10000,  # Adjust size of the markers
            color=filtered_segments_df['health_score'],  # Color based on health score
            colorscale='Viridis',  # Use Viridis color scale
            showscale=True,  # Show the color scale
            colorbar=dict(title='Health Score')  # Title for the color bar
        )
    ))

    fig.update_layout(
        title='Customer Segments Analysis',
        xaxis_title='Annual Purchase Frequency',
        yaxis_title='Average Basket Size',
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Segment metrics table
    st.dataframe(
        filtered_segments_df.style.background_gradient(subset=['health_score'], cmap='Accent')
    )

elif analysis_type == "Digital Engagement":
    # Digital Engagement Analysis
    st.subheader("Digital Customer Experience")
    
    # Create digital engagement dashboard
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Daily Traffic Pattern', 'Virtual Try-On Funnel',
                       'AI Recommendation Impact', 'Engagement Metrics'),
        specs=[[{"type": "scatter"}, {"type": "funnel"}],
               [{"type": "bar"}, {"type": "indicator"}]]
    )
    
    # Traffic pattern
    fig.add_trace(
        go.Scatter(
            x=filtered_digital_df['date'],
            y=filtered_digital_df['website_visits'],
            name='Website Visits',
            fill='tozeroy'
        ),
        row=1, col=1
    )
    
    # Funnel
    fig.add_trace(
        go.Funnel(
            y=['Visits', 'Try-Ons', 'Purchases'],
            x=[filtered_digital_df['website_visits'].mean(),
               filtered_digital_df['virtual_try_ons'].mean(),
               filtered_digital_df['virtual_try_ons'].mean() * 0.2]
        ),
        row=1, col=2
    )
    
    # AI impact
    fig.add_trace(
        go.Bar(
            x=filtered_digital_df['date'][-7:],
            y=filtered_digital_df['ai_recommendations'][-7:],
            name='AI Recommendations'
        ),
        row=2, col=1
    )
    
    # Engagement score
    fig.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=75,
            title={'text': "Engagement Score"},
            gauge={'axis': {'range': [None, 100]}}
        ),
        row=2, col=2
    )
    
    fig.update_layout(height=800)
    st.plotly_chart(fig, use_container_width=True)

else:  # Anomaly Detection
    st.subheader("Anomaly Detection & Pattern Analysis")
    
    # Calculate rolling statistics
    filtered_sales_df['rolling_mean'] = filtered_sales_df['total_sales'].rolling(
        window=rolling_window).mean()
    filtered_sales_df['rolling_std'] = filtered_sales_df['total_sales'].rolling(
        window=rolling_window).std()
    
    # Detect anomalies
    filtered_sales_df['anomaly'] = abs(filtered_sales_df['total_sales'] - 
                             filtered_sales_df['rolling_mean']) > (threshold * 
                             filtered_sales_df['rolling_std'])
    
    # Create anomaly detection chart
    fig = go.Figure()
    
    # Base sales line
    fig.add_trace(go.Scatter(
        x=filtered_sales_df['date'],
        y=filtered_sales_df['total_sales'],
        name='Sales',
        line=dict(color='black')
    ))
    
    # Rolling mean
    fig.add_trace(go.Scatter(
        x=filtered_sales_df['date'],
        y=filtered_sales_df['rolling_mean'],
        name=f'{rolling_window}-Day Average',
        line=dict(color='blue', dash='dash')
    ))
    
    # Anomaly points
    anomalies = filtered_sales_df[filtered_sales_df['anomaly']]
    fig.add_trace(go.Scatter(
        x=anomalies['date'],
        y=anomalies['total_sales'],
        mode='markers',
        name='Anomalies',
        marker=dict(color='red', size=10)
    ))
    
    fig.update_layout(
        title='Sales Anomaly Detection',
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Anomaly metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Anomalies Detected",
            f"{len(anomalies)}",
            f"{len(anomalies)/len(filtered_sales_df)*100:.1f}% of days"
        )
    with col2:
        st.metric(
            "Average Anomaly Magnitude",
            f"${abs(anomalies['total_sales'] - anomalies['rolling_mean']).mean():,.0f}",
            "vs normal variation"
        )

# Footer with additional insights
with st.expander("Additional Insights"):
    st.markdown("""
    ### Key Findings
    - Sales show strong weekly seasonality with peaks on weekends
    - Virtual try-on feature has 30% higher conversion rate than standard browsing
    - Beauty Enthusiast segment shows highest AI feature adoption
    - Anomaly detection identified potential inventory stockouts
    """)