import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Set page config
st.set_page_config(
    page_title="Sephora Analytics Dashboard",
    page_icon="💄",
    layout="wide"
)

# Data generation functions
def generate_sales_data(start_date='2023-01-01', periods=365):
    """Generate daily sales data for different channels"""
    dates = pd.date_range(start=start_date, periods=periods)
    
    data = []
    for date in dates:
        retail_sales = np.random.normal(22000000, 3000000)
        online_sales = np.random.normal(9000000, 1500000)
        kohls_sales = np.random.normal(5000000, 1000000)
        
        if date.month in [11, 12]:
            retail_sales *= 1.5
            online_sales *= 1.8
            kohls_sales *= 1.4
        
        data.append({
            'date': date,
            'retail_sales': retail_sales,
            'online_sales': online_sales,
            'kohls_sales': kohls_sales,
            'total_sales': retail_sales + online_sales + kohls_sales,
            'week': date.isocalendar()[1],
            'month': date.month,
            'year': date.year
        })
    
    return pd.DataFrame(data)

def generate_digital_metrics(sales_df):
    """Generate digital experience and AI metrics"""
    digital_data = []
    
    for _, row in sales_df.iterrows():
        visitors = int(np.random.normal(500000, 50000))
        
        digital_data.append({
            'date': row['date'],
            'website_visitors': visitors,
            'mobile_app_users': int(visitors * 0.6),
            'conversion_rate': np.random.normal(0.03, 0.005),
            'ai_recommendations_shown': int(visitors * 0.8),
            'ai_driven_purchases': int(visitors * 0.15),
            'virtual_try_ons': int(visitors * 0.25),
            'personalized_emails_sent': int(visitors * 0.4),
            'email_engagement_rate': np.random.normal(0.22, 0.03),
            'app_engagement_minutes': np.random.normal(8, 2)
        })
    
    return pd.DataFrame(digital_data)

def generate_customer_segments():
    """Generate customer segment data"""
    segments = ['Beauty Enthusiast', 'Occasional Buyer', 'Luxury Seeker', 
                'Value Hunter', 'Gen Z Explorer']
    data = []
    
    for segment in segments:
        data.append({
            'segment': segment,
            'customer_count': int(np.random.normal(2000000, 300000)),
            'avg_basket_size': np.random.normal(65, 15),
            'annual_purchase_frequency': np.random.normal(6, 1.5),
            'online_shopping_preference': np.random.normal(0.4, 0.1),
            'ai_feature_adoption_rate': np.random.normal(0.3, 0.08),
            'loyalty_program_participation': np.random.normal(0.7, 0.1)
        })
    
    return pd.DataFrame(data)

def generate_ai_investments():
    """Generate AI initiative investment data"""
    initiatives = [
        'Personalization Engine', 'Virtual Try-On Technology', 
        'Customer Service AI', 'Inventory Optimization AI',
        'Predictive Analytics', 'Voice Commerce', 
        'AR Shopping Experience', 'AI Beauty Advisor'
    ]
    
    data = []
    for initiative in initiatives:
        data.append({
            'initiative': initiative,
            'investment_2024': np.random.normal(5000000, 1000000),
            'projected_investment_2025': np.random.normal(8000000, 1500000),
            'roi_2024': np.random.normal(0.15, 0.05),
            'projected_roi_2025': np.random.normal(0.25, 0.07),
            'implementation_progress': np.random.normal(0.7, 0.15),
            'customer_adoption_rate': np.random.normal(0.3, 0.1)
        })
    
    return pd.DataFrame(data)

# Generate data
@st.cache_data
def load_data():
    sales_df = generate_sales_data()
    digital_df = generate_digital_metrics(sales_df)
    segments_df = generate_customer_segments()
    ai_investments_df = generate_ai_investments()
    return sales_df, digital_df, segments_df, ai_investments_df

# Load data
sales_df, digital_df, segments_df, ai_investments_df = load_data()

# Filtered data
# Sidebar filters (optional)

# Date range selector
with st.sidebar:
    st.header("Filters")
    
    # Date range selector
    min_date = sales_df['date'].min()
    max_date = sales_df['date'].max()
    date_range = st.date_input(
        "Select Date Range",
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

# Apply filters to data
filtered_sales_df = sales_df[(sales_df['date'] >= pd.Timestamp(start_date)) & 
                             (sales_df['date'] <= pd.Timestamp(end_date))]
filtered_digital_df = digital_df[(digital_df['date'] >= pd.Timestamp(start_date)) & 
                                 (digital_df['date'] <= pd.Timestamp(end_date))]

# Filter the segments dataframe based on the user selection
filtered_segments_df = segments_df[segments_df['segment'].isin(selected_segments)]

# Dashboard title
st.title("🎯 Sephora Analytics Dashboard")
st.subheader("Monthly Comparisons")

# Top metrics
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

# Daily Visitors
current_visitors = filtered_digital_df[filtered_digital_df['date'].dt.month == current_month]['website_visitors'].mean()
previous_visitors = filtered_digital_df[filtered_digital_df['date'].dt.month == previous_month]['website_visitors'].mean()
visitors_change = ((current_visitors - previous_visitors) / previous_visitors) * 100 if previous_visitors else 0

# AI-Driven Sales
current_ai_ratio = (filtered_digital_df[filtered_digital_df['date'].dt.month == current_month]['ai_driven_purchases'].sum() / 
                    filtered_digital_df[filtered_digital_df['date'].dt.month == current_month]['website_visitors'].sum() * 100) if current_visitors else 0
previous_ai_ratio = (filtered_digital_df[filtered_digital_df['date'].dt.month == previous_month]['ai_driven_purchases'].sum() / 
                     filtered_digital_df[filtered_digital_df['date'].dt.month == previous_month]['website_visitors'].sum() * 100) if previous_visitors else 0
ai_ratio_change = current_ai_ratio - previous_ai_ratio

# Display Metrics
with col1:
    st.metric(
        "Total Revenue (MTD)", 
        f"${current_revenue/1e6:.1f}M",
        f"{revenue_change:+.1f}%",
        delta_color="inverse"
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
        "Daily Visitors",
        f"{current_visitors/1000:.0f}K",
        f"{visitors_change:+.1f}%",
        delta_color="normal"
    )

with col4:
    st.metric(
        "AI-Driven Sales",
        f"{current_ai_ratio:.1f}%",
        f"{ai_ratio_change:+.1f}%",
        delta_color="normal"
    )
   

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Sales Performance", "Digital Engagement", 
    "Customer Segments", "AI Initiatives"
])

