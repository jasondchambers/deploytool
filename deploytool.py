import os
import yaml
import website

def load_websites_from_yaml(filename):
    home_dir = os.path.expanduser("~")
    filename = os.path.join(home_dir, "websites.yml")
    with open(filename, "r") as file:
        websites_data = yaml.safe_load(file)
    return [
        website.Website(
            url=site["url"],
            docker_repo=site["docker_repo"],
            gcloud_project=site["gcloud_project"]
        )
        for site in websites_data["websites"]
    ]

def main():
    websites = load_websites_from_yaml("websites.yml")
    for site in websites:
        site.check_for_updates()
        print(f"{site.url}:")
        print(f"\tstatus: {site.website_status}")
        print(f"\tcurrent deployed: {site.current_deployed()} {site.date_of_current_deployed()}")
        print(f"\tlatest available: {site.latest_available()} {site.date_of_latest_available()}")

if __name__ == "__main__":
    main()
