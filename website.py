import subprocess
from datetime import datetime
from enum import Enum
import dockerhub

class WebsiteStatus(Enum):
    UNKNOWN = 1
    UPTO_DATE = 2
    OUT_OF_DATE = 3
    NOT_DEPLOYED = 4
        
class Website:

    def __init__(self, url, docker_repo, gcloud_project):
        self.url = url
        self.docker_repo = docker_repo
        self.gcloud_project = gcloud_project
        self.digest_currently_deployed = self.get_current_revision()
        self.tags = dockerhub.get_image_tags(self.docker_repo)
        self.currently_deployed_tag = dockerhub.find_tag(tags=self.tags,search_for_digest=self.digest_currently_deployed)
        self.most_recent_tag = dockerhub.find_most_recent_tag(tags=self.tags)
        self.website_status = WebsiteStatus.UNKNOWN

    def check_for_updates(self):
        if self.most_recent_tag:
            if self.digest_currently_deployed != None:
                if self.most_recent_tag['digest'] == self.currently_deployed_tag['digest']:
                    self.website_status = WebsiteStatus.UPTO_DATE
                else:
                    self.website_status = WebsiteStatus.OUT_OF_DATE
            else:
                self.website_status = WebsiteStatus.NOT_DEPLOYED

    def current_deployed(self):
        tag_name = None
        if self.currently_deployed_tag:
            tag_name = self.currently_deployed_tag['name']
        return f"{self.docker_repo}:{tag_name}"

    def date_of_current_deployed(self):
        if self.currently_deployed_tag:
            current_deployed_date = datetime.fromisoformat(self.currently_deployed_tag['last_updated'].replace('Z', '+00:00'))
            return current_deployed_date.strftime("%m/%d/%Y, %H:%M:%S")
        else:
            return ""

    def latest_available(self):
        tag_name = None
        if self.most_recent_tag:
            tag_name = self.most_recent_tag['name']
        return f"{self.docker_repo}:{tag_name}"

    def date_of_latest_available(self):
        if self.most_recent_tag:
            latest = datetime.fromisoformat(self.most_recent_tag['last_updated'].replace('Z', '+00:00'))
            return latest.strftime("%m/%d/%Y, %H:%M:%S")
        else:
            return ""

    def get_current_revision(self):
        current_revision = subprocess.run(['current_revision.sh', self.gcloud_project], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        return current_revision
