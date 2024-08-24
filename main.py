import requests
from datetime import datetime

print("--------___------------------Prayer Times Application in Python------------------___--------")

now = datetime.now()

def convert_to_12hr(time_str):
    """Converts a 24-hour time string to 12-hour format with AM/PM."""
    hour = int(time_str[:2])
    minute = time_str[3:]
    period = "Am"

    if hour >= 12:
        period = "Pm"
        if hour > 12:
            hour -= 12
    elif hour == 0:
        hour = 12
    
    return f"{str(hour).zfill(2)}:{minute} {period}"


run = True
while run:
    CITY = input("\nEnter a City name:  ")
    COUNTRY = input(f"Where is {CITY}?  ").replace(" ", "+")

    BASE_URL = f"https://api.aladhan.com/v1/timingsByCity/{now.day}-{now.month}-{now.year}?city={CITY}&country={COUNTRY}"

    try:
        response = requests.get(BASE_URL)
        data = response.json()

        if "data" in data:
            Fajr = data['data']['timings']['Fajr']
            Dhuhr = data['data']['timings']["Dhuhr"]
            Asr = data['data']['timings']["Asr"]
            Maghrib = data['data']['timings']["Maghrib"]
            Isha = data['data']['timings']["Isha"]

            # Convert prayer times to 12-hour format 
            Fajr = convert_to_12hr(Fajr)
            Dhuhr = convert_to_12hr(Dhuhr)
            Asr = convert_to_12hr(Asr)
            Maghrib = convert_to_12hr(Maghrib)
            Isha = convert_to_12hr(Isha)

            print(f"\nFajr: {Fajr}\nDhuhr: {Dhuhr}\nAsr: {Asr}\nMaghrib: {Maghrib}\nIsha: {Isha}")
        else:
            print(f"No data found for the given {CITY}/{COUNTRY}.")

    except:
        print(f"Error: Unable to fetch data.")

    run = input("\nContinue this program?  ").lower()
    if run != "yes":
        if run != "no":
            print("Invalid input!")
        run = False
