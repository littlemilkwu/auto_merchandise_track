# auto merchandise track
## 專案說明

此專案主要是來追蹤 PTT 買賣相關版的商品更新<br>
每批次查詢會抓取目標商品最新的 20 筆貼文<br>
透過 IFTTT 的 webhook 和 line message<br>
回傳到自己的 LINE Notify 聊天室<br>
已經查詢過的商品<br>
會被加入到歷史資料的 csv 當中<br>
避免重複的查詢、回傳行為<br>

## 前置需求
### 1. 套件安裝
```
pip install requests pandas beautifulsoup4
```
### 2. IFTTT 設定
請參考以下文章建立 IFTTT 服務
https://www.oxxostudio.tw/articles/201803/ifttt-line.html

line message 回傳內容改成以下：
```
<br>title: {{Value1}}<br>
<br>url: {{Value2}} <br>
<br>content: <br>
<pre>{{Value3}} </pre>
```

### 3. .env 設定
將 .env.example 複製一份 .env<br>
並且在 .env 的 WEBHOOK_KEY 填入自己 webhook 獲得的值<br>


## 使用方法
可以自定義輸入

1. 每批次查詢間隔時間
2. 要關注的商品名稱
3. PTT 版
4. 結束時間

## TO-DO
* fix: 每次重啟都會重置
* 加入 request 回傳的