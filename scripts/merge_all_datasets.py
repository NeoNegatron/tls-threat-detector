import pandas as pd

# Load all labeled TLS datasets
benign = pd.read_csv("../data/labeled_parsed_ssl.csv")
hydra = pd.read_csv("../data/labeled_malicious_tls.csv")
warmcookie = pd.read_csv("../data/labeled_warmcookie.csv")

# Combine & shuffle
combined = pd.concat([benign, hydra, warmcookie])
combined = combined.sample(frac=1).reset_index(drop=True)

# Save merged dataset
combined.to_csv("../data/final_tls_dataset.csv", index=False)
print(f"[✓] Final dataset created: {combined.shape[0]} records saved.")


