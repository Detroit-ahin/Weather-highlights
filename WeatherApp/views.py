from django.shortcuts import render
# import json to load json data to python dictionary
import urllib.request
# urllib.request to make a request to api
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        #''' api key might be expired use your own api_keyplace api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API
        # print(city)
        api_url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=19271528f8b9badf220b6280c99116e8').read()
        api_url2 = json.loads(api_url)
                # converting JSON data to a dictionary


        data = {
            "country": city,
            "weather_description": api_url2['weather'][0]['description'],
            "weather_temperature": api_url2['main']['temp'],
            "weather_pressure": api_url2['main']['pressure'],
            "weather_humidity":api_url2['main']['humidity'],
            "weather_icon": api_url2['weather'][0]['icon'],
        }
                # data for variable list_of_data

    else:
        city = None
        data = {
            "country": None,
            "weather_description": None,
            "weather_temperature": None,
            "weather_pressure": None,
            "weather_humidity":None,
            "weather_icon": None,
        }
        #showing none
    print(data['weather_icon'])
    return render(request, 'index.html', {"city": city, "data" :data})
    
    