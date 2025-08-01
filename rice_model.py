# rice_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# 1. Load data
df = pd.read_excel("Crop_recommendation.xlsx")
df_rice = df[df['label'] == 'rice'].copy()

# 2. Select features and preprocess
numerical_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
X = df_rice[numerical_cols].values
y = np.ones(len(df_rice))  # Assume all samples are high-yield for demo

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 4. Build a simple model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X.shape[1],)),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer=Adam(0.001), loss='binary_crossentropy', metrics=['accuracy'])

# 5. Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)

# 6. Define prediction function
def predict_rice_yield(input_data):
    input_array = np.array([[
        input_data['N'],
        input_data['P'],
        input_data['K'],
        input_data['temperature'],
        input_data['humidity'],
        input_data['ph'],
        input_data['rainfall']
    ]])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled, verbose=0)[0][0]
    return 'Yes' if prediction > 0.5 else 'No'
