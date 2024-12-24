---
layout: default
title: 2.4.2 Sprint 2 Review
parent: 2.4 Sprint
grand_parent:   2. Projektorganisation  
nav_order: 2
---
# # Sprint 2 Abschluss

## Fazit vom Sprint 2

Im zweiten Sprint lag der Fokus auf der Einrichtung des Kubernetes-Clusters und der Integration der Microservices. Während der Arbeit traten Herausforderungen auf, die erfolgreich gelöst werden konnten:

- Cluster-Aufbau auf MAAS: Es gab wiederholte Probleme mit dem Verlust der Worker-Nodes, welche durch Anpassungen an der Netzwerkkonfiguration und Stabilisierung des Clusters behoben werden konnten.

- GitHub Runner: Der GitHub Runner verlor regelmäßig die Verbindung zum Cluster, was den reibungslosen Ablauf des Deployments erschwerte.  

  - Lösung: Um die Stabilität des Deployments zu gewährleisten, wurde ArgoCD für das Deployment der Microservices eingesetzt. Dies ermöglichte eine zuverlässige und deklarative Bereitstellung im Kubernetes-Cluster.  

Durch die zeitintensiven Problembehebungen und den entstandenen Stress kam das Dokumentieren der Arbeitsschritte leider zu kurz. Die fehlende Dokumentation wird im nächsten Sprint nachgeholt, um eine lückenlose Nachvollziehbarkeit sicherzustellen. Zudem konnte der Sprint-Abschluss aufgrund der Verzögerungen erst verspätet durchgeführt werden.

  

## Status Prozentual
  

| Dokumentation | Konzept | Kubernetes Cluster | GitHub Deployment | Testplanung |

| ------------- | ------- | ------------------ | ----------------- | ----------- |

| 30%           | 30%     | 80%                | 40%               | 20%        |


## Ergebnisse aus Sprint 2

1. Einrichtung des Kubernetes-Clusters  
   - Der MicroK8s-Cluster wurde stabilisiert und die Netzwerkprobleme auf MAAS wurden behoben.  
   - Die Worker-Nodes konnten dauerhaft im Cluster gehalten werden.


2. Deployment-Strategie angepasst  
   - Aufgrund der Instabilität des GitHub Runners wurde auf ArgoCD umgestellt.  
   - ArgoCD ermöglicht nun eine zuverlässige, automatisierte Bereitstellung der Microservices im Kubernetes-Cluster.

3. Integration der Microservices  

   - Erste Microservices wurden erfolgreich mit ArgoCD deployed und getestet.  
   - Die YAML-Dateien für Deployments und Services wurden optimiert.

4. Dokumentation als Nachholbedarf  
   - Aufgrund der Zeitknappheit und des Troubleshootings wurde das Dokumentieren der Arbeitsschritte vernachlässigt. Dies wird im nächsten Sprint priorisiert und nachgeholt.
### Status Prozentual
| Dokumentation | Konzept | Kubernetes Cluster  | GitHub Deployment  | Testplanung |     |
| ------------- | ------- | ------------------- | ------------------ | ----------- | --- |
| 20%           | 100%    | 80%                 | 20%                | 0%          |     |


### Sprint Backlog
![](attachments/Pasted%20image%2020241218154133.png)

## Learnings für den nächsten Sprint

  
1. Monitoring einführen: Ein Fokus auf Monitoring-Tools wie Prometheus oder Grafana hilft, zukünftige Probleme frühzeitig zu erkennen.  
2. Dokumentation nachholen: Sämtliche bisherige Arbeitsschritte und Problemlösungen müssen im nächsten Sprint nachdokumentiert werden.  
3. CI/CD Pipeline optimieren: ArgoCD ist stabil, muss jedoch in Kombination mit den YAML-Dateien weiter getestet und verfeinert werden.  
4. Ausfallsicherheit testen: Umfangreiche Tests zur Stabilität des Clusters unter Last und bei möglichen Netzwerkproblemen sind erforderlich.
## Kritische Würdigung des Sprint-Reviews

  

Der zweite Sprint war geprägt von unerwarteten Problemen beim Cluster-Aufbau auf MAAS und beim Einsatz des GitHub Runners. Durch die Umstellung auf ArgoCD konnte eine verlässliche Deployment-Strategie implementiert werden. Allerdings führte der hohe Zeitaufwand für Problemlösungen dazu, dass das Dokumentieren der Arbeitsschritte zu kurz kam. Der Sprint-Abschluss musste aufgrund der Verzögerungen verspätet durchgeführt werden. Dies wird im kommenden Sprint aufgeholt, um die Nachvollziehbarkeit und Qualität der Arbeit sicherzustellen.

