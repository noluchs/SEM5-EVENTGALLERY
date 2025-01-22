---
layout: default
title: 1. Einleitung
nav_order: 1
permalink: /
---
# Einleitung

[![](https://mermaid.ink/img/pako:eNp9VN9v2jAQ_lcsP3USFZP2xkMlSMaKtlYVoaq0ZQ9HcgQLx878Y5Q2_d93xgTSFeGXfLn7_OXuPjuvvNAl8hGvDDRrtkhzxWhZv4yBR4uGpfhXFGhjKqwQ_ZXzffJqYvSWwKec_44MVGWu_tNJpPblSoJBdo9uq83mpJZMSatHWHilUF6U--6XaBQ6tKTsrUNzkpsarRxtItEOsgxNaOGoGdYEik2kHdBZ1thUOkmJFMG73B06kHJJyQNiPzSUJCxBFVRSn5tOiJaCgyVYvNjb-CnrKumNPPsSaqjhRSvC76TnuNGVEk5odeL0ghe_9vWZhqdAsvHDrNe1d-vPQSw82VV4oHKigKB31un9Wbi-vmlvF4uHrCVTYzyZhmg3qhjrphUSnUUxczQsKFFFLCFiG8s5w5jjH4_WtZ2XkdLZGRjJbJik7cHFmI54n52iK-hs0g1o2Tfhbn3wMgIaYKOtcNrsju32hecI5fDJCEdb08nH_GMj6SwMU71VAbTBtA-kWQ0VsjGNf2eFbfum8QGv0dQgSrqcr2FrzsmEms7OiGCJK_DS5TxXb0QF73S2UwUfOeNxwI321ZqPViAtvfmmBIepALK87ihYhubu4u3f_wQGvAH1U-v6sPHtH2ZiUCs?type=png)](https://mermaid-js.github.io/mermaid-live-editor//edit#pako:eNp9VN9v2jAQ_lcsP3USFZP2xkMlSMaKtlYVoaq0ZQ9HcgQLx878Y5Q2_d93xgTSFeGXfLn7_OXuPjuvvNAl8hGvDDRrtkhzxWhZv4yBR4uGpfhXFGhjKqwQ_ZXzffJqYvSWwKec_44MVGWu_tNJpPblSoJBdo9uq83mpJZMSatHWHilUF6U--6XaBQ6tKTsrUNzkpsarRxtItEOsgxNaOGoGdYEik2kHdBZ1thUOkmJFMG73B06kHJJyQNiPzSUJCxBFVRSn5tOiJaCgyVYvNjb-CnrKumNPPsSaqjhRSvC76TnuNGVEk5odeL0ghe_9vWZhqdAsvHDrNe1d-vPQSw82VV4oHKigKB31un9Wbi-vmlvF4uHrCVTYzyZhmg3qhjrphUSnUUxczQsKFFFLCFiG8s5w5jjH4_WtZ2XkdLZGRjJbJik7cHFmI54n52iK-hs0g1o2Tfhbn3wMgIaYKOtcNrsju32hecI5fDJCEdb08nH_GMj6SwMU71VAbTBtA-kWQ0VsjGNf2eFbfum8QGv0dQgSrqcr2FrzsmEms7OiGCJK_DS5TxXb0QF73S2UwUfOeNxwI321ZqPViAtvfmmBIepALK87ihYhubu4u3f_wQGvAH1U-v6sPHtH2ZiUCs)

Im 3. Semester habe ich ein Galerieverwaltungssystem mit Gesichtserkennung entwickelt, das auf einem Server in diversen Containern läuft. Das System ist zwar funktional, aber es fehlen wichtige Funktionen wie automatische Skalierbarkeit und Ausfallsicherheit. Ziel dieser Arbeit ist es, das bestehende System Kubernetes-fähig zu machen und eine CI/CD-Pipeline einzurichten, um eine effiziente und fehlerfreie Bereitstellung der Microservices sicherzustellen.

## Need:
Das bestehende Microservice-basierte Galerieverwaltungssystem benötigt eine zukunftssichere Plattform, die eine automatische Skalierung und Ausfallsicherheit ermöglicht. Derzeit erfolgt das Deployment manuell, was zu potenziellen Fehlern und Verzögerungen führt. Da das System mit wachsenden Datenmengen und steigender Nutzerzahl umgehen muss, ist eine flexible, automatisierte Lösung notwendig.

## Approach:
Das System wird auf Kubernetes migriert, um eine automatische Orchestrierung und Skalierung der Microservices sicherzustellen. Kubernetes ermöglicht es, die Ressourcen je nach Auslastung dynamisch anzupassen. Zudem wird eine CI/CD-Pipeline implementiert, die sicherstellt, dass der Code nach jeder Änderung automatisch getestet und in den Produktions-Cluster integriert wird. Dies erfolgt entweder mit GitHub oder Azure DevOps als CI/CD-Tool.

## Benefit:
Durch die Kubernetes-Migration wird das System widerstandsfähiger und kann auf veränderte Lastanforderungen reagieren. Die CI/CD-Pipeline automatisiert den gesamten Bereitstellungsprozess und reduziert menschliche Fehler. Die Nutzung von Kubernetes und CI/CD sorgt dafür, dass die Anwendung hochverfügbar ist, einfach zu warten und flexibel auf zukünftige Anforderungen skalierbar bleibt.

## Competition:
Im Vergleich zu herkömmlichen Server- und Containerlösungen bietet Kubernetes eine native Unterstützung für automatische Skalierbarkeit und Ausfallsicherheit. Andere Lösungen erfordern oft manuelle Skalierung oder den Einsatz zusätzlicher Tools, um ähnliche Ergebnisse zu erzielen. Kubernetes bietet eine umfassende Plattform, die nicht nur die Verwaltung erleichtert, sondern auch die Effizienz im Betrieb erheblich steigert.


## Praxisbeispiel mit Zahlen und Fakten

**Event:** Musikfestival mit 10.000 Teilnehmern  
**Fotos:** 10.000 Fotos wurden während des Events gemacht

### Aktuelle Situation
- Viele Teilnehmer machen sich nicht die Mühe, ihre Fotos manuell zu suchen, da es zu zeitaufwendig ist. Dadurch gehen viele wertvolle Erinnerungen verloren und die Interaktionsrate auf der Webseite bleibt niedrig.
- Das aktuelle System benötigt manuelles Deployment und manuelle Skalierung, wodurch Ressourcen ineffizient genutzt werden und Verzögerungen entstehen können, wenn plötzlich viele Teilnehmer gleichzeitig auf das System zugreifen.

### Mit dem neuen System (nach Kubernetes-Migration und CI/CD)
- **Teilnehmererfahrung:** Teilnehmer laden ein Selfie hoch, und das System analysiert es innerhalb von 30 Sekunden, um alle relevanten Fotos anzuzeigen. Durch die Integration in Kubernetes kann das System bei erhöhtem Teilnehmeraufkommen automatisch skalieren und die hohe Verfügbarkeit der Anwendung gewährleisten.
- **Automatisierte Skalierung:** Kubernetes skaliert die Microservices dynamisch nach der Last, um eine gleichbleibend hohe Performance zu bieten, unabhängig von der Anzahl der gleichzeitig aktiven Teilnehmer.
- **Kontinuierliche Verbesserungen:** Durch die Implementierung der CI/CD-Pipeline werden Änderungen und Optimierungen im System automatisch getestet und nahtlos bereitgestellt, ohne dass die Verfügbarkeit beeinträchtigt wird.

### Ergebnis
- **Erhöhte Nutzerzufriedenheit:** Teilnehmer können ihre persönlichen Fotos schnell und unkompliziert finden, was zu einer höheren Zufriedenheit führt.
- **Steigerung der Interaktionsrate:** Durch die leichtere Zugänglichkeit der Fotos steigt die Wahrscheinlichkeit, dass Teilnehmer ihre Bilder auf Social Media teilen.
- **Verbesserte Veranstaltungswahrnehmung:** Die Möglichkeit, leicht an persönliche Fotos zu gelangen, verbessert das gesamte Veranstaltungserlebnis und hinterlässt einen positiven Eindruck bei den Teilnehmern.
- **Skalierbarkeit und Zuverlässigkeit:** Durch Kubernetes kann das System bei hohen Nutzerzahlen automatisch skalieren und bleibt dabei zuverlässig und performant.

## Nutzen für den Veranstalter
- **Verbesserte Nutzererfahrung:** Das System bietet eine schnelle und präzise Fotosuche, wodurch das Erlebnis für die Teilnehmer angenehmer und interaktiver wird.
- **Erhöhte Teilungsrate:** Da die Teilnehmer ihre Fotos leichter finden und teilen können, steigt die Wahrscheinlichkeit, dass sie die Fotos auf Social Media teilen, was die Sichtbarkeit und Reichweite der Veranstaltung erhöht.
- **Effiziente Verwaltung und automatische Skalierung:** Veranstalter können eine grosse Menge an Fotos effizient verwalten. Durch die automatische Skalierung in Kubernetes wird das System bei steigenden Nutzerzahlen nicht langsamer, und die Bereitstellung von neuen Features und Updates erfolgt ohne Unterbrechungen dank der CI/CD-Pipeline.