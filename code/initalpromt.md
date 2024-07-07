# Projekt: Event Gallery Management mit Gesichtserkennung

### Einführung

Die digitalen und interaktiven Bedürfnisse bei Veranstaltungen erfordern eine effiziente Lösung zur schnellen Identifizierung persönlicher Fotos in grossen Galerien. Dieses Projekt entwickelt ein Microservice-basiertes System mit Gesichtserkennung, um dieses Problem zu adressieren. Es unterscheidet sich von bestehenden Lösungen durch seine modulare Architektur und die direkte Integration von Gesichtserkennungstechnologien, die speziell auf die Anforderungen von Event-Veranstaltern und Teilnehmern zugeschnitten sind.

#### Bedarf

Veranstaltungen erzeugen eine grosse Menge an Fotomaterial, das effizient verwaltet und durchsucht werden muss. Besucher und Teilnehmer benötigen eine schnelle Methode, um sich selbst auf Fotos zu finden, ohne manuell durch Hunderte oder Tausende von Bildern blättern zu müssen.

#### Ansatz

Durch die Entwicklung eines Microservice-basierten Galerie-Verwaltungssystems mit integrierter Gesichtserkennung können Nutzer durch einfaches Hochladen eines Selfies alle Fotos finden, auf denen sie abgebildet sind. Dieses System nutzt moderne Cloud-Dienste und Gesichtserkennungstechnologien, um eine skalierbare und effiziente Lösung zu bieten.

#### Vorteile

Die Hauptvorteile dieses Systems sind die erhebliche Zeitersparnis für die Nutzer bei der Suche nach eigenen Fotos und die Verbesserung des Gesamterlebnisses bei Veranstaltungen. Durch die Automatisierung des Suchprozesses wird das Erlebnis für den Endnutzer wesentlich angenehmer und interaktiver.

#### Wettbewerb

Aktuelle Lösungen erfordern oft manuelles Durchsuchen der Galerien oder bieten keine spezifische, nutzerfreundliche Suche basierend auf Gesichtserkennung. Dieses System stellt eine direkte Verbesserung dar, indem es eine intuitive, effektive und schnelle Suche ermöglicht und sich durch seine Microservice-Architektur leicht an verschiedene Grössen und Arten von Veranstaltungen anpassen lässt.

---

### Verzeichnungsstruktur

```plaintext


```

---

### Datenbankmodell

Das Datenbankmodell beschreibt die Struktur und die Beziehungen der verschiedenen Tabellen.

#### Tabelle: `users`

- **id**: Primärschlüssel des Benutzers.
- **username**: Benutzername des Benutzers.
- **email**: E-Mail-Adresse des Benutzers.
- **password_hash**: Passwort-Hash des Benutzers.
- **created_at**: Erstellungsdatum des Benutzers.

#### Tabelle: `galleries`

- **id**: Primärschlüssel der Galerie.
- **title**: Titel der Galerie.
- **description**: Beschreibung der Galerie.
- **created_at**: Erstellungsdatum der Galerie.
- **user_id**: Fremdschlüssel, der auf die `id` der `users`-Tabelle verweist.

#### Tabelle: `photos`

- **id**: Primärschlüssel des Fotos.
- **filename**: Dateiname des Fotos.
- **url**: URL des Fotos.
- **gallery_id**: Fremdschlüssel, der auf die `id` der `galleries`-Tabelle verweist.
- **description**: Beschreibung des Fotos.
- **uploaded_at**: Hochladedatum des Fotos.

#### Tabelle: `events`

- **id**: Primärschlüssel des Events.
- **name**: Name des Events.
- **date**: Datum des Events.
- **location**: Ort des Events.
- **gallery_id**: Fremdschlüssel, der auf die `id` der `galleries`-Tabelle verweist.

#### Tabelle: `face_recognitions`

- **id**: Primärschlüssel der Gesichtserkennung.
- **photo_id**: Fremdschlüssel, der auf die `id` der `photos`-Tabelle verweist.
- **user_id**: Fremdschlüssel, der auf die `id` der `users`-Tabelle verweist.
- **recognized_at**: Datum und Uhrzeit der Erkennung.

### Beziehungen

- Ein Benutzer (`user`) kann mehrere Galerien (`galleries`) besitzen.
- Eine Galerie (`gallery`) kann mehrere Fotos (`photos`) enthalten.
- Ein Event (`event`) kann eine Galerie (`gallery`) haben.
- Eine Gesichtserkennung (`face_recognition`) bezieht sich auf ein Foto (`photo`) und einen Benutzer (`user`).

### Grafische Darstellung

```plaintext
+----------------------+         +-----------------------+         +----------------------+
|        users         |         |       galleries       |         |        photos        |
+----------------------+         +-----------------------+         +----------------------+
| id (PK)              |<--+     | id (PK)               |<--+     | id (PK)              |
| username             |   |     | title                 |   |     | filename             |
| email                |   |     | description           |   |     | url                  |
| password_hash        |   |     | created_at            |   +---> | gallery_id (FK)      |
| created_at           |   +---> | user_id (FK)          |         | description          |
+----------------------+         +-----------------------+         | uploaded_at          |
                                                                   +----------------------+

+----------------------+         +-----------------------+
|       events         |         |   face_recognitions   |
+----------------------+         +-----------------------+
| id (PK)              |<--+     | id (PK)               |
| name                 |   |     | photo_id (FK)         |
| date                 |   +---> | user_id (FK)          |
| location             |         | recognized_at         |
| gallery_id (FK)      |         +-----------------------+
+----------------------+
```

### SQLAlchemy Model Definition

```python
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=db.func.current_timestamp())
    galleries = relationship('Gallery', backref='owner', lazy=True)

class Gallery(db.Model):
    __tablename__ = 'galleries'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=db.func.current_timestamp())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    photos = relationship('Photo', backref='gallery', lazy=True)
    events = relationship('Event', backref='gallery', lazy=True)

class Photo(db.Model):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    gallery_id = Column(Integer, ForeignKey('galleries.id'), nullable=False)
    description = Column(String(255))
    uploaded_at = Column(DateTime, default=db.func.current_timestamp())

class Event(db.Model):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=False)
    gallery_id = Column(Integer, ForeignKey('galleries.id'), nullable=False)

class FaceRecognition(db.Model):
    __tablename__ = 'face_recognitions'
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer, ForeignKey('photos.id'), nullable=False)
    user_id = Column(Integer, ForeignKey
```
### Frontend
```plaintext
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Home.jsx
│   │   ├── GalleryView.jsx
│   │   ├── Admin/
│   │   │   ├── Login.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── GalleryManager.jsx
│   │   │   ├── PhotoManager.jsx
│   │   ├── common/
│   │   │   ├── GalleryCard.jsx
│   │   │   └── PhotoCard.jsx
│   ├── context/
│   │   └── AuthContext.jsx
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
├── Dockerfile
├── package.json
├── tailwind.config.js
└── vite.config.js
```


### Backend
    