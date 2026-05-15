# MLP Letter Classifier – FastAPI + Nginx + HTTPS Deployment

A simple machine learning API that predicts handwritten letters (A–Z) based on 16 numerical features.
The project includes:

- FastAPI backend (MLP classifier)
- Static frontend (HTML/JS)
- Nginx reverse proxy
- Full HTTPS deployment using Let's Encrypt
- Public demo available online

---

## 🚀 Live Demo

You can test the model directly in your browser:

👉 **https://api.doomiiniik.dev/**

The page allows you to paste a 16‑element feature vector and get a predicted letter.

---

## 🧪 Example Input Records

You can use these ready-made examples to test the model:

[8, 10, 6, 7, 2, 3.1, 2.7, 4.8, 3.6, 0.8, 1.9, 2.7, 6, 4, 7, 5]

[3, 7, 4, 5, 1, 1.7, 2.3, 3.2, 2.8, 0.6, 1.1, 2.0, 4, 3, 5, 4]

[5, 12, 7, 9, 3, 2.8, 3.4, 5.6, 4.9, 1.2, 2.3, 3.8, 7, 5, 8, 6]


---

## 📡 API Endpoint

### **POST /v1/predict**

**Request body:**
```json
{
  "features": [16 numerical values...]
}


{
  "predicted_class": "A",
  "probabilities": { ... }
}
```



🏗️ Architecture Overview

    FastAPI serves the ML model on 127.0.0.1:8000

    Nginx handles:

        HTTPS termination

        Reverse proxy for /v1/, /docs, /openapi.json

        Serving the frontend

    Let's Encrypt provides automatic SSL certificate renewal

    Frontend communicates with backend via HTTPS


Client → HTTPS → Nginx → FastAPI → Model


🔧 Technologies Used

    Python / FastAPI

    scikit-learn (MLPClassifier)

    Nginx

    Let's Encrypt (Certbot)

    HTML / JavaScript frontend

    Ubuntu Server



📦 Deployment Notes

    Backend runs locally behind Nginx

    HTTPS is fully automated via Certbot

    Frontend is served directly from /var/www/

    No mixed-content issues (full HTTPS stack)


👤 Author

Dominik
Project built for portfolio & ML deployment practice.
