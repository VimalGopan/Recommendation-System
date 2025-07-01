# 🛍️ Product Recommendation System

A machine learning-powered recommendation engine that suggests products based on user ratings using **collaborative filtering** (SVD). Built with **Python**, **Flask**, **HTML/CSS/JS**, and real-world e-commerce data.

---

## 📌 Features

- 🔄 Random product selector
- ✅ Recommendations based on user-product interaction
- 💡 Collaborative filtering via Truncated SVD
- 🖥️ Interactive UI using HTML/CSS and JavaScript
- ⚙️ Flask-based backend
- 📊 Product names mapped dynamically with ID

---

## 🧠 How It Works

1. **Data Preprocessing**  
   - Loaded and cleaned 20k+ user ratings
   - Mapped product IDs to meaningful names
   - Created a utility matrix (User vs Product)

2. **Model**  
   - Applied Truncated SVD for matrix decomposition
   - Built a product-product similarity matrix using correlation

3. **Web App (Flask)**  
   - Random product grid UI
   - Recommend products with >90% similarity
   - Dynamic UI interaction (highlight, recommendation list)

---

## 🛠️ Tech Stack

| Layer        | Tools Used                       |
|--------------|----------------------------------|
| Language     | Python 3                         |
| Backend      | Flask                            |
| Frontend     | HTML, CSS, JavaScript            |
| ML Model     | Scikit-learn (Truncated SVD)     |
| Data Handling| Pandas, NumPy                    |
| Deployment   | Localhost / (Optional: Render, AWS, Heroku) |

---

## 📷 Screenshots

> Add a few screenshots or GIFs of:
- Random products grid
- Recommendations after clicking a product
- Flask terminal output (optional)

---

## 📁 Folder Structure
product-recommender/
│
├── app.py                  # 🔥 Flask application entry point
├── model.py                # 🧠 SVD-based recommendation engine
├── Beauty.csv              # 📊 Ratings dataset (UserId, ProductId, Rating)
│
├── static/                 # 🎨 Static assets
│   ├── favicon.ico         #    → Navigate icon
│
├── templates/              # 🖼️ HTML templates
│   └── index.html          #    → UI layout for the web app
│
├── images/                 # 📷 Screenshots or visuals for README
│   ├── webpage_before.png
│   └── webpage_after.png
│
└── README.md               # 📘 Project documentation


---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/product-recommender
cd product-recommender
pip install -r requirements.txt
python app.py

