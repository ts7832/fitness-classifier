import gradio as gr
import numpy as np
import joblib

# Min-max values from the training dataset for scaling (update if retrained)
MIN_MAX_VALUES = {
    "age": (18, 79),
    "height_cm": (150, 199),
    "weight_kg": (30, 250),
    "heart_rate": (45.0, 107.1),
    "blood_pressure": (90.0, 156.6),
    "sleep_hours": (4.0, 11.5),
    "nutrition_quality": (0.0, 10.0),
    "activity_index": (1.0, 5.0),
}

# Model names and paths
MODEL_PATHS = {
    "Logistic Regression": "./models/LogisticRegression.joblib",
    "Decision Tree": "./models/DecisionTreeClassifier.joblib",
    "Random Forest": "./models/RandomForestClassifier.joblib",
    "Gradient Boosting": "./models/GradientBoostingClassifier.joblib",
    "XGBoost": "./models/XGBClassifier.joblib",
}


def predict_fitness(
    model_name,
    age,
    height_cm,
    weight_kg,
    heart_rate,
    blood_pressure,
    sleep_hours,
    nutrition_quality,
    activity_index,
    smokes,
    gender,
):
    # Input validation
    if (
        age < 0
        or height_cm < 0
        or weight_kg < 0
        or heart_rate < 0
        or blood_pressure < 0
        or sleep_hours < 0
    ):
        return "Invalid input: values cannot be negative."
    if not (0 <= nutrition_quality <= 10):
        return "Nutrition quality must be between 0 and 10."
    if not (1 <= activity_index <= 5):
        return "Activity index must be between 1 and 5."

    # Scale numerical input to 0-1 using MIN_MAX_VALUES
    num_features = [
        ("age", age),
        ("height_cm", height_cm),
        ("weight_kg", weight_kg),
        ("heart_rate", heart_rate),
        ("blood_pressure", blood_pressure),
        ("sleep_hours", sleep_hours),
        ("nutrition_quality", nutrition_quality),
        ("activity_index", activity_index),
    ]
    scaled = []
    for key, val in num_features:
        min_v, max_v = MIN_MAX_VALUES[key]
        scaled.append((val - min_v) / (max_v - min_v))
    scaled.append(smokes)
    scaled.append(gender)
    input_data = np.array([scaled])

    # Load model
    model_path = MODEL_PATHS.get(model_name)
    if model_path is None:
        return "Model not found."
    try:
        model = joblib.load(model_path)
    except Exception as e:
        return f"Error loading model: {e}"

    # Predict
    try:
        pred = model.predict(input_data)[0]
    except Exception as e:
        return f"Prediction error: {e}"

    return "Fit" if pred == 1 else "Not Fit"


# Gradio UI

with gr.Blocks() as demo:
    gr.Markdown("# Fitness Classification Predictor")
    gr.Markdown("Select a model and enter the person's data to predict fitness status.")
    gr.Markdown(
        "**Note:** For best results, use values within the specified min and max for each field. Predictions outside these ranges may be unreliable."
    )

    with gr.Row():
        model_choice = gr.Dropdown(
            list(MODEL_PATHS.keys()), label="Select Model", value="XGBoost"
        )

    with gr.Row():
        age = gr.Number(
            label="Age (years)", minimum=0, step=1, value=30, info="Min: 18, Max: 79."
        )
        height_cm = gr.Number(
            label="Height (cm)", minimum=0, value=170, info="Min: 150, Max: 199."
        )
        weight_kg = gr.Number(
            label="Weight (kg)", minimum=0, value=70, info="Min: 30, Max: 250."
        )
    with gr.Row():
        heart_rate = gr.Number(
            label="Heart Rate (bpm)",
            minimum=0,
            value=70,
            info="Min: 45.0, Max: 107.1.",
        )
        blood_pressure = gr.Number(
            label="Blood Pressure (mmHg)",
            minimum=0,
            value=120,
            info="Min: 90.0, Max: 156.6.",
        )
        sleep_hours = gr.Number(
            label="Sleep Hours (per day)",
            minimum=0,
            maximum=24,
            value=8,
            info="Min: 4.0, Max: 11.5.",
        )
    with gr.Row():
        nutrition_quality = gr.Slider(
            0, 10, step=0.1, label="Nutrition Quality (0-10)", value=5
        )
        activity_index = gr.Slider(
            1, 5, step=0.1, label="Activity Index (1-5)", value=3
        )
    with gr.Row():
        smokes = gr.Radio([0, 1], label="Smokes?", value=0, info="0 = No, 1 = Yes")
        gender = gr.Radio([0, 1], label="Gender", value=0, info="0 = Male, 1 = Female")

    predict_btn = gr.Button("Predict Fitness")
    output = gr.Textbox(label="Prediction Result")

    predict_btn.click(
        predict_fitness,
        inputs=[
            model_choice,
            age,
            height_cm,
            weight_kg,
            heart_rate,
            blood_pressure,
            sleep_hours,
            nutrition_quality,
            activity_index,
            smokes,
            gender,
        ],
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()
