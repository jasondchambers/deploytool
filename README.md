# deploytool
Provides continuous delivery capability for websites deployed to Google Cloud from container images stored on DockerHub.

## Step 1

Create a configuration file called websites.yml in your home directory:

    websites:
      - name: somewebsite
        url: somewebsite.com
        docker_repo: name/repo-jasonsblog
        gcloud_project: micro-wrench-416713

## Step 2 

Install [gcloud CLI](https://cloud.google.com/sdk/docs/install-sdk).

## Step 3

Login with gcloud:

    $ gcloud auth application-default login

## Step 4

Install dependencies (probably best to create either a miniconda env or a venv):

    $ pip install -r requirements.txt

## Step 5 

Ensure the directory containing deploytool is in your PATH.

## Step 6 

Run deploytool as follows:

    $ python3 deploytool.py

    sketchyjason.com:
            status: WebsiteStatus.UPTO_DATE
            current deployed: yzxbmlf/www-art:9 04/28/2024, 17:50:04
            latest available: yzxbmlf/www-art:9 04/28/2024, 17:50:04
    circleinaspiral.com:
            status: WebsiteStatus.UPTO_DATE
            current deployed: yzxbmlf/www-jasonsblog:48 04/29/2024, 16:58:04
            latest available: yzxbmlf/www-jasonsblog:48 04/29/2024, 16:58:04
    stratfordremodel.com:
            status: WebsiteStatus.OUT_OF_DATE
            current deployed: yzxbmlf/www-house:14 04/24/2024, 00:23:25
            latest available: yzxbmlf/www-house:13 04/24/2024, 02:00:31

TODO - does not yet deploy the latest version if it is out of date. Make it so.
