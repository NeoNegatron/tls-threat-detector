import pandas as pd

df = pd.read_csv("../data/parsed_ssl.csv")
df['label'] = 0
df.to_csv("../data/labeled_parsed_ssl.csv", index=False)

print("[✓] Saved labeled benign TLS.")


