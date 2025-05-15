# 🎬 Movie Recommendation System using KNN Algorithm

## 📚 Title
**Movie Recommendation System Based on Genre and Title Similarity using K-Nearest Neighbors**

## 👨‍💻 Team Members

| Name             | Roll Number     |
|------------------|-----------------|
| Jay Pachchigar    | U22EC033       |
| Pankaj Vaniya        | U22EC055        |
| Raghav Khatri       | U22EC060        |

## 📝 Project Overview

This project presents a content-based **Movie Recommendation System** developed using the **K-Nearest Neighbors (KNN)** algorithm. It analyzes the **genres** and **titles** of movies from the `movies.csv` dataset to suggest similar movies based on user input.

The application frontend is built with **React Native and Expo**, and the model is deployed using **Render.com**.

---

## 🚀 Features

- 🔍 **Search & Autocomplete**: Users can search for any movie with live autocomplete suggestions.
- 🎯 **KNN-based Recommendations**: Similar movies are recommended based on genre and title similarity.
- 📊 **TF-IDF Vectorization**: Movie metadata is transformed using TF-IDF for accurate similarity computation.
- 📱 **Mobile Friendly**: Built using React Native and Expo for a seamless mobile experience.
- ☁️ **Deployed on Render**: Backend and model hosted live for real-time responses.

---

## 🧠 Tech Stack

### 🖥️ Frontend
- React Native
- Expo
- Axios

### 🧪 Backend & ML
- Python
- Scikit-learn
- Pandas
- SciPy
- TfidfVectorizer
- K-Nearest Neighbors (KNN)

### 🗃️ Dataset
- `movies.csv` (containing movie titles and genres)

### ☁️ Deployment
- **Model & API**: Hosted on [Render.com](https://render.com)

---


---

## 🔧 How It Works

1. Load and preprocess movie data from `movies.csv`.
2. Use **TF-IDF** to vectorize the `genres` and `title` columns.
3. Combine the vectors and normalize the matrix.
4. Fit the **K-Nearest Neighbors** model using cosine similarity.
5. On user input, return top-N similar movie titles excluding the input itself.

---

## 🛠️ Installation & Setup

### Backend (Python + Render)

1. Place `movies.csv` and `knn_model.py` in a folder.
2. Create a Flask or FastAPI wrapper (optional) to serve recommendations.
3. Deploy to [Render](https://render.com).

### Frontend (React Native + Expo)


npm install             
npx expo start

## 🙌 Acknowledgments

- The **MovieLens dataset** for providing the movie metadata.
- **Scikit-learn** for machine learning tools.
- **Render** for free deployment services.
- **Expo** and **React Native** for a seamless development experience.

---

## 📎 Links

- 🔗 **Live Model API**: [Render App](https://your-render-link.com)
- 📱 **Frontend App**: Accessible via **Expo Go** or physical device using the QR code

## 📎 Links



- 📱 **[App Download Link](https://drive.google.com/file/d/1_lqKxe57jA0G3o7kkxO2IMYs50Pc0pOW/view?usp=sharing)**
- 🎥 **[Working Video Demo](https://drive.google.com/file/d/1RaAhfgDoUoT397mk2VAh_Fx4px9d9Vgi/view?usp=sharing)**
---

## 📁 Folder Structure & File Overview

```bash
.
├── assets/                 # Stores static files like images or fonts used by the frontend
├── components/            # React Native components (UI elements used in App.js)
├── .gitignore             # Specifies intentionally untracked files to ignore by Git
├── App.js                 # Entry point of the React Native application (renders UI)
├── app.json               # Expo configuration file for the React Native app
├── eas.json               # EAS (Expo Application Services) build configuration
├── index.js               # Root file for registering the main React Native app
├── package.json           # Project dependencies and scripts for the React Native app
├── package-lock.json      # Exact versions of dependencies used (ensures reproducible builds)
├── Procfile               # For deploying the app using platforms like Heroku (defines web process)
├── README.md              # Project documentation and overview
├── knn_model.py           # Core Python script implementing the KNN algorithm for movie recommendations
├── main.py                # Backend server script (likely using Flask/FastAPI) to handle requests from frontend
├── movies.csv             # Dataset containing movie information (title, genre, etc.)
├── requirements.txt       # Python dependencies required for the backend
