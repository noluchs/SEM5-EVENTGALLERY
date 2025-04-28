---
layout: default
title: 1. Einleitung
nav_order: 1
permalink: /
---
# Einleitung

Die Projekteinleitung beschreibt die grundlegenden Ziele und Anforderungen der Semesterarbeit. Dabei werden die folgenden Kernpunkte hervorgehoben:

## Zielsetzung

- **Bereitstellung von Microservices auf Kubernetes:** Die bereits entwickelten Microservices werden in einem Kubernetes-Cluster deployed und orchestriert, um ihre Skalierbarkeit und Verfügbarkeit zu gewährleisten.
    
- **Automatisierung des Deployment-Prozesses:** Eine CI/CD-Pipeline wird eingerichtet, um den Quellcode bei jeder Änderung automatisiert zu testen und in den Produktions-Cluster zu integrieren. Dies gewährleistet kontinuierliche Verbesserungen und zeitnahe Implementierungen.
    
- **Sicherstellung der Skalierbarkeit und Ausfallsicherheit:** Kubernetes ermöglicht die automatische Skalierung der Microservices basierend auf der Nachfrage, und die Pipeline sorgt für problemlose Aktualisierungen der Services.
    

## Motivation

Im Rahmen dieser Semesterarbeit soll ein modernes, skalierbares und resilient aufgebautes System geschaffen werden, das den Anforderungen einer Cloud-nativen Architektur entspricht. Der Fokus liegt auf der Automatisierung von Prozessen, der einfachen Reproduzierbarkeit sowie der Nutzung moderner Technologien wie Kubernetes, ArgoCD und Terraform.

Die Arbeit liefert praxisrelevante Einblicke in die Automatisierung und Orchestrierung von Anwendungen, die sowohl im Entwicklungs- als auch im Produktionsumfeld von großem Nutzen sind.

## Erwartete Ergebnisse

Die Semesterarbeit zielt darauf ab, folgende Ergebnisse zu erreichen:

1. **Kubernetes-Cluster:** Ein stabiler und funktionsfähiger Kubernetes-Cluster, auf dem die Microservices zuverlässig betrieben werden können.
    
2. **CI/CD-Pipeline:** Eine automatisierte CI/CD-Pipeline, die Änderungen am Quellcode kontinuierlich integriert und bereitstellt.
    
3. **Skalierbarkeit und Verfügbarkeit:** Eine evaluierte und dokumentierte Skalierbarkeit sowie Ausfallsicherheit der bereitgestellten Services.
    
4. **Dokumentation:** Eine vollständige technische Dokumentation der Implementierung und Konfiguration aller eingesetzten Tools und Technologien.
    

## Systemarchitektur

Die folgende Übersicht zeigt die Architektur des Projekts und die Interaktion der verschiedenen Komponenten:
[![](https://mermaid.ink/img/pako:eNp9VN9v2jAQ_lcsP3USFZP2xkMlSMaKtlYVoaq0ZQ9HcgQLx878Y5Q2_d93xgTSFeGXfLn7_OXuPjuvvNAl8hGvDDRrtkhzxWhZv4yBR4uGpfhXFGhjKqwQ_ZXzffJqYvSWwKec_44MVGWu_tNJpPblSoJBdo9uq83mpJZMSatHWHilUF6U--6XaBQ6tKTsrUNzkpsarRxtItEOsgxNaOGoGdYEik2kHdBZ1thUOkmJFMG73B06kHJJyQNiPzSUJCxBFVRSn5tOiJaCgyVYvNjb-CnrKumNPPsSaqjhRSvC76TnuNGVEk5odeL0ghe_9vWZhqdAsvHDrNe1d-vPQSw82VV4oHKigKB31un9Wbi-vmlvF4uHrCVTYzyZhmg3qhjrphUSnUUxczQsKFFFLCFiG8s5w5jjH4_WtZ2XkdLZGRjJbJik7cHFmI54n52iK-hs0g1o2Tfhbn3wMgIaYKOtcNrsju32hecI5fDJCEdb08nH_GMj6SwMU71VAbTBtA-kWQ0VsjGNf2eFbfum8QGv0dQgSrqcr2FrzsmEms7OiGCJK_DS5TxXb0QF73S2UwUfOeNxwI321ZqPViAtvfmmBIepALK87ihYhubu4u3f_wQGvAH1U-v6sPHtH2ZiUCs?type=png)](https://mermaid-js.github.io/mermaid-live-editor//edit#pako:eNp9VN9v2jAQ_lcsP3USFZP2xkMlSMaKtlYVoaq0ZQ9HcgQLx878Y5Q2_d93xgTSFeGXfLn7_OXuPjuvvNAl8hGvDDRrtkhzxWhZv4yBR4uGpfhXFGhjKqwQ_ZXzffJqYvSWwKec_44MVGWu_tNJpPblSoJBdo9uq83mpJZMSatHWHilUF6U--6XaBQ6tKTsrUNzkpsarRxtItEOsgxNaOGoGdYEik2kHdBZ1thUOkmJFMG73B06kHJJyQNiPzSUJCxBFVRSn5tOiJaCgyVYvNjb-CnrKumNPPsSaqjhRSvC76TnuNGVEk5odeL0ghe_9vWZhqdAsvHDrNe1d-vPQSw82VV4oHKigKB31un9Wbi-vmlvF4uHrCVTYzyZhmg3qhjrphUSnUUxczQsKFFFLCFiG8s5w5jjH4_WtZ2XkdLZGRjJbJik7cHFmI54n52iK-hs0g1o2Tfhbn3wMgIaYKOtcNrsju32hecI5fDJCEdb08nH_GMj6SwMU71VAbTBtA-kWQ0VsjGNf2eFbfum8QGv0dQgSrqcr2FrzsmEms7OiGCJK_DS5TxXb0QF73S2UwUfOeNxwI321ZqPViAtvfmmBIepALK87ihYhubu4u3f_wQGvAH1U-v6sPHtH2ZiUCs)