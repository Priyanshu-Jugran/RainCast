# RainCast
RainCast is a Python-based machine learning project that predicts whether it will rain tomorrow in Australia using a Gaussian Naive Bayes classifier trained on historical weather data from the WeatherAUS dataset.  
The project demonstrates an end-to-end workflow: data preprocessing, model training and evaluation, model serialization, and a desktop GUI for interactive rainfall prediction.  

------------------------------------------------
1. Project Overview
------------------------------------------------

The main goal of RainCast is to build a simple yet effective binary classification model that predicts the "RainTomorrow" label (Yes/No) from daily weather observations.  
It focuses on a subset of readily interpretable numerical features and encodes rainfall indicators into numeric form so they can be used directly by the Naive Bayes algorithm.  
On top of the trained model, a lightweight GUI built with Tkinter allows users to manually input current weather conditions and instantly see whether rain is expected the next day.  

------------------------------------------------
2. Dataset
------------------------------------------------

The project uses the public WeatherAUS dataset (`weatherAUS.csv`), which contains daily weather records for multiple Australian locations, including temperatures, rainfall, humidity, pressure, and other meteorological attributes.  
For simplicity and clarity, the project narrows the dataset down to the following columns that are most relevant to short-term rainfall prediction:  

- MinTemp  
- MaxTemp  
- Rainfall  
- Humidity9am  
- Humidity3pm  
- RainToday  
- RainTomorrow  

The target variable is `RainTomorrow`, which indicates whether it rained the following day and is converted from "Yes"/"No" to `1`/`0` during preprocessing.  
The `RainToday` feature is also encoded as `1` (Yes) or `0` (No) and used as an important leading indicator for next-day rainfall.  

------------------------------------------------
3. Code Structure
------------------------------------------------

A typical layout of the RainCast project looks like this:  

- `weatherAUS.csv` – raw input dataset.  
- `weatherDataset.csv` – cleaned and preprocessed dataset generated from the raw CSV.  
- `dataset_prep.py` – script for selecting required columns, encoding labels, and handling missing values.  
- `model_training.py` – script that trains and evaluates the Gaussian Naive Bayes model and saves it to disk.  
- `raincast.py` – Tkinter-based GUI application that loads the trained model and provides interactive predictions.  
- `README` / `README.txt` – documentation describing how to install, run, and understand the project.  

This straightforward structure makes it easy to follow the data path from the raw CSV through to the final user-facing interface.  

------------------------------------------------
4. Data Preprocessing (dataset_prep.py)
------------------------------------------------

The preprocessing workflow is implemented in `dataset_prep.py`, which reads the raw `weatherAUS.csv` file using pandas.  
Only the necessary columns are retained: `MinTemp`, `MaxTemp`, `Rainfall`, `Humidity9am`, `Humidity3pm`, `RainToday`, and `RainTomorrow`, reducing noise and focusing on the most useful features.  
The categorical rainfall indicators `RainToday` and `RainTomorrow` are mapped from "Yes"/"No" strings to numeric values `1` and `0`, making them suitable as model input and output.  
Rows containing missing values in any of these selected columns are dropped to ensure the training data is complete and consistent.  
Finally, the cleaned dataset is saved as `weatherDataset.csv`, which becomes the primary input for the training script.  

Typical command to run preprocessing:  

    python dataset_prep.py  

------------------------------------------------
5. Model Training and Evaluation (model_training.py)
------------------------------------------------

The `model_training.py` script is responsible for building and assessing the prediction model using scikit-learn.  
It loads the cleaned `weatherDataset.csv`, separates the target column `RainTomorrow` from the feature columns, and then performs an 80/20 train–test split using `train_test_split`.  
The chosen model is `GaussianNB` (Gaussian Naive Bayes), which assumes that each feature is normally distributed and conditionally independent given the class label.  
The model is trained on the training set, and predictions are generated for the test set to evaluate performance.  
Key evaluation metrics are printed, including overall accuracy and a full classification report with precision, recall, and F1-score for both "rain" and "no rain" classes.  

