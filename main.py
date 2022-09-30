from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/getTimesStories')
def latest_stories():
    import requests
    from bs4 import BeautifulSoup as bs
    try:
        url = "https://time.com/"
        web_page = requests.get(url)
        soup = bs(web_page.content,'html5lib')
        card = soup.find("div", attrs = {"class": "partial latest-stories"})
        latest_heading = card.find('ul')
        final_data = list()
        for data_ele in latest_heading.find_all('a', href=True):
            final_data.append({'title': data_ele.text.strip().replace('\n', ''), 'link': "https://time.com" + str(data_ele['href'])})
        return final_data
    except Exception as e:
        return [{"Exception": str(e)}]
    
    

if __name__  == "__main__":
   app.run(debug=True, port = 8000)
    