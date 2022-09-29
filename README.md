<h2 align="center">Telegram bots</h2>

### 1) TravelBot
This bot can show you information about exchange rates and weather (preset and custom ones).
Also it can transliterate text from latin form to armenian(east/west) or georgian. 

#### Start:
Try @ArmeniaGeorgiaInfoBot in Telegram

#### Development:
##### 1) Clone this repository
    git clone <link>
##### 2) Create a .env file (mine in TravelBot directory)
    BOT_TOKEN = <TOKEN OF YOUR TELEGRAM BOT>
    WEATHER_AP = https://api.openweathermap.org/data/2.5/weather?q={0}&appid=<YOUR API KEY>&units=metric
    CURRENCY_API=https://api.getgeoapi.com/v2/currency/convert?api_key=<YOUR ANOTHER API KEY>&from={0}&to={1}&amount=1&format=json
    HEROKU_APP_NAME=<NAME OF YOUR HEROKU APPLICATION>