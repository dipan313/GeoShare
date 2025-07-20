# GeoShare 🌍

**GeoShare** is a Django-based web application that allows users to **generate and share their real-time geolocation** via a unique link. The recipient can view the shared location on a map and see the distance between themselves and the sharer.

---

## 🚀 Features
- 🔗 **Generate Shareable Location Link:** Users can generate a link with their current location.
- 📍 **Real-Time Distance Calculation:** Calculates and displays the distance between the sharer and the viewer.
- 🗺️ **Interactive Map:** Displays both user and sharer location on an interactive map (using Leaflet.js).
- 🔒 **CSRF-Protected:** Secure location sharing via Django's built-in security mechanisms.

---

## 🛠️ Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Map Service:** Leaflet.js + OpenStreetMap
- **Geolocation:** HTML5 Geolocation API

---

## 📸 Screenshots
> Add relevant screenshots here of:
1. The link generation page.
2. The map view with distance shown.

---


---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip
- virtualenv (optional but recommended)

### Setup
```bash
git clone https://github.com/dipan313/GeoShare.git
cd GeoShare
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 🚀 Access
Visit: [http://127.0.0.1:8000/generate/](http://127.0.0.1:8000/generate/) to create a location link.

---

## 📌 Future Enhancements
- User authentication for link access control.
- Expiry of generated links for enhanced privacy.
- Real-time tracking between sharer and viewer.

---

## 🤝 Contributing
Feel free to fork this repo, make changes, and submit PRs.

---

## 📄 License
This project is open-source under the **MIT License**.

---

## 🙌 Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Leaflet.js](https://leafletjs.com/)
- [OpenStreetMap](https://www.openstreetmap.org/)
