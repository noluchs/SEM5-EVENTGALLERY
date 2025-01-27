---
layout: default
title: 2.4.3 Sprint 3 Review
parent: 2.4 Sprint
grand_parent:   2. Projektorganisation  
nav_order: 3
---
# Sprint 3 Abschluss und Projektabschluss

## Fazit vom Sprint 3 und Projektabschluss

Der dritte Sprint markierte den erfolgreichen Abschluss der gesamten Semesterarbeit. Der Fokus lag auf der Durchführung von Tests, der Optimierung des Systems, der Implementierung der automatischen Skalierung sowie der Fertigstellung der Dokumentation und der Präsentation. Trotz einiger unerwarteter Herausforderungen konnten alle Projektziele erreicht werden.

### Erreichte Ziele

1. **Integration der Microservices**
   - Die Microservices wurden vollständig in den Kubernetes-Cluster integriert.
   - Datenflüsse zwischen den Services wurden getestet und stabilisiert.
   - Erste Lasttests bestätigten die Skalierbarkeit und Stabilität.

2. **Automatische Skalierung**
   - Der Horizontal Pod Autoscaler (HPA) wurde erfolgreich implementiert, um eine dynamische Skalierung basierend auf CPU-Auslastung zu ermöglichen.
   - Skalierungsszenarien wurden getestet, und die Ausfallsicherheit wurde sichergestellt.

3. **Tests und Optimierung**
   - Umfangreiche Systemtests zur Überprüfung der Verfügbarkeit, Skalierbarkeit und Performance wurden durchgeführt.
   - Schwachstellen im System wurden identifiziert und optimiert.

4. **Abschluss der Dokumentation**
   - Die technische Dokumentation wurde abgeschlossen und umfasst alle Architekturentscheidungen, Konfigurationsdetails, Testergebnisse und Anleitungen zur Wartung sowie Weiterentwicklung.
   - Die Herausforderungen und Lösungswege wurden ausführlich dokumentiert.

5. **Präsentation vorbereitet**
   - Die Präsentation für das Kolloquium wurde erstellt und mit Diagrammen sowie Testergebnissen angereichert.
   - Die wichtigsten Ergebnisse und der Projektverlauf wurden klar und prägnant dargestellt.

### Status Prozentual

| Bereich                 | Fortschritt |
| ----------------------- | ----------- |
| Dokumentation           | 100 %       |
| Konzept                 | 100 %       |
| Kubernetes Cluster      | 100 %       |
| Tests und Skalierung    | 100 %       |
| Präsentation            | 100 %       |

### Kanban Board

![](attachments/Pasted%20image%2020250127132052.png)
### Learnings aus dem Projekt

#### Flexibilität und Problemlösung
Die Notwendigkeit, auf Herausforderungen wie die Stabilisierung der Worker-Nodes und die Umstellung auf ArgoCD zu reagieren, hat die Bedeutung von Flexibilität und schnellem Problemlösungsdenken unterstrichen.

#### Skalierbarkeit und Performance
Die Implementierung und Tests des HPA haben gezeigt, wie wichtig eine robuste Skalierungsstrategie für eine zuverlässige und skalierbare Anwendung ist.

#### Dokumentation als kontinuierlicher Prozess
Es wurde deutlich, dass eine laufende Pflege der Dokumentation nicht nur die Nachvollziehbarkeit sichert, sondern auch den Projektabschluss erleichtert. Diese Erkenntnis sollte für zukünftige Projekte berücksichtigt werden.

## Kritische Würdigung des gesamten Projekts

Das Projekt wurde erfolgreich abgeschlossen und hat alle gesetzten Ziele erreicht. Die Herausforderungen, insbesondere bei der Stabilisierung des Clusters und der Einführung einer automatischen Skalierung, haben wertvolle Erfahrungen geliefert. Die gesammelten Learnings und die Ergebnisse des Projekts bilden eine solide Grundlage für zukünftige Arbeiten und Entwicklungen.

Mit der vollständigen Integration der Microservices, der Skalierbarkeit durch Kubernetes und der fertigen Dokumentation konnte ein stabiles und skalierbares System präsentiert werden, das die Anforderungen voll erfüllt.
