import pandas as pd
import joblib

# Load model and training feature columns
model = joblib.load("../models/tls_threat_model.pkl")
train_features = joblib.load("../models/training_features.pkl")

# Load parsed TLS log from new pcap (e.g., warmcookie)
df = pd.read_csv("../data/warmcookie_tls_log.csv")

# Drop columns that were excluded during training
df = df.drop(columns=[
    'ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h',
    'id.resp_p', 'server_name', 'cert_chain_fps',
    'client_cert_chain_fps', 'ssl_history'
], errors='ignore')

# One-hot encode
df = pd.get_dummies(df)

# Align with training features
for col in train_features:
    if col not in df.columns:
        df[col] = 0
df = df[train_features]

# Run prediction
df['predicted_label'] = model.predict(df)

# Save results
df.to_csv("../data/predicted_tls_results.csv", index=False)
print("[✓] Inference complete. Results saved to predicted_tls_results.csv")

