# import requests

# url = "https://restcountries.com/v3.1/all"
# response = requests.get(url)

# if response.status_code == 200:
#     countries = response.json()
#     print(countries)
#     # for country in countries:
#     #     print(f"Name: {country['name']['common']}, Region: {country.get('region', 'N/A')}")
# else:
#     print("Failed to fetch data")