---
layout: default
title: 1. Einleitung
nav_order: 1
permalink: /
---
# Einleitung

Die Projekteinleitung beschreibt die grundlegenden Ziele und Anforderungen der Semesterarbeit. Dabei werden die folgenden Kernpunkte hervorgehoben:

## Zielsetzung

- Aufbau eines lokalen DeepFace-Microservices zur Gesichtserkennung und Integration in die EventGallery Plattform.
- Umsetzung einer automatisierten Infrastruktur mithilfe von Terraform, Ansible und GitOps über ArgoCD.
- Sicherstellung eines sicheren, datenschutzkonformen Betriebs der Plattform ohne Abhängigkeit von Cloud-Diensten.
- Entwicklung einer skalierbaren und modularen Architektur für zukünftige Erweiterungen.

## Motivation

Im Rahmen dieser Semesterarbeit wird die bestehende EventGallery-Plattform aus der 4. Semesterarbeit weiterentwickelt. 
Ziel ist es, die bisherige Cloud-Abhängigkeit zu eliminieren und eine komplett selbstbetriebene Infrastruktur zu schaffen. 
Der Fokus liegt auf Datenschutz, Automatisierung, Skalierbarkeit und Betriebssicherheit. 
Dies liefert praxisrelevante Einblicke in moderne Cloud-native Ansätze und den Aufbau datenschutzkonformer Systeme.

## Erwartete Ergebnisse

Die Semesterarbeit zielt darauf ab, folgende Ergebnisse zu erreichen:

1. **FaceService:** Lokaler Microservice zur Gesichtserkennung basierend auf DeepFace, integriert in die EventGallery.
2. **Speicherlösung:** Lokale Speicherung von Eventbildern und Encodings mit MinIO und MySQL.
3. **Automatisierte Infrastruktur:** Aufbau und Verwaltung der Infrastruktur über Infrastructure as Code und GitOps.
4. **Secret Management:** Sichere Verwaltung sensibler Konfigurationsdaten mit Bitwarden CLI oder SOPS.
5. **Dokumentation:** Vollständige technische Dokumentation aller Entwicklungen, Entscheidungen und Resultate.

## Systemarchitektur

Die folgende Übersicht zeigt die Architektur des Projekts und die Interaktion der verschiedenen Komponenten:

```mermaid
graph TD
    subgraph Benutzer
        User["Benutzer (Browser)"]
    end

    subgraph Cloudflare Netzwerk
        CF["Cloudflare Tunnel"]
    end

    subgraph Kubernetes Cluster
        Frontend["Frontend Service"]
        Backend["Backend Service"]
        DB["MySQL Datenbank"]
        MinIO["MinIO (Dateispeicher)"]
        FaceService["DeepFace FaceService (lokal)"]
        Metallb["MetalLB Load Balancer"]
        ArgoCD["ArgoCD (GitOps)"]
    end

    subgraph Secrets Management
        Bitwarden["Bitwarden / SOPS"]
    end

    User -->|HTTPS| CF
    CF --> Metallb
    Metallb --> Frontend
    Frontend -->|API-Calls| Backend
    Backend -->|Authentifizierung| Bitwarden
    Backend -->|Gesichtserkennung| FaceService
    Backend -->|Speichern| MinIO
    Backend -->|Datenbankzugriff| DB
    ArgoCD --> Frontend
    ArgoCD --> Backend
    ArgoCD --> FaceService
    ```