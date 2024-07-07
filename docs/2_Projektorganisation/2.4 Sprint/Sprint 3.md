---
layout: default
title: 2.4.1 Sprint 3 Review
parent: 2.4 Sprint
grand_parent:   2. Projektorganisation  
nav_order: 3
---

# Sprint 3 Abschluss

  

## Fazit vom Sprint 3

  

Im dritten Sprint wurden alle Ziele erreicht, wenn auch mit erheblichem Mehraufwand. Die Authentifizierung zwischen Backend und Frontend funktionierte nicht wie erwartet, daher habe ich diese Aufgabe an Auth0 ausgelagert. Beim Proxy gab es Probleme mit Nginx, sodass ich auf Traefik umgestiegen bin, da es besser mit Docker und dem Management von Let's Encrypt-Zertifikaten funktioniert.


### Erreichte Ziele
  
1. **Integration der Microservices**
   - Erfolgreiche API-Integration zwischen den Services
   - Sicherstellung der Datenkonsistenz und Integrität
  

2. **Frontend fertiggestellt**
   - Implementierung aller geplanten Benutzeroberflächen
   - Integration des Frontends mit den Backend-APIs
   - Durchführung von End-to-End-Tests zur Sicherstellung der Funktionalität
   - Optimierung der Benutzeroberfläche für eine bessere User Experience (UX)


3. **Deployment vorbereitet und durchgeführt**
   - Erstellung und Testen der Deployment-Skripte
   - Einrichtung der Produktionsumgebung auf AWS EC2 mit Docker Compose
   - Konfiguration und Testen der CI/CD-Pipeline mit GitHub Actions
   - Sicherstellung, dass alle Dienste reibungslos in der Produktionsumgebung laufen


4. **Dokumentation erstellt**
   - Technische Dokumentation der Architektur und APIs
   - Erstellung von Benutzerhandbüchern und Betriebsdokumentationen
   - Detaillierte Dokumentation der Setup- und Deployment-Prozesse
   - Zusammenstellung aller relevanten Informationen für die spätere Wartung und Weiterentwicklung des Systems
  

5. **Präsentation vorbereitet**
   - Erstellung der Präsentationsmaterialien, einschliesslich Folien, Diagramme und Demo
   - Üben und Vorbereiten der Abschlusspräsentation, um die wichtigsten Aspekte des Projekts klar und präzise zu vermitteln
   - Feedback von Kollegen eingeholt und die Präsentation entsprechend verbessert
  

6. **Proxy mit SSL-Zertifikat**
   - Implementierung eines Reverse Proxys mit Traefik
   - Konfiguration des automatischen SSL-Zertifikatsmanagements mit Let's Encrypt
   - Sicherstellung, dass alle Datenübertragungen zwischen dem Client und den Servern sicher und verschlüsselt sind
   - Testen der SSL-Konfiguration und Überprüfung der Sicherheitszertifikate

### Status Prozentual

| Bereich           | Fortschritt |
| ----------------- | ----------- |
| Dokumentation     | 100 %       |
| Konzept           | 100 %       |
| Backend           | 100 %       |
| Frontend          | 100 %       |
| AWS EC2           | 100 %       |
| GitHub Deployment | 100 %       |
  

### Kanban Board

![](attachments/Screenshot%202024-07-06%20at%2011.48.26.png)

  

### Learnings für den nächsten Sprint
  

#### Flexibilität und Anpassungsfähigkeit


Die Notwendigkeit, Lösungen anzupassen und neue Tools zu integrieren, hat gezeigt, wie wichtig Flexibilität und Anpassungsfähigkeit in der Softwareentwicklung sind. Der Wechsel von Nginx zu Traefik und die Integration von Auth0 haben wesentlich zum Erfolg beigetragen.

#### Frühzeitiges Testen und Iterieren

Durch frühzeitiges Testen und Iterieren konnten viele Probleme rechtzeitig erkannt und behoben werden. Diese Vorgehensweise hat sich als äusserst effektiv erwiesen, um die Qualität des Endprodukts zu sichern.


#### Dokumentation als fortlaufender Prozess 

Die fortlaufende Erstellung und Aktualisierung der Dokumentation hat sich als äusserst wertvoll erwiesen. Eine gute Dokumentation erleichtert die Zusammenarbeit im Team und die zukünftige Wartung des Systems erheblich.

## Kritische Würdigung des Sprint-Reviews

  

Der dritte Sprint hat gezeigt, dass eine flexible Planung und die Bereitschaft, neue Werkzeuge und Ansätze zu integrieren, entscheidend für den Erfolg sind. Trotz der Herausforderungen und des zusätzlichen Aufwands wurden alle gesetzten Ziele erreicht. Die Erfahrungen aus diesem Sprint werden in zukünftigen Projekten von grossem Nutzen sein.