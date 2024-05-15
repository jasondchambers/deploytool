#!/usr/bin/env bash

gcloud_project=$1
service=$2
image=$3

gcloud config set project $gcloud_project 2>/dev/null
gcloud config set run/region us-central1
gcloud run deploy $service \
--image=$image \
--region=us-central1 \
--project=$gcloud_project \
 && gcloud run services update-traffic $service --to-latest
