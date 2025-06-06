import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/predicted_tls_results.csv")

# --- Plot TLS Version Breakdown ---
version_cols = [col for col in df.columns if col.startswith("version_")]
version_df = df[version_cols + ['predicted_label']]
version_df = version_df.groupby('predicted_label').sum().T
version_df.plot(kind="bar", figsize=(8, 5))
plt.title("TLS Version Usage by Predicted Label")
plt.xlabel("TLS Version")
plt.ylabel("Flow Count")
plt.legend(["Benign (0)", "Malicious (1)"], title="Predicted Label")
plt.tight_layout()
plt.show()

# --- Plot Top Cipher Usage ---
cipher_cols = [col for col in df.columns if col.startswith("cipher_")]
cipher_df = df[cipher_cols + ['predicted_label']]
cipher_df = cipher_df.groupby('predicted_label').sum().T
cipher_df.plot(kind="bar", figsize=(12, 6))
plt.title("Cipher Suite Usage by Predicted Label")
plt.xlabel("Cipher")
plt.ylabel("Flow Count")
plt.legend(["Benign (0)", "Malicious (1)"], title="Predicted Label")
plt.tight_layout()
plt.show()

# --- Plot Session Resumption ---
if 'resumed_T' in df.columns:
    resumed_df = df.groupby('predicted_label')[['resumed_T']].sum()
    resumed_df['resumed_F'] = df.groupby('predicted_label')[['resumed_F']].sum()
    resumed_df.T.plot(kind="bar", figsize=(6, 4))
    plt.title("Session Resumption by Predicted Label")
    plt.xlabel("Resumed")
    plt.ylabel("Flow Count")
    plt.legend(["Benign", "Malicious"], title="Predicted Label")
    plt.tight_layout()
    plt.show()
