#!/usr/bin/env bash
gcloud config set project $1 2>/dev/null
gcloud config set run/region us-central1
gcloud run deploy $1 \
--image=$2 \
--region=us-central1 \
--project=$1 \
 && gcloud run services update-traffic $1 --to-latest
