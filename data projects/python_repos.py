import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print "Status code:", r.status_code

response_dict = r.json()
# print response_dict.keys()

print "Total repositories:", response_dict['total_count']

#explore
repo_dicts = response_dict['items']
print "Respositories:", len(repo_dicts)

repo_dict = repo_dicts[0]
print "\nKeys:", len(repo_dict.keys())
for key in sorted(repo_dict.keys()):
    print(key)




