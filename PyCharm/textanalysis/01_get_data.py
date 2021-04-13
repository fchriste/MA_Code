from bs4 import BeautifulSoup
import urllib.request
import json
import requests

#change topic of data, either 'rhb' or 'lavaux'
topic="rhb"

# define directories
output_path= "data/01_get_data/%s/" % topic


# define url with query string
search_url = 'https://www.e-periodica.ch/digbib/dossearch?'

# define search query
search = {
    'ssearchtext': topic
}

# define empty list to save pids
list_pid = list()

page_number = 0

# get element next page which defines end of loop
next_page = '/digbib/hitlist?p=pn'

while True:
    # define url to iterate through the different pages
    page_url = 'https://www.e-periodica.ch/digbib/hitlist?p=pi%d' % page_number
    # open session to get query results of all pages
    with requests.Session() as session:
        # set post url with search query
        post = session.post(search_url, data=search)
        # get search result of respective page
        r = session.get(page_url)
        # use html parser to extract all links
        soup = BeautifulSoup(r.text, "html.parser")

        # define empty list to get stop criteria
        links_n = list()

        # loop through page to get links
        for link in soup.findAll('a'):
            # save links as variables
            all_links = link.get('href')
            links_n.append(all_links)
            # extract 'pids' if available
            if 'pid' in all_links:
                # split links after 'pid'
                end_link = all_links.split("pid=", 1)[1]
                # split links to extract pid only
                pid = end_link.split("&", 1)[0]
                # append existing list with pid if not already in list
                if pid not in list_pid:
                    list_pid.append(pid)

    # check if next page element is present
    if next_page in links_n:
        page_number += 1
        print("1: %d" % page_number)
    # next page element is not present, final page is reached
    else:
        break
# initiate counter for logging
log_counter = 0
print("length of list")
print(len(list_pid))
# iterate through all pids
for i in list_pid:
    # open link to each pid to get json
    with urllib.request.urlopen("https://www.e-periodica.ch/digbib/ajax/pageinfo?pid=%s" % i) as url:
        # save data variable
        data = json.loads(url.read().decode())

    # write json file in data folder named after {pid}.json
    with open('%s/%s.json' % (output_path,i), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
    print("2: %d" % log_counter)
    log_counter += 1
