import requests

# API endpoint URL
api_url = 'https://secure.alpsinc.com/MarketingAPI/api/v1/'

# Authentication token
token = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIxNzE4MTQ0ODM1IiwianRpIjoiNzZhMTU3NTAtMWRjYi00NjVjLWEzZTItMzcwYzA2MDM5Nzc4IiwiaXNzIjoid3d3LnNhYmFjZWYuY29tIiwic3ViIjoiaHR0cHM6Ly9zZWN1cmUuYWxwc2luYy5jb20vTWFya2V0aW5nQVBJL2FwaS92MS9Ub2tlbi9OZXciLCJuYmYiOiIxNzE4MTQ0ODM1IiwiZXhwIjoiMTcxODIzMTIzNSIsIm1rdCI6ImZhbHNlIn0.D9OGuXHWY6lNb4SkL8LznMA1AzFmZb7OOV2jF9OGEBaU-avNmzN4WADjU56Ax2exSfT8-T7rNZXh6Txuie_93g'

# Set the request headers
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Specify the fund ticker symbol
fund_ticker = 'JEQ'

# Make the API request to retrieve holdings data
response = requests.get(api_url + f'dailyprice/{fund_ticker}', headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    data = response.json()
    # Process the retrieved data
    print(data)
else:
    # Request failed
    print(f'Request failed with status code: {response.status_code}')
    print('Response content:', response.text)