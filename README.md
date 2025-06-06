# tls-threat-detector
Machine Learning-based TLS Threat Detection

# AI-Powered Encrypted TLS Threat Detection (No Decryption)

## 🔒 Overview

This project demonstrates a machine learning-based framework for detecting malicious TLS-encrypted traffic **without decrypting packet contents**. Built using Python, Zeek, and scikit-learn, it emulates real-world SOC workflows by capturing and analyzing both benign and attack traffic in a virtual lab.

---

## 🎯 Problem Statement

Traditional intrusion detection systems often struggle with threats hidden inside encrypted TLS connections. Decryption is costly, impractical, and introduces privacy risks. This project solves the problem by analyzing **TLS handshake metadata** extracted via Zeek to classify traffic as benign or malicious.

---

## 🛠️ Architecture & Workflow

1. **Traffic Simulation**

   * Benign: Simulated using `curl` to sites like GitHub, Facebook
   * Malicious: Performed attacks using Nmap, Hydra, and real-world malware PCAPs (e.g., WarmCookie)

2. **Packet Capture**

   * Used `tcpdump` to collect `.pcap` files from virtual machines (Kali ↔ Ubuntu)

3. **Log Generation with Zeek**

   * Ran `zeek -C -r <file>.pcap` to generate `ssl.log`

4. **Parsing & Labeling**

   * Parsed `ssl.log` using Python and Pandas
   * Added labels: `0 = benign`, `1 = malicious`

5. **Model Training**

   * Trained a `RandomForestClassifier` using TLS metadata (e.g., version, cipher, curve, resumed, SNI)
   * Achieved **94% detection accuracy**

6. **Inference & Validation**

   * Applied trained model on unseen PCAPs (e.g., WarmCookie)
   * Successfully identified 57/134 flows as malicious ✅

7. **Visualization**

   * Analyzed correlations between TLS versions, cipher suites, and malicious flows using Seaborn

---

## 📊 Sample Visuals

* **TLS Version vs Prediction**
  ![TLS Version](images/tls_version_vs_label.png)

* **Cipher Suite Usage**
  ![Cipher Usage](images/cipher_usage.png)

* **Session Resumption Patterns**
  ![Resumed Sessions](images/resumed_session.png)

---

## 🔍 Key Features

* **No packet decryption** required ✅
* **Real-world attack PCAPs** for training & validation ✅
* Feature engineering from `ssl.log` (Zeek metadata) ✅
* High accuracy with simple model + explainability ✅

---

## 🧪 Tech Stack

* Python 3.13
* Zeek 7.2
* scikit-learn, Pandas, Seaborn, Matplotlib
* VirtualBox, Kali Linux, Ubuntu

---

## 🚀 How to Run

1. Activate your virtualenv:

```bash
source venv/bin/activate
```

2. Run model training:

```bash
python scripts/train_model.py
```

3. Run inference on new TLS logs:

```bash
python scripts/infer_tls_traffic.py
```

4. Generate charts:

```bash
python scripts/visualize_predictions.py
```

---

## 🙋‍♂️ Author

**NeoNegatron** – Cybersecurity Engineer, passionate about encrypted threat detection & SOC automation.

---

## 📄 License

MIT License
