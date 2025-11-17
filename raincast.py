import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

# Load your trained model
model = joblib.load('NBTmodel.joblib')

# Required column names
columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Humidity9am', 'Humidity3pm', 'RainToday']

# Function to predict rain
def predict_rain():
    try:
        # Get input values from Entry widgets
        min_temp = float(entry_min_temp.get())
        max_temp = float(entry_max_temp.get())
        rainfall = float(entry_rainfall.get())
        humidity9am = float(entry_humidity9am.get())
        humidity3pm = float(entry_humidity3pm.get())
        rain_today = int(entry_rain_today.get())  # Should be 0 or 1

        # Create DataFrame for prediction
        input_df = pd.DataFrame([[min_temp, max_temp, rainfall, humidity9am, humidity3pm, rain_today]],
                                columns=columns)

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Show result
        result = "Yes 🌧️" if prediction == 1 else "No ☀️"
        messagebox.showinfo("Prediction", f"Will it rain tomorrow?\n{result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Initialize GUI
root = tk.Tk()
root.title("Rain Tomorrow Prediction")

# Labels and Entry fields
tk.Label(root, text="MinTemp").grid(row=0, column=0)
entry_min_temp = tk.Entry(root)
entry_min_temp.grid(row=0, column=1)

tk.Label(root, text="MaxTemp").grid(row=1, column=0)
entry_max_temp = tk.Entry(root)
entry_max_temp.grid(row=1, column=1)

tk.Label(root, text="Rainfall").grid(row=2, column=0)
entry_rainfall = tk.Entry(root)
entry_rainfall.grid(row=2, column=1)

tk.Label(root, text="Humidity 9AM").grid(row=3, column=0)
entry_humidity9am = tk.Entry(root)
entry_humidity9am.grid(row=3, column=1)

tk.Label(root, text="Humidity 3PM").grid(row=4, column=0)
entry_humidity3pm = tk.Entry(root)
entry_humidity3pm.grid(row=4, column=1)

tk.Label(root, text="Rain Today (1=Yes, 0=No)").grid(row=5, column=0)
entry_rain_today = tk.Entry(root)
entry_rain_today.grid(row=5, column=1)

# Predict Button
tk.Button(root, text="Predict", command=predict_rain).grid(row=6, column=0, columnspan=2, pady=10)

# Run GUI loop
root.mainloop()
