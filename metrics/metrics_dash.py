import streamlit as st
import pandas as pd

def main():
    st.title("Business Metrics Learning Dashboard")
    
    # Sidebar for framework selection
    framework = st.sidebar.radio(
        "Select Framework",
        ["How to Measure Anything", "Theory of Constraints", "Product Analytics"]
    )
    
    # Dictionary containing all framework information
    frameworks = {
        "How to Measure Anything": {
            "concepts": [
                {
                    "title": "Clarifying the Measurement",
                    "description": "If it matters, it's measurable",
                    "example": "Measuring 'skin glow' by breaking it down into observable components (hydration levels, evenness, light reflection)",
                    "metrics": [" Specific observable components", "Current measurement uncertainty", "Value of reducing uncertainty"]
                },
                {
                    "title": "Information Value",
                    "description": "Know what's worth measuring",
                    "example": "Determining whether to invest in an AI skin analysis tool",
                    "metrics": ["Cost of being wrong", "Value of better information", "Risk reduction opportunity"]
                },
                {
                    "title": "Calibrated Estimation",
                    "description": "Making better estimates under uncertainty",
                    "example": "Predicting customer response to new formulation",
                    "metrics": ["Confidence Intervals", "Historical Accuracy", "Range-based Estimates"]
                },
                {
                    "title": "Sampling Methods",
                    "description": "Getting meaningful data with less measurement",
                    "example": "Testing new products with representative customer segments",
                    "metrics": ["Sample Size Calculations", "Margin of Error", "Statistical Significance"]
                },
                {
                    "title": "Proxy Measurements",
                    "description": "Measuring something by measuring something else",
                    "example": "Using repurchase rate as proxy for product satisfaction",
                    "metrics": ["Correlation Strength", "Leading Indicators", "Secondary Measures"]
                },
                {
                    "title": "Breaking Down Intangibles",
                    "description": "Making 'unmeasurable' things measurable",
                    "example": "Measuring 'clean beauty' perception",
                    "metrics": ["Component Measurements", "Expected Value", "Composite Scores"]
                },
                {
                    "title": "Risk Analysis",
                    "description": "Quantifying uncertainty and risk",
                    "example": "Launching new product line",
                    "metrics": ["Probability Distributions", "Observable Indicators", "Risk Tolerance Thresholds"]
                },
                {
                    "title": "Measurement Economics",
                    "description": "Making measurements worth the effort",
                    "example": "Cost-benefit of customer surveys vs. usage data",
                    "metrics": ["Cost of Measurement", "Expected Value of Information", "ROI of Information"]
                }
            ]
        },

        "Theory of Constraints": {
            "concepts": [
                {
                    "title": "Identify",
                    "description": "Find the system's main bottleneck/constraint that's limiting overall performance",
                    "example": "Customer drop-off between receiving products and establishing daily skincare routine",
                    "metrics": ["Conversion Rates", "Usage Patterns", "Time Between Purchases", "Churn Analysis"]
                },
                {
                    "title": "Exploit",
                    "description": "Make the constraint as efficient as possible using existing resources",
                    "example": "Simplify skincare routines, create better onboarding, identify 'gateway' habits",
                    "metrics": ["Routine Completion Rates", "Tutorial Engagement", "Time To Form Habit", "Product Usage Frequency"]
                },
                {
                    "title": "Subordinate",
                    "description": "Align all other processes to support the constraint",
                    "example": "Adjust education content to focus on habit formation, redesign packaging for easier use",
                    "metrics": ["Support Ticket Categories", "Education Completion Rates", "Resource Allocation Effectiveness"]
                },
                {
                    "title": "Elevate",
                    "description": "If needed, make major changes or investments to break the constraint",
                    "example": "Develop smart mirrors, hire personal coaches, create simplified product lines",
                    "metrics": ["ROI of New Investments", "Impact On Retention", "Cost Per Retained User", "Improvement In Constraint Throughput"]
                },
                {
                    "title": "Repeat",
                    "description": "Once current constraint is resolved, identify the next bottleneck",
                    "example": "After solving usage consistency, focus on results visualization → repurchase conversion",
                    "metrics": ["System Throughput", "New Bottleneck Indicators", "Overall Efficiency Improvements"]
                },
            ]
        },

        "Product Analytics": {
            "concepts": [
                {
                    "title": "Core Product Metric Categories",
                    "description": "Product metrics that fall into 5 main categories",
                    "example": "ride hailing app like Lyft",
                    "metrics": ["Acquisition (new users/leads)", "Activation (user onboarding success)", "Engagement (active usage)", "Retention (user stickiness)", "Monetization (revenue metrics)"]
                },
                {
                    "title": "Leading vs Lagging Indicators",
                    "description": "Descriptive or Prescriptive Analytics",
                    "example": "LTV and KPI metrics",
                    "metrics": ["Leading indicators help predict future performance and drive daily tactics", "Lagging indicators measure past success and long-term strategy", "You need both types to effectively understand product performance"]
                },
                {
                    "title": "Essential Metrics to Track",
                    "description": "High-level business metrics",
                    "example": "SaaS products",
                    "metrics": ["Acquisition: New signups, Customer Acquisition Cost (CAC)",
                                "Activation: Activation rate, Time to activate, Free-to-paid conversion",
                                "Engagement: MAU/WAU/DAU, Stickiness (DAU/MAU), Feature usage",
                                "Retention: Retention rate, Churn rate, Customer Lifetime Value (CLV)",
                                "Monetization: Monthly Recurring Revenue (MRR), Net Revenue Retention (NRR), Average Revenue Per User (ARPU)"]
                },
                {
                    "title": "Key Calculations",
                    "description": "What needs to be performed in SQL",
                    "example": "These are proportions, not straight numbers",
                    "metrics": ["Activation Rate = Users who trigger activation / All users",
                                "Stickiness = Daily Active Users / Monthly Active Users"
                                "Churn Rate = Total active users at end / Total active users at start"
                                "ARPU = Monthly Revenue / Monthly Active Users"]
                },
                {
                    "title": "Best Practices",
                    "description": "Follow these",
                    "example": "Lessons from defining/following the wrong numbers for insight/strategy",
                    "metrics": ["Avoid vanity metrics that don't provide actionable insights",
                                "Track a mix of leading and lagging indicators",
                                "Focus on metrics that align with product goals",
                                "Use metrics to form hypotheses and test product changes",
                                "Look for correlations between feature usage and retention/revenue"]
                },
                {
                    "title": "Visualization Tips",
                    "description": "A picture says a thousand words",
                    "example": "Executive reporting",
                    "metrics": ["Use funnel analysis for conversion tracking",
                                "Create feature matrices to analyze feature adoption",
                                "Track cohort analysis for retention patterns",
                                "Monitor trends over time with time series charts"]
                                                }
            ]
        }
    }
    
    # Display selected framework
    st.header(framework)
    
    # Display concepts for selected framework
    for concept in frameworks[framework]["concepts"]:
        with st.expander(f"📊 {concept['title']}", expanded=True):
            st.subheader("Description")
            st.write(concept["description"])
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Example")
                st.write(concept["example"])
            with col2:
                st.subheader("Key Metrics")
                for metric in concept["metrics"]:
                    st.write(f"• {metric}")
            
            # Add interactive elements
            if st.checkbox(f"Add notes for {concept['title']}", key=concept['title']):
                user_notes = st.text_area("Your Notes", key=f"notes_{concept['title']}")
                if user_notes:
                    st.success("Notes saved!")

if __name__ == "__main__":
    st.set_page_config(page_title="Metrics Learning Dashboard", layout="wide")
    main()
