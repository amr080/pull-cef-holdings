import requests
import csv

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
fund_ticker = 'BRW'

# Make the API request to retrieve holdings data
response = requests.get(api_url + f'holding/{fund_ticker}/full', headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    data = response.json()
    
    # Process the retrieved holdings data
    holdings = data
    csv_data = []
    headers = ['Name', 'Holding Type', 'Shares', 'Settlement Price', 'Market Value', 'Coupon Rate',
               'Client Sector', 'Client Country', "Moody's Rating", 'S&P Rating', 'Maturity']
    
    csv_data.append(headers)
    
    for holding in holdings:
        row = [
            holding['name'],
            holding['holdingtype'],
            holding['shares'],
            holding['settlementprice'] if 'settlementprice' in holding and holding['settlementprice'] is not None else "",
            holding['marketvalue'],
            holding['rate'] if 'rate' in holding and holding['rate'] is not None else "",
            holding.get('clientsector', ''),
            holding.get('clientcountry', ''),
            holding.get('moodysRating', ''),
            holding.get('sandPRating', ''),
            holding['futuredate'] if 'futuredate' in holding and holding['futuredate'] is not None else ""
        ]
        csv_data.append(row)
    
    # Write the data to a CSV file
    with open('holdings.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    
    print("Holdings data exported to 'holdings.csv' file.")
else:
    # Request failed
    print(f'Request failed with status code: {response.status_code}')
    print('Response content:', response.text)