import requests

def findTemperatureLive():  
    """Print the current temperature in Boston using data from boston.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!  The page structure changed
    during Summer 2021.  The code below works as of 2021-08-26.
    """

    # Get the weather page
    weather = requests.get("https://www.boston.com/weather").text
    # The temperature can be found after the span class label
    # "local-weather__current-info-temp" and immediately before the
    # HTML code "<sup>&deg</sup>; (the superscript degree symbol)
    curLoc = weather.find("local-weather__current-info-temp")
    if curLoc != -1:
        # Now, find the degree symbol ("<sup>&deg;") following the temperature
        degLoc = weather.find("<sup>&deg", curLoc)
        # The temperature number is preceded by an HTML tag
        tempLoc = weather.rfind(">", 0, degLoc)
        # Temperature value is everything between the tag and the degree symbol
        print("Temperature in Boston is",weather[tempLoc+1:degLoc], "degrees")
    else:
        print("Page format has changed; cannot find the temperature")

if __name__ == "__main__":
    findTemperatureLive()
