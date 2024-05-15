# deploytool
Provides continuous delivery capability for websites deployed to Google Cloud from container images stored on DockerHub.

## Step 1

Create a configuration file called websites.yml in your home directory:

    websites:
      - name: somewebsite
        url: somewebsite.com
        service: www-art
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

Run deploytool as follows. In the example below, we have three websites - sketchyjason.com is out of date and so it deploys a new update:

    $ python3 deploytool.py

     python3 deploytool.py
    sketchyjason.com:
	    status: WebsiteStatus.OUT_OF_DATE
	    current deployed: yzxbmlf/www-art:9 04/28/2024, 17:50:04
	    latest available: yzxbmlf/www-art:10 04/30/2024, 19:06:36
	    deploying latest available: yzxbmlf/www-art:10
    Updated property [run/region].
    Deploying container to Cloud Run service [www-art] in project [www-art] region [us-central1]
    ✓ Deploying... Done.
      ✓ Creating Revision...
      ✓ Routing traffic...
    Done.
    Service [www-art] revision [www-art-00012-qz8] has been deployed and is serving 100 percent of traffic.
    Service URL: https://www-art-xyyhnvkh3q-uc.a.run.app
    ✓ Updating traffic...
      . Routing traffic...
    Done.
    URL: https://www-art-xyyhnvkh3q-uc.a.run.app
    Traffic:
      100% LATEST (currently www-art-00012-qz8)
    circleinaspiral.com:
	    status: WebsiteStatus.UPTO_DATE
	    current deployed: yzxbmlf/www-jasonsblog:48 04/29/2024, 16:58:04
	    latest available: yzxbmlf/www-jasonsblog:48 04/29/2024, 16:58:04
    stratfordremodel.com:
	    status: WebsiteStatus.UPTO_DATE
	    current deployed: yzxbmlf/www-house:16 04/30/2024, 18:44:17
	    latest available: yzxbmlf/www-house:16 04/30/2024, 18:44:17
