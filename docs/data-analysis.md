## Chapter: Exploratory Data Analysis Results

This chapter presents the main findings from the exploratory data analysis (EDA) performed on the fitness dataset. The analysis was conducted using Python libraries such as pandas, matplotlib, and seaborn, and focused on understanding the structure, distribution, and relationships within the data.

### 1. Data Overview

The dataset contains several features related to individual health and lifestyle, including age, height, weight, heart rate, blood pressure, sleep hours, nutrition quality, activity index, smoking status, and gender. The target variable is `is_fit`, indicating overall fitness status.

### 2. Data Cleaning

- All rows with missing values in the main input columns were removed to ensure data quality.
- The `smokes` attribute was standardized to binary values (1 for "yes", 0 for "no").

### 3. Numerical Attribute Analysis

For each numerical attribute (age, height, weight, heart rate, blood pressure, sleep hours, nutrition quality, activity index), descriptive statistics were computed and distributions visualized:

- Most attributes showed reasonable distributions, with some skewness in variables like activity index and nutrition quality.
- Histograms and kernel density plots revealed the spread and central tendency of each feature.
- **Evenly Distributed Attributes:** Features such as age, height, nutrion quality and activity index exhibited relatively even distributions across their ranges, indicating a balanced representation of values without significant clustering or gaps.
- **Normally Distributed Attributes:** Weight, heart rate, blood pressure and sleep hours approximated a normal (bell-shaped) distribution, as shown by their histograms and density plots, suggesting most values are concentrated around the mean with symmetric tails.

### 4. Categorical Attribute Analysis

- **Smoking Status:** The majority of individuals in the dataset are non-smokers. Bar plots were used to visualize the distribution.
- **Gender:** The dataset contains both male and female participants, with a slight imbalance between the two groups.

### 5. Target Attribute Analysis

- The `is_fit` variable was analyzed to understand the proportion of fit vs. non-fit individuals. The dataset contains both classes, with a distribution visualized using bar plots.

### 6. Correlation Analysis

- A correlation matrix was computed (with gender and smokes encoded as a binary variable) to examine relationships between features and the target variable.
- The heatmap visualization highlighted the strength and direction of correlations. Some features, such as activity index and nutrition quality, showed stronger correlations with fitness status.

### 7. Key Insights

- Data cleaning and preprocessing are crucial for reliable analysis.
- Certain features, especially activity index and nutrition quality, may be important predictors of fitness.
- The dataset is suitable for further modeling and predictive analysis, given the diversity and quality of the features.

---

This chapter summarizes the main EDA steps and findings. For detailed code and visualizations, refer to the accompanying Jupyter notebook.
