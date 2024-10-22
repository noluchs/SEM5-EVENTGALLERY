# MSCV-Gallery-with-Face-Matching

Dokumentation unter
[Dokumentation](https://noluchs.github.io/SEM4)

## Intro

This repo hosts the project _EventGallery_, a microservice-based gallery management system with integrated face recognition, designed to enhance the experience of event participants by efficiently identifying personal photos in large photo galleries.

## Technologies

- Flask (https://flask.palletsprojects.com/en/3.0.x/)
- ApiFlask (https://apiflask.com/)
- SQLAlchemy (https://www.sqlalchemy.org/)
- MySQL (https://www.mysql.com/de/)
- pyTest (https://docs.pytest.org/en/8.0.x/)
- Gunicorn (https://gunicorn.org/)
- Vue (https://vuejs.org/)
- Amazon Rekognition (https://aws.amazon.com/rekognition/)

## Installation


```

## Design
![PlantUML model](https://www.plantuml.com/plantuml/png/NOxD2i8m48Jl-nHBxtq5AUBFrNl9OPiEMapIibd58BwxWT9BRyFtCSDqsKJj5GFH8lufTt1pVYFPLKA0beQ_nDpVTFuKnsrxuFwYSpAaqUt5iGviVCkhEOd981cEVaIFQGGZBbOu8WxGl28_gGyWwcgl7le3)


## CI/CD

CI Variables (GitHub Actions):

- `DEPLOY_TARGET` - IP-address or DNS-name of the target server
- `SSH_HOST_KEY` - ssh-keyscan of the target server
- `SSH_PRIVATE_KEY` - private key to connect to the target server via SSH
