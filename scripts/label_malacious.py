import pandas as pd

df = pd.read_csv("../data/parsed_tls.csv")
df['label'] = 1
df.to_csv("../data/labeled_malicious_tls.csv", index=False)

print("[✓] Saved labeled malicious TLS.")

