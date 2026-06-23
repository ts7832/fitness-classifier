# Fitness Classification User Interface Guide

This document describes how to use the Fitness Classification Predictor web interface, which allows you to select a machine learning model and input personal health data to predict whether a person is classified as "Fit" or "Not Fit".

## Accessing the Interface

Run the application with:

```bash
python main.py
```

This will launch a Gradio web interface in your browser.

## Model Selection

- **Select Model:** Use the dropdown menu to choose from available models:
	- Logistic Regression
	- Decision Tree
	- Random Forest
	- Gradient Boosting
	- XGBoost

## Input Fields

Enter the following information for the person you want to classify:

| Field               | Type      | Range/Options         | Description                                                                 |
|---------------------|-----------|----------------------|-----------------------------------------------------------------------------|
| Age (years)         | Number    | 18 - 79              | Person's age. Values outside this range may yield unreliable predictions.    |
| Height (cm)         | Number    | 150 - 199            | Person's height in centimeters.                                             |
| Weight (kg)         | Number    | 30 - 250             | Person's weight in kilograms.                                               |
| Heart Rate (bpm)    | Number    | 45.0 - 107.1         | Resting heart rate in beats per minute.                                     |
| Blood Pressure      | Number    | 90.0 - 156.6         | Systolic blood pressure in mmHg.                                            |
| Sleep Hours         | Number    | 4.0 - 11.5           | Average hours of sleep per day.                                             |
| Nutrition Quality   | Slider    | 0.0 - 10.0           | Subjective nutrition quality (0 = poor, 10 = excellent).                    |
| Activity Index      | Slider    | 1.0 - 5.0            | Physical activity level (1 = low, 5 = high).                                |
| Smokes?             | Radio     | 0 = No, 1 = Yes      | Whether the person smokes.                                                  |
| Gender              | Radio     | 0 = Male, 1 = Female | Person's gender.                                                            |

**Note:** For best results, use values within the specified min and max for each field. Predictions outside these ranges may be unreliable.

## Making a Prediction

1. Fill in all required fields with the person's data.
2. Click the **Predict Fitness** button.
3. The result will appear in the Prediction Result box, showing either "Fit" or "Not Fit".

## Tips

- All numerical fields must be non-negative.
- If you enter a value outside the recommended range, the prediction may not be reliable.
- You can quickly test different models and see how predictions change for the same input.

---

For more details on the models and data processing, see the other documentation files in this project.
