# Translator_FullStack_GCP
 Translation Tool from English To Spanish and Spanish to English
 ---
**The main goal of this project is to build the entire application on Google Cloud Computing using Python with Flask, API, Docker, Google Datastore, and Google Cloud Deployment.**
---
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

