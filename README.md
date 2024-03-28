# Translator_FullStack_GCP
 Translation Tool from English To Spanish and Spanish to English
 - Anh Ho 
 ---

***Translator_FullStack_GCP*** is a robust translation tool equipped with a sleek web interface, built using the Flask web framework. Seamlessly translating between English and Spanish, as well as Spanish to English, this application leverages the power of Google Cloud Datastore library for efficient data storage and retrieval. Powered by Gunicorn, a Python WSGI HTTP server, it ensures smooth and reliable connectivity between web servers like nginx and the application itself. Enhance your multilingual communication effortlessly with Translator_FullStack_GCP.

 
**The main goal of this project is to build the entire application on Google Cloud Platform **
All the tools I have used for this project including:
```
Python with Flask: Appropriate for web application development.

Merriam-Webster API: Suitable for integrating a translation tool and dictionary functionality into my application.

Docker containers: A standard choice for packaging and deploying applications, including images and dependencies.

Google Datastore: A NoSQL database service provided by Google Cloud, often used for storing and retrieving structured data in applications.

Google Cloud Deployment: Refers to the process of deploying your application on Google Cloud, ensuring scalability, reliability, and accessibility.
```
Deployed URL: https://final-zd23viltva-wl.a.run.app/ 
---
![image](https://github.com/anhoop89/Translator_FullStack_GCP/assets/102849461/13bf598d-3ec9-4a0f-b844-e17d1e8e6993)
# **** How to set up the project from a scratch ****
## Create the service account: 
> gcloud iam service-accounts create finalTranslation

## Add the Cloud Datastore User role to the service account: 
> gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
  --member serviceAccount:finalTranslation@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
  --role roles/datastore.user

## how to set up API key into the cloud and avoid hard-code: in translate.py

> def __init__(self):
self.api_key = os.environ.get("API_KEY")  

# RUN LOCALLY: How to run the project locally
> python3 -m venv env

> source env/bin/activate

> pip install -r requirements.txt

> export API_KEY="877a0bd4-cb72-4741-8265-41e318755512" 

> python app.py

# DOCKER: build a docker image: 
> create an image: docker build -t translation_img .

> run docker with the API key for testing: docker run --env API_KEY=877a0bd4-cb72-4741-8265-41e318755512 -p 8000:8000 --env PORT=8000 --rm translation_img

## Build the docker container using Cloud Build and then push it to the gcr.io registry to host it
gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/translation_img

# DEPLOY the project using GCP
>gcloud run deploy final --image gcr.io/${GOOGLE_CLOUD_PROJECT}/translation_img --set-env-vars API_KEY=877a0bd4-cb72-4741-8265-41e318755512 --service-account finalTranslation@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com
## check a list of the existing services deployed in your project
>gcloud run services list

## destroy the deployment

> To destroy or delete a deployment in Google Cloud Run, you can use the 
> gcloud run services delete final


