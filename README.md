
---

## 🏦 Loan Default Prediction App

### 🔗 Live Demo

👉 [Loan Default Prediction App](https://loandefaultprediction-m8ocjvdmbirtcy7np3dzzc.streamlit.app/)

---

### 📘 Overview

This is a **Machine Learning web app** built using **Streamlit** that predicts whether a loan will be **approved or defaulted** based on applicant information such as income, credit history, and education.

The model uses a **Random Forest Classifier**, trained on a loan dataset to provide reliable predictions.

---

### 🧠 Features

* Interactive web UI built with **Streamlit**
* Predicts loan approval/default based on user inputs
* Trained using **Random Forest Classifier**
* Deployed seamlessly using **Streamlit Cloud**
* Clean feature preprocessing and encoding pipeline

---

### 🧩 Tech Stack

| Category      | Tools Used                  |
| ------------- | --------------------------- |
| Language      | Python                      |
| ML Libraries  | scikit-learn, pandas, numpy |
| Visualization | matplotlib, seaborn         |
| Frontend      | Streamlit                   |
| Deployment    | Streamlit Cloud             |

---

### 📊 Dataset

The model was trained using a loan dataset (e.g., from Kaggle’s “Loan Prediction” dataset).
It includes features such as:

* Gender
* Marital Status
* Dependents
* Education
* Employment Type
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Term
* Credit History
* Property Area

Target Variable → `Loan_Status`
(`1` = Approved / `0` = Default Risk)

---

### 🧾 Installation & Setup (Local)

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/loan-default-prediction.git
cd loan-default-prediction
```

#### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

#### 3️⃣ Activate it

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

#### 5️⃣ Run the app locally

```bash
streamlit run app.py
```

---

### 🌐 Deployment (Streamlit Cloud)

1. Push your project to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **“Deploy an app”** → connect your GitHub repo.
4. Select your repo and branch.
5. Set `app.py` as the entry point.
6. Deploy 🎉

---

### 🧠 Example Prediction

| Feature            | Example Input |
| ------------------ | ------------- |
| Gender             | Male          |
| Married            | Yes           |
| Dependents         | 1             |
| Education          | Graduate      |
| Self Employed      | No            |
| Applicant Income   | 5000          |
| Coapplicant Income | 1500          |
| Loan Amount        | 150           |
| Loan Term          | 360           |
| Credit History     | 1             |
| Property Area      | Urban         |

→ ✅ **Prediction:** Loan Approved

---