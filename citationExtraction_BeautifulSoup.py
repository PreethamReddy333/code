import requests
from bs4 import BeautifulSoup
def get_citation(title,year=' ',volume=' ',pages=' '):
    #Format the search query
    query = f"{title} {year} {volume} {pages}"
    #query = query.replace(' ','+')
    url = f"https://scholar.google.com/scholar?q={query}"
    #send a GET request to google scholar portal
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #find the first search result
    result = soup.find('div',{'class':'gs_ri'})
    if result:
        #Extract the citation text
        citation = result.find('div',{'class':'gs_a'}).text
        return citation
    else:
        return "citation not found"
#driver code with an example
article_title = "Personalized collaborative filtering recommender system using domain knowledge"
article_year= " "
article_volume =" "
article_pages =" "
citation = get_citation(article_title,article_year,article_volume,article_pages)
print(citation)







