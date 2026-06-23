# Model Evaluation Report

This document summarizes the model evaluation process and results as performed in the `model-evaluation.ipynb` notebook. The workflow includes data preparation, dataset splitting, model selection, evaluation metrics, and final model testing.

## Data Preparation

- The dataset was loaded from `fitness_dataset.csv`.
- All columns were cast to appropriate data types: numerical columns to `float64`, categorical columns to `boolean`.
- Missing values were removed to ensure data quality.
- The `smokes` attribute was mapped to boolean values (`True` for "yes"/"1", `False` for "no"/"0").
- The `gender` attribute was encoded as 0 (Male) and 1 (Female).
- All numerical features were scaled to the [0, 1] range using min-max normalization.

## Dataset Split

- The data was split into input features (`X`) and target (`y = is_fit`).
- The dataset was divided into training (60%), validation (20%), and test (20%) sets using stratified sampling to preserve class balance.

## Tested Models

The following classification models were evaluated:

| Model                  | Description                                 |
|------------------------|---------------------------------------------|
| Logistic Regression    | Linear model for binary classification      |
| Decision Tree          | Tree-based model with max depth 5           |
| Random Forest          | Ensemble of 100 trees, max depth 10         |
| Gradient Boosting      | 100 estimators, learning rate 0.1, depth 3  |
| XGBoost                | 50 estimators, max depth 4                  |

## Evaluation Metrics

Each model was evaluated on the validation set using the following metrics:

- **Accuracy**: Proportion of correct predictions
- **Precision**: Proportion of positive identifications that were correct
- **Recall**: Proportion of actual positives that were identified correctly
- **F1 Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under the ROC curve

## Results Table

Below is a summary table of the validation results for each model. The best value for each metric is highlighted in **bold**.

| Model                |  Accuracy  |  Precision  |  Recall  |  F1 Score  |  ROC-AUC  |
|----------------------|------------|-------------|----------|------------|-----------|
| Logistic Regression  | 0.7908     | 0.7881      | 0.6414   | 0.7072     | **0.8747**    |
| Decision Tree        | 0.7310     | 0.6597      | 0.6552   | 0.6574     | 0.7170    |
| Random Forest        | 0.8016     | 0.8158      | 0.6414   | 0.7181     | 0.8520    |
| Gradient Boosting    | 0.8016     | 0.7903      | 0.6759   | 0.7286     | 0.8518    |
| XGBoost              | **0.8288**     | **0.8417**      | **0.6966**   | **0.7623**     | 0.8511    |


## Best Model Selection
The best model was selected based on having the highest number of best (bolded) metric values across the validation results table. In this analysis, the best model was:

> **XGBoost**

## Final Model Testing Results

The best model was evaluated on the test set to assess its generalization performance. The following metrics were reported:

- **Accuracy**: 0.7554
- **Precision**: 0.7516
- **Recall**: 0.6886
- **F1 Score**: 0.7188
- **ROC-AUC**: 0.8228

The ROC curve for the best model was plotted, showing good separation between classes and confirming the model's effectiveness.

---

This report provides a comprehensive overview of the model evaluation process. For detailed code, refer to the `model-evaluation.ipynb` notebook.
