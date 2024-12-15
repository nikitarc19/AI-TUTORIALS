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


# import win10toast
# from win10toast import ToastNotifier

# # create an object to ToastNotifier class
# n = ToastNotifier()

# n.show_toast("Saman is a Teacher", "You got notification", duration = 10, 
# icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")

# Create a timer to remind drink water in each 1 min

# how to call function in interval time.....
# call a funcation in interval




# def show_toasts():
#     m=ToastNotifier()
#     print('running')
#     m.show_toast("Drink water", "You got notification", duration = 1)

# import threading 
# t = threading.Timer(5.0,show_toasts)
# t.start()


# from win11toast import toast
# import threading
# import time

# def show_toast():
#     print("Notification is being displayed")
#     toast("Drink Water", "You got a notification")  # Provide a valid path


# # Set a timer to show the notification after 5 seconds
# t = threading.Timer(5.0, show_toast)
# t.start()

# # Keep the program running to avoid premature termination
# while threading.active_count() > 1:
#     time.sleep(0.1)


# from win11toast import toast

# image = {
#     'src': r'https://4.bp.blogspot.com/-u-uyq3FEqeY/UkJLl773BHI/AAAAAAAAYPQ/7bY05EeF1oI/s800/cooking_toaster.png',
#     'placement': 'hero'
# }

# toast('Saman', 'I Love You and Thank you for teaching.', image=image)


from win11toast import toast

image = {
    'src':r'C:\Users\SML\Documents\AItutorial1\Project\Images\41CnqyKmKgL.png',
    'placement': 'okay'
 }

toast('Will you be my boyFriend?', 'Click a button',buttons=['Approve', 'Dismiss', 'Other'],image=image)
toast('Samanuuuu', 'Which do you like?', selection=['ME', 'Mygirlfriend', 'Nikita?'], button='Submit')


