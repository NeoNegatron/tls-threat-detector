import pandas as pd

# Load labeled CSVs
benign = pd.read_csv("../data/labeled_parsed_ssl.csv")
malicious = pd.read_csv("../data/labeled_malicious_tls.csv")

# Combine and shuffle
combined = pd.concat([benign, malicious]).sample(frac=1).reset_index(drop=True)

# Save final dataset
combined.to_csv("../data/final_tls_dataset.csv", index=False)
print("[✓] Saved final TLS dataset with shape:", combined.shape)

