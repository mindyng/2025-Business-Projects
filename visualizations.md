# Basics
* in order to determine visualization to use, need to figure out measured variables' data types
  
* Different Types of Data:
  * NUMERICAL (discrete, continuous-infinite decimal points)
    * Continuous: values can take on (in theory) infinite decimal points. Has a meaningful 0 (e.g., the 0 point isn't arbitrary), which allows ratio comparisons (e.g,. according to the sample of participants, males are, on average, 20% taller than females)   
    * FYI: Interval or Ratio can be discrete/continuous
    * Interval data: On a scale, which have equal distances (e.g., Strongly Disagree - Disagree - Neither Agree or Disagree - Agree - Strongly Agree)
    * Allows use of parametrics statistics (which assume a normal distribution)
    * Time Series
  * CATEGORICAL (no order/ordered)
    * These values classify the samples into sets of similar samples. Within categorical features are the values nominal, ordinal, ratio and interval
    * Non-parametric stat's used here.

* Comparisons

  * Comparison (bivariate here) is done to see if variables:
    * covary (as x gets smaller/larger, then y gets smaller/larger)
    * depend on one another (x cannot happen without y)
    * predict one another (x leads to y)

      * determined by A/B Test. For cause in question, expose to experimental group from random sample of population. If same measurement between ctl and test group shows higher reading with exp group and there is stat sig effect from cause then can say with level of confidence that x leads to y

      * different typed of causation:
        * x causes y (direct causation);
        * y causes x (reverse causation);
        * x and y are both caused by z (common causation);
        * There is no connection between x and y; the correlation is a coincidence.

      * Correlations are standardised to vary between -1 and +1, with 0 representing no relationship, -1 a perfect negative relationship, and +1 a perfect positive relationship.
        
  * Different Types of Comparisons:
    * Univariate - looking at one variable
    * Bivariate - looking at 2 variables
    * Multivariate - looking at multiple variables (3-D)

      * Uni-variate (skipped - pie chart and bar chart) -- plot histograms to confirm normal distribution before performing correlation plots

        * Categorical data
          * bar (get counts of each category)
          * pie (get normalized counts- count divided by whole pop)
          * line (counts of categories over time)

        * Continuous data
        *   histogram (group continuous data and get count of groups)
        *   line (conversion rate over time)
        *   violin (density of quantile distribution (3-D/kde version of boxplot))

      * Bi-variate (x vs other predictor/target variable)

        * Nominal by Nominal: Contingency table, Pearson's chi-square test, Phi/Cramer's V --> Clustered bar charts
        * Ordinal by Ordinal: Spearman's rho, Kendall's tau-b --> Scatterplot (with point bins)
        * Dichotomous by Interval/Ratio: Point biserial correlation coefficient --> Scatterplot
        * Interval/Ratio by interval/ratio: Pearson product-moment correlation coefficient --> (x, y vs z)

    * Remember that correlation does not prove causation. Relationship between two variables may be caused by third variable. And this is why multivariate analysis is important.

<img width="1858" alt="Screenshot 2025-01-11 at 1 12 18 PM" src="https://github.com/user-attachments/assets/360b1401-80cc-45b7-99eb-7c92dbab7018" />

# Advanced

Let me outline advanced visualization principles from both books and apply them specifically to Sephora's analytics needs:

1. **Visual Hierarchy and Purpose-Driven Design**
   - Start with clear business questions:
     - "How does AI investment impact customer lifetime value?"
     - "Which customer segments drive omnichannel growth?"
     - "What's the relationship between virtual try-ons and purchase conversion?"
   - Organize metrics in a logical flow from strategic to tactical
   - Use size and positioning to emphasize key performance drivers

2. **Advanced Comparative Techniques**
   - Small Multiples for Store Performance
     - Grid of sparklines showing sales trends across regions
     - Consistent scale for easy comparison
     - Color highlighting for stores exceeding/missing targets

3. **Sophisticated Color Usage**
   - Strategic Color Application:
     - Reserved colors (like Sephora's black/white) for branding
     - Alert colors only for actionable metrics
     - Color intensity mapping to customer loyalty scores
   - Accessibility-First Design:
     - Colorblind-friendly palette for segment analysis
     - Pattern fills for additional visual encoding

4. **Context-Rich Visualization**
   - Bullet Charts for KPIs:
     - Current performance vs targets
     - Historical range bands
     - Year-over-year comparison
   - Reference Lines:
     - Industry benchmarks
     - Seasonal expectations
     - Pre/post promotion baselines

5. **Advanced Chart Types for Complex Relationships**
   - Sankey Diagrams:
     - Customer journey flows
     - Product category relationships
     - Cross-sell patterns
   - Horizon Charts:
     - Long-term trend analysis
     - Seasonal pattern detection
     - Multiple metrics in compact space

6. **Interactive Depth**
   - Progressive Disclosure:
     - Top-level metrics with drill-down capability
     - Tooltips with contextual insights
     - Linked views for cross-filtering
   - Custom Interactions:
     - Brush and zoom for time periods
     - Lasso select for segment analysis
     - Dynamic reference lines

7. **Spatial and Temporal Analysis**
   - Calendar Heatmaps:
     - Daily sales patterns
     - Promotion effectiveness
     - Staffing optimization
   - Geographic Analysis:
     - Store performance maps
     - Market penetration
     - Competition analysis

8. **Advanced Metric Combinations**
   - Composite Indicators:
     - Customer health score
     - Store efficiency index
     - Product performance rating
   - Derived Metrics:
     - Sales velocity
     - Customer acquisition cost
     - Lifetime value prediction

9. **Actionable Insights Design**
   - Exception Highlighting:
     - Automated anomaly detection
     - Threshold alerts
     - Trend breakpoints
   - Prescriptive Elements:
     - Next best action recommendations
     - Risk indicators
     - Opportunity signals

10. **Layout Innovation**
    - Trellis Displays:
      - Product category performance
      - Channel comparison
      - Time series decomposition
    - Linked Small Multiples:
      - Connected views of related metrics
      - Coordinated highlighting
      - Consistent scales

## [Implemented advanced visualization](http://192.168.1.250:8501)
### [Python Script](https://github.com/mindyng/2025-Business-Projects/blob/main/adv_sephora_dash.py)

Key features of this advanced dashboard:

1. **Sophisticated Analysis Options**
   - Multiple analysis types (Performance, Customer Behavior, Digital Engagement, Anomaly Detection)
   - Interactive controls for analysis parameters
   - Advanced filtering options

2. **Advanced Visualizations**
   - Composite charts with multiple visualization types
   - Interactive anomaly detection
   - Customer segment bubble charts
   - Digital engagement funnels

3. **Enhanced Interactivity**
   - Dynamic date range selection
   - Segment filtering
   - Adjustable analysis parameters
   - Expandable insights section

4. **Performance Optimization**
   - Cached data loading
   - Efficient data structures
   - Optimized chart rendering
   - 
<img width="1779" alt="Screenshot 2025-01-14 at 12 05 24 PM" src="https://github.com/user-attachments/assets/2addfa30-b353-426c-9212-bf317135dc69" />