From a sample training run, the project documents results similar to:  

- Accuracy around 80% on the test set.  
- High precision and recall for the "No rain" class.  
- Lower recall for the "Rain" class due to class imbalance, where non-rainy days are more common.  

The script also demonstrates a single hard-coded sample prediction to verify that the trained model can successfully predict based on numeric input.  
After training, the model is serialized and saved to disk using `joblib.dump` under the filename `NBTmodel.joblib`.  

Typical command to train the model:  

    python model_training.py  

------------------------------------------------
6. GUI Application for Prediction (raincast.py)
------------------------------------------------

The `raincast.py` file implements a desktop application using Tkinter, the standard GUI toolkit included with Python.  
On startup, it loads the previously saved `NBTmodel.joblib` model so that the GUI can immediately perform predictions without retraining.  
The interface consists of labeled input fields where the user can enter numeric values for: MinTemp, MaxTemp, Rainfall, Humidity at 9AM, Humidity at 3PM, and Rain Today (as 0 or 1).  
When the user clicks the "Predict" button, these values are collected from the input widgets, converted to a one-row pandas DataFrame with the same column order used during training, and passed to the model’s `predict` method.  
The result is displayed in a message box indicating whether it will rain tomorrow, usually expressed as a clear "Yes" or "No" answer.  

The app includes simple error handling to catch invalid or non-numeric input and display an appropriate error message to the user.  

Typical command to launch the GUI:  

    python raincast.py  

------------------------------------------------
7. Technologies Used
------------------------------------------------

- Python 3 – main programming language for the scripts and GUI.  
- pandas – used for reading CSV files, selecting and transforming columns, and writing cleaned datasets.  
- scikit-learn – provides `train_test_split`, `GaussianNB`, and evaluation metrics like accuracy and classification reports.  
- joblib – used to serialize and load the trained Naive Bayes model efficiently.  
- Tkinter – built-in Python GUI toolkit used to create the desktop interface for rainfall prediction.  

These widely-used libraries make the project easy to extend and understand for anyone familiar with the Python data science ecosystem.  

------------------------------------------------
8. How to Run the Project
------------------------------------------------

1. Ensure Python 3 and the required libraries (pandas, scikit-learn, joblib) are installed in your environment.  
2. Place `weatherAUS.csv` in the project directory alongside the scripts.  
3. Run `dataset_prep.py` to generate `weatherDataset.csv` from the raw data.  
4. Run `model_training.py` to train the Gaussian Naive Bayes model and create `NBTmodel.joblib`.  
5. Finally, run `raincast.py` to open the GUI and start making interactive rainfall predictions.  

Each step is independent and can be re-run if the dataset is updated or if you wish to retrain the model with different preprocessing or parameters.  

------------------------------------------------
9. Limitations and Possible Improvements
------------------------------------------------

Because the model uses only a limited subset of features and a relatively simple Naive Bayes algorithm, its performance, especially for predicting rainy days, may not match more complex models trained on the full dataset.  
The class imbalance in the WeatherAUS data (more dry days than rainy days) leads to lower recall for rain predictions, meaning some rainy days may be misclassified as dry.  

Potential enhancements include:  

- Incorporating additional features such as wind, pressure, or cloud cover to capture more information.  
- Applying resampling or class weights to address class imbalance and improve rainy-day detection.  
- Trying alternative algorithms like Logistic Regression, Random Forests, or Gradient Boosting to compare accuracy and robustness.  
- Adding visualizations or logging to better understand feature importance and model behavior.  
- Improving the GUI with validation, better layout, theming, and packaging as a standalone executable.  

------------------------------------------------
10. Author and Credits
------------------------------------------------

This project is designed as an educational and practical example of end-to-end rainfall prediction using Python and Naive Bayes.  
By Priyanshu Jugran.

The WeatherAUS dataset and similar resources are typically credited to the Australian Bureau of Meteorology and the open data community that curates and republishes them.  

