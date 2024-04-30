import requests
from datetime import datetime

def get_image_tags(repository):
    url = f"https://hub.docker.com/v2/repositories/{repository}/tags/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tags = data.get('results', [])
        return tags
    else:
        print(f"Failed to fetch tags for repository {repository}. Status code: {response.status_code}")
        return []

def find_most_recent_tag(tags):
    if not tags:
        return None
    most_recent_tag = None
    most_recent_date = None
    for tag in tags:
        creation_date = datetime.fromisoformat(tag['last_updated'].replace('Z', '+00:00'))
        if creation_date:
            if most_recent_date is None or creation_date > most_recent_date:
                most_recent_date = creation_date
                most_recent_tag = tag
    return most_recent_tag

def find_tag(tags, search_for_digest):
    if not tags:
        return None
    found_tag = None
    for tag in tags:
        if tag.get('digest') == search_for_digest:
            # Found
            found_tag = tag
    return found_tag
