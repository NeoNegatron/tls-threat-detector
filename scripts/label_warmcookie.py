import pandas as pd

# Load parsed log from WarmCookie PCAP
df = pd.read_csv("../data/warmcookie_tls_log.csv")
df['label'] = 1  # 1 = malicious

# Save labeled dataset
df.to_csv("../data/labeled_warmcookie.csv", index=False)
print("[✓] Labeled WarmCookie TLS data saved.")


