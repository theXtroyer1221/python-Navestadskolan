import json
import requests

class app:
  def convert_USD_SEK(self, number):
    
    r = requests.get('https://free.currconv.com/api/v7/convert?apiKey=do-not-use-this-key&q=USD_SEK&compact=ultra')

    data = r.json()

print(data["USD_SEK"])
    #Detta function tar in hur mycket USD och kollar hur mycket SEK det är i nätet, sedan räcknar det ut priset 
    mulnumber = float(number) / 100 
    print(f"{number}cm är {mulnumber}m")

print("Genom att dela med hundra får vi cm till m")
#input från användaren
USD = input("hur mycket USD?: ")
app.convert_USD_SEK(app, USD)
 
