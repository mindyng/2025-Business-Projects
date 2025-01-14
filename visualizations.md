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

# Advanced
