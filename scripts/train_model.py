import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load labeled TLS dataset
df = pd.read_csv("../data/final_tls_dataset.csv")

# Drop non-informative or non-ML-friendly columns
df = df.drop(columns=[
    'ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h',
    'id.resp_p', 'server_name', 'cert_chain_fps',
    'client_cert_chain_fps', 'ssl_history'
], errors='ignore')

# One-hot encode categorical columns
df = pd.get_dummies(df)

# Separate features and target
X = df.drop(columns=['label'])
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n[✓] Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/tls_threat_model.pkl")

#Save feature columns
joblib.dump(list(X.columns), "../models/training_features.pkl")
print("[✓] Models and features saved")


