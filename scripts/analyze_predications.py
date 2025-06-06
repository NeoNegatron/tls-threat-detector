import pandas as pd

df = pd.read_csv("../data/predicted_tls_results.csv")
print("[✓] Prediction Summary:")
print(df['predicted_label'].value_counts())


