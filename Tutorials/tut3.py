# # import required libraries 
# import requests 
# from bs4 import BeautifulSoup 
# from win10toast import ToastNotifier 

# # create an object to ToastNotifier class 
# n = ToastNotifier() 

# # define a function 
# def getdata(url): 
# 	r = requests.get(url) 
# 	return r.text 
	
# htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 

# soup = BeautifulSoup(htmldata, 'html.parser') 

# current_temp = soup.find("span", attrs={"data-testid": "TemperatureValue"})
# chances_rain = soup.find("div", attrs={"data-testid": "precipValue"})

# temp = current_temp.text if current_temp else "N/A"
# temp_rain = chances_rain.text if chances_rain else "N/A"

# result = f"Current temperature: {temp} in Patna Bihar\nChances of rain: {temp_rain}"
# n.show_toast("live Weather update", 
# 			result, duration = 10) 





from win10toast import ToastNotifier 
