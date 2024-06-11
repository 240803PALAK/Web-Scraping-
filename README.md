# Web-Scraping-

    import requests
    from bs4 import BeautifulSoup
    
    url = "https://www.amazon.in/Oneplus-Celadon-Marble-128GB-Storage/dp/B0CX58MTNN/ref=sr_1_2_sspa?crid=SOVIK37SFJPM&dib=eyJ2IjoiMSJ9.y7M5hd-iDtOvnQOKpN9vDAL9QO4tLknpmTbxTddsIX2yIPbGAkRkXgbyW7WMSGzvPtAIaLpDNPiyvx4GOAn5TOv1ixtvtMqONFYHBeMjRPGqpe7RqUYFGwcDpTtHtNOAoJP0KbwakQIfz6j17q6xx3IS_IsHCdzQ3J8Cux8JOZxphM6m49JYLGvKYWf-hPCiYjZNIaUqGx9QUEMUx6J_uIWH2C0XoyM_0h36TWmuiqE.fCOHVCQo8pejhqboLdTXikqPyvaCz2JfgezVEL-o59E&dib_tag=se&keywords=phone&qid=1718116799&sprefix=phone%2Caps%2C319&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.prettify())
