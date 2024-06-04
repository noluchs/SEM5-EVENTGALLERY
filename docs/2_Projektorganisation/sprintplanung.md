---
layout: default
title: 2.3 Sprint Planung 
parent: 2. Projektorganisation
nav_order: 3
---


# Sprint Planung 

## Sprint 1: Initialisierung und Basis-Setup (11. Mai - 31. Mai)

### Ziele:
- Projektanforderungen erfassen und dokumentieren
- Technologieauswahl und Setup der Entwicklungsumgebung
- Basis-Setup der Microservices

### Aufgaben:
1. **Anforderungsanalyse**
   - Benutzeranforderungen sammeln und dokumentieren
   - User Stories und Use Cases erstellen

2. **Technologieauswahl und Setup**
   - Auswahl des Backend-Frameworks (Flask) und Frontend-Frameworks (React mit Vite)
   - Auswahl der Datenbanktechnologie (PostgreSQL, MongoDB)
   - Tools für CI/CD und Containerisierung (Docker, Docker Compose, GitHub Actions) festlegen

3. **Systemarchitektur planen**
   - Microservice-Architektur entwerfen
   - API-Spezifikationen und Kommunikationsprotokolle definieren
   - Architekturdiagramme und Systemübersichten erstellen

4. **Basis-Setup der Microservices**
   - Grundstruktur der Microservices für Benutzerverwaltung, Galerieverwaltung und Bildverwaltung aufsetzen
   - Lokale Entwicklungsumgebung mit Docker und Docker Compose vorbereiten
   - Repository-Struktur auf GitHub einrichten

### Deliverables:
- Anforderungsdokumentation
- Technologie- und Toolauswahl
- Architekturdiagramme und Systemdesign-Dokumente
- Funktionsfähige Entwicklungsumgebung
- Basis-Setup der Microservices

---

## Sprint 2: Implementierung der Kernfunktionen und Sicherheit (1. Juni - 21. Juni)

### Ziele:
- Entwicklung der Kernfunktionen für Benutzerverwaltung, Galerieverwaltung und Bildverwaltung
- Implementierung der grundlegenden Sicherheitsmechanismen

### Aufgaben:
1. **Benutzerverwaltung implementieren**
   - Registrierung, Login und Benutzerprofilverwaltung
   - Datenbankintegration und ORM-Konfiguration (SQLAlchemy)

2. **Galerieverwaltung implementieren**
   - Erstellen, Verwalten und Löschen von Galerien
   - Hinzufügen und Entfernen von Bildern

3. **Bildverwaltung implementieren**
   - Hochladen, Speichern und Abrufen von Bildern
   - Anbindung an AWS S3

4. **Sicherheitsmechanismen integrieren**
   - Authentifizierung und Autorisierung mit JWT
   - Sicherheitsrichtlinien für Datenverschlüsselung und Schutz implementieren

5. **API-Struktur planen und implementieren**
   - API-Endpoints für Backend-Services definieren
   - Integration der Gesichtserkennungs-API planen

### Deliverables:
- Funktionsfähige Kernfunktionen der Microservices
- Implementierte Sicherheitsmechanismen
- API-Spezifikationen und Basis-Implementierungen

---

## Sprint 3: Integration, Tests und Deployment (22. Juni - 5. Juli)

### Ziele:
- Integration der Microservices
- Durchführung von Unit- und Integrationstests
- Erstellung der Abschlussdokumentation und Vorbereitung der Präsentation
- Deployment der Anwendung

### Aufgaben:
1. **Integration der Microservices**
   - API-Integration zwischen den Services
   - Sicherstellung der Datenkonsistenz und Integrität

2. **Tests durchführen**
   - Unit-Tests für einzelne Komponenten entwickeln
   - Integrationstests für die gesamte Anwendung schreiben
   - End-to-End-Tests durchführen

3. **Performance-Optimierung**
   - Analyse der Anwendungsperformance
   - Optimierung der Datenbankabfragen und Server-Responses

4. **Dokumentation erstellen**
   - Technische Dokumentation der Architektur und APIs
   - Benutzerhandbücher und Betriebsdokumentation
   - Dokumentation der Setup- und Deployment-Prozesse

5. **Präsentation vorbereiten**
   - Erstellen der Präsentationsmaterialien
   - Üben und Vorbereiten der Abschlusspräsentation

6. **Deployment vorbereiten und durchführen**
   - Deployment-Skripte erstellen und testen
   - Produktionsumgebung auf AWS EC2 mit Docker Compose einrichten
   - CI/CD-Pipeline mit GitHub Actions konfigurieren und testen

### Deliverables:
- Integrierte und getestete Anwendung
- Umfassende Abschlussdokumentation
- Präsentationsmaterialien
- Erfolgreich deployte Anwendung