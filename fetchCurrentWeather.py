import urllib.request
import json

def weather_fetcher():
    
    # User determines whether to enter city or zip code
    n = input("Would you like to enter City or ZIP? ")

    if n == "City" or n == "city" or n == "CITY":
        city_name = input("Enter Name of City: ")

        response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&units={}&APPID={}".format(city_name, 'imperial', 'a748d4cee36119dedfc8827a2c6cb125'))

        # Convert the json data into a list
        weather_data = json.loads(response.read().decode('utf8'))

        # Print the weather
        print('City:    ' + weather_data['name'])
        print('Weather: ' + weather_data['weather'][0]['main'])
        print('Temp:    ' + str(weather_data['main']['temp']))

    elif n == "Zip" or n == "zip" or "ZIP":
        zip_code = input("Enter Zip Code: ")

        response = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?zip={}&units={}&APPID={}".format(zip_code, 'imperial', 'a748d4cee36119dedfc8827a2c6cb125'))

        # Convert the json data into a list
        weather_data = json.loads(response.read().decode('utf8'))

        # Print the weather
        print('City:    ' + weather_data['name'])
        print('Weather: ' + weather_data['weather'][0]['main'])
        print('Temp:    ' + str(weather_data['main']['temp']))

    else:
        print("No option found.")
        input("Press Enter..")
        exit()

if __name__ == "__main__":
    weather_fetcher()
    input('Enter...')
