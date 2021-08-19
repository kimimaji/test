from selenium import webdriver
import time

class webGet():

    # webdriver設定
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_options)

    # SITE
    URLs = {
        # 'rs':"https://jp.rs-online.com/web/c/connectors/pcb-connectors-wire-housings/pcb-sockets/?searchTerm=",
        # 'chip1stop':"https://www.chip1stop.com/view/searchResult/SearchResultTop?partSameFlg=true&keyword=",
        # 'digikey':"https://www.digikey.jp/products/ja?pkeyword=&keywords=",
        'google検索':"https://www.google.co.jp/search?q=",
        'yahoo検索':"https://search.yahoo.com/search?p=",
        }

    def PageTitle ( self, searchKeyword ) :

        all_items = {}
        for i,url in enumerate(self.URLs.values()):
            print(url + searchKeyword)
            self.browser.get(url + searchKeyword)
            time.sleep(1)

            all_items[i] = format(self.browser.title)
        self.browser.quit()

        return all_items
    
