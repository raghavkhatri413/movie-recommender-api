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

---

## 🤝 Contributing

This is a **team submission for academic purposes**.

For improvements or future extensions, feel free to fork and enhance the project!