# Sales Performance Tab
with tab1:
    st.subheader("Channel Performance Trends")
    
    # Prepare monthly data
    monthly_sales = filtered_sales_df.groupby('month').agg({
        'retail_sales': 'sum',
        'online_sales': 'sum',
        'kohls_sales': 'sum'
    }).reset_index()
    
    # Create stacked bar chart
    fig = px.bar(
        monthly_sales,
        x='month',
        y=['retail_sales', 'online_sales', 'kohls_sales'],
        title='Monthly Sales by Channel',
        labels={'value': 'Sales ($)', 'month': 'Month'},
        template='plotly_white'
    )
    fig.update_layout(barmode='stack', height=500)
    st.plotly_chart(fig, use_container_width=True)

# Digital Engagement Tab
with tab2:
    st.subheader("Digital Engagement Metrics")
    
    # Calculate aggregates
    avg_mobile_app_users = filtered_digital_df['mobile_app_users'].mean()
    avg_conversion_rate = filtered_digital_df['conversion_rate'].mean() * 100  # Convert to percentage
    total_ai_driven_purchases = filtered_digital_df['ai_driven_purchases'].sum()
    total_personalized_emails = filtered_digital_df['personalized_emails_sent'].sum()
    avg_email_engagement_rate = filtered_digital_df['email_engagement_rate'].mean() * 100  # Convert to percentage
    avg_app_engagement_minutes = filtered_digital_df['app_engagement_minutes'].mean()

    # Display aggregate metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg. Mobile App Users", f"{avg_mobile_app_users:,.0f}")
        st.metric("Avg. App Engagement Minutes", f"{avg_app_engagement_minutes:.1f} mins")
    with col2:
        st.metric("Avg. Conversion Rate", f"{avg_conversion_rate:.2f}%")
        st.metric("Total AI-Driven Purchases", f"{total_ai_driven_purchases:,}")
    with col3:
        st.metric("Total Personalized Emails", f"{total_personalized_emails:,}")
        st.metric("Avg. Email Engagement Rate", f"{avg_email_engagement_rate:.2f}%")
        

    # Create time series plot
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('Website Traffic', 'AI Feature Engagement', 'Virtual Try-On\'s'),
        vertical_spacing=0.12
    )
    
    # Traffic and conversions
    fig.add_trace(
        go.Scatter(
            x=filtered_digital_df['date'],
            y=filtered_digital_df['website_visitors'],
            name='Website Visitors'
        ),
        row=1, col=1
    )
    
    # AI engagement
    fig.add_trace(
        go.Scatter(
            x=filtered_digital_df['date'],
            y=filtered_digital_df['ai_recommendations_shown'],
            name='AI Recommendations',
            line=dict(color='orange')
        ),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(
            x=filtered_digital_df['date'],
            y=filtered_digital_df['virtual_try_ons'],
            name='Virtual Try-On\'s',
            line=dict(color='green')
        ),
        row=3, col=1
    )
    
    fig.update_layout(height=700)
    st.plotly_chart(fig, use_container_width=True)

# Customer Segments Tab
with tab3:
    st.subheader("Customer Segment Analysis")
    
    # Calculate segment value
    filtered_segments_df['annual_value'] = (filtered_segments_df['customer_count'] * 
                                 filtered_segments_df['avg_basket_size'] * 
                                 filtered_segments_df['annual_purchase_frequency'])
    
    # Create bubble chart
    fig = px.scatter(
        filtered_segments_df,
        x='ai_feature_adoption_rate',
        y='loyalty_program_participation',
        size='annual_value',
        color='segment',
        title='Customer Segment Analysis',
        labels={
            'ai_feature_adoption_rate': 'AI Feature Adoption Rate',
            'loyalty_program_participation': 'Loyalty Program Participation'
        }
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# AI Initiatives Tab
with tab4:
    st.subheader("AI Investment Analysis")
    
    # ROI comparison chart
    fig = go.Figure(data=[
        go.Bar(
            name='2024 ROI',
            x=ai_investments_df['initiative'],
            y=ai_investments_df['roi_2024']
        ),
        go.Bar(
            name='2025 Projected ROI',
            x=ai_investments_df['initiative'],
            y=ai_investments_df['projected_roi_2025']
        )
    ])
    
    fig.update_layout(
        title='AI Initiative ROI Comparison',
        barmode='group',
        xaxis_tickangle=-45,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Priority matrix
    fig = px.scatter(
        ai_investments_df,
        x='projected_roi_2025',
        y='customer_adoption_rate',
        size='projected_investment_2025',
        color='implementation_progress',
        text='initiative',
        title='AI Initiative Priority Matrix'
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)