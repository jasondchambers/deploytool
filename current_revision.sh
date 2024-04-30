#!/usr/bin/env bash
gcloud config set project $1 2>/dev/null
gcloud run revisions list --region us-central1 --limit=1 --format="get(imageDigest)" | cut -d'@' -f2 2>/dev/null
