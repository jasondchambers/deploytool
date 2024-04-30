# deploytool
Provides continuous delivery capability for websites deployed to Google Cloud.

## Step 1

Create a configuration file called websites.yml in your home directory:

    websites:
      - name: somewebsite
        url: somewebsite.com
        docker_repo: name/repo-jasonsblog
        gcloud_project: micro-wrench-416713

## Step 2

Login with gcloud:

    $ cloud auth application-default login

## Step 3

Install dependencies (probably best to create either a miniconda env or a venv):

    $ pip install -r requirements.txt

## Step 4 

Ensure the directory containing deploytool is in your PATH.

## Step 5 

Run deploytool as follows:

    $ python3 deploytool.py
