import requests
from urllib import parse
from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import os
load_dotenv()

class AutoMerchandiseTrack:
    PTTHOST = 'https://www.ptt.cc/bbs/'
    TITLE_KEYWORD = ['賣', '販', '售']
    WEBHOOK_KEY = os.getenv('WEBHOOK_KEY')
    def __init__(self, time_interval, merchandise, board, stop_time):
        self.time_interval = time_interval
        self.merchandise = parse.quote(merchandise)
        self.board_url = self.PTTHOST + board
        self.stop_time = datetime.fromisoformat(stop_time)
        self.filename = f'./history_track/track_{merchandise.replace(" ", "_")}_{board}.csv'
        
        if (~os.path.isfile(self.filename)):
            df_init = pd.DataFrame(columns=['id', 'title', 'url'])
            df_init.to_csv(self.filename, index=False)
    
    def search(self):
        df_history = pd.read_csv(self.filename)
        id_history = df_history['id'].tolist()

        html_text = requests.get(f'{self.board_url}/search?q={self.merchandise}').text
        bs = BeautifulSoup(html_text, 'lxml')
        re_items = bs.select('.r-ent .title a')
        re_items.reverse()
        re_ls = []
        for item in re_items:
            temp_dict = {}
            temp_dict['id'] = item['href'].split('/')[-1]
            temp_dict['title'] = item.text
            temp_dict['url'] = f"{self.board_url}/{temp_dict['id']}"
            re_ls.append(temp_dict)

        for re_dict in re_ls:
            if (re_dict['id'] not in id_history):
                if any(KEYWORD in re_dict['title'] for KEYWORD in self.TITLE_KEYWORD):
                    re_dict['content'] = self.get_content(re_dict['url'])
                    self.send_line(
                        re_dict['title'], 
                        re_dict['url'],
                        re_dict['content']
                    )
                df_append = pd.DataFrame([[re_dict['id'], re_dict['title'], re_dict['url']]], columns=['id', 'title', 'url'])
                df_history = pd.concat([df_history, df_append], axis=0)
                df_history.to_csv(self.filename, index=False, encoding='utf-8-sig')
            sleep(5)
        
            
    def get_content(self, url):
        html_text = requests.get(url).text
        bs = BeautifulSoup(html_text, 'lxml').select('.article-metaline')[-1]
        content = bs.next_sibling
        return content

    def send_line(self, title, url, content):
        requests.post(
            f'https://maker.ifttt.com/trigger/line/with/key/{self.WEBHOOK_KEY}',
            data={'value1': title, 'value2': url, 'value3': content}
        )

    def start_tracking(self):
        now_datetime = datetime.now() # init
        while (now_datetime < self.stop_time):
            print('HITS : ', now_datetime)
            self.search()
            sleep(self.time_interval)
            now_datetime = datetime.now() # update


if __name__ == "__main__":
    pass