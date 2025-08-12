import json
import requests

class GitHubRepoFetcher:
    def __init__(self):
        self.owner=None
        self.repo=None
    def set_repo(self,owner,repo):
        self.owner=owner
        self.repo=repo
    def fetch_details(self):
        try :
            url = f'https://api.github.com/repos/{self.owner}/{self.repo}'
            r = requests.get(url)
            r.raise_for_status()
            details=r.json()
            pretty_json = json.dumps(details, indent=4, sort_keys=True)
            return pretty_json
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
        
    def fetch_issues(self):
         url = f'https://api.github.com/repos/{self.owner}/{self.repo}/issues'
         r=requests.get(url)
         issues=r.json()
         if len(issues)==0:
             print("No open issue found")
         else:
             for i in issues:
                 print(f"{i['number']} - {i['title']} ({i['html_url']})")
             return issues
             
    
f=GitHubRepoFetcher()
f.set_repo("urmi1506","DSA-")
print(f.fetch_details())
f.fetch_issues()

        
