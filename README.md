Hi! This is the simple movie CRUD api to demonstrate my skillset.

========================================

Technologies I've used are :

- Python 3.9 programming language
- Django Rest framework
- Sqlite/PostgreSQL
- I've Dockerized the project and also the project contains docker-compose.yaml file for deployment
- Simple bash scripts for the initializing of dokcer images are also included in the project
- Nginx configuration is in the nginx directory
- Swagger for API documentation

========================================

Assumptions :

- I've tested the project on local machine, this is not the final production environment project!

- The main app is named "movieApp", so the main models, views, serializers are there

- I tried to test on Liara Object Storage service that uses Minio, but there was a problem in communicating with Liara API,
So this project stores files on local filesystem

- In the Nginx configuration file, there is a single upstream section, but if we have an Object Storage service, up and running,
It will have two upstream sections (additional section will be used for the Object Storage backend) respectively

- The images are stored in /media directory , and the static files are stored in /static directory

- The screenshot directory contains some images of working project

=========================================

Running the project :

- docker-compose up -d

It's up and running on your localhost :)
