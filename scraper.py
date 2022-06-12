from typing import List
import bs4, requests

class scraperClass:
    def __init__(self) -> None:
        self.link_list = []

    def get_sourceGames(self, payload: str) -> str:
        source = requests.get(f"https://steamunlocked.net/?s={payload.lower()}").text
        return source


    def extractGames(self, source, target: str):
        soup = bs4.BeautifulSoup(source, features="html.parser")
        list = soup.find_all("a")
        if list:
            for a in list:
                if target.lower() in a.get("href") and "free-download" in a.get("href"):
                    self.link_list.append(a.get("href"))


    def getGames(self, target) -> List:
        self.extractGames(self.get_sourceGames(target), target)

        new_link_list = list(set(self.link_list))
        self.link_list.clear()

        return new_link_list


    def get_sourceGoogle(self, payload: str) -> str:
        source = requests.get(f"https://www.google.com/{payload.lower()}").text
        return source


    def extractSites(self, source, target):
        soup = bs4.BeautifulSoup(source, features="html.parser")
        list = soup.find_all("a")
        if list:
            for a in list:
                if target.lower() in a.get("href"):
                    self.link_list.append(a.get("href"))


    def getSites(self, target):
        self.extractSites(self.get_sourceGoogle(target), target)

        new_link_list = list(set(self.link_list))
        self.link_list.clear()

        return new_link_list
        


if __name__ == "__main__":
    obj = scraperClass()
    print(obj.getSites("martinpescatore"))
    #print(obj.getGames("SONIC"))


