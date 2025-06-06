import pandas as pd
import os

log_path = "../data/ssl.log"  # You're already in the data folder
output_path = "../data/parsed_tls.csv"

columns = [
    'ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p',
    'version', 'cipher', 'curve', 'server_name', 'resumed',
    'last_alert', 'next_protocol', 'established', 'ssl_history',
    'cert_chain_fps', 'client_cert_chain_fps', 'sni_matches_cert'
]

# Read Zeek log with custom column names
df = pd.read_csv(
    log_path,
    sep='\t',
    comment='#',
    names=columns,
    engine='python'
)

# Convert timestamp
df['ts'] = pd.to_datetime(df['ts'], errors='coerce', unit='s')

# Save to CSV
df.to_csv(output_path, index=False)
print(f"[✓] Parsed SSL log saved to {output_path}")

