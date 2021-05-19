import requests
import bs4


def main():
    response = requests.get("https://www.topcoder.com/tc?module=ProblemArchive&sr=551&er=600")
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    soup.find()


main()
