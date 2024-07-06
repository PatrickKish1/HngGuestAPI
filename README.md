# HNG INTERNSHIP

## Description

This web application displays the user's public IP address and provides weather information based on the user's location. Users can enter their name, and the application will greet them and show the temperature in their location.

## Hosted Endpoint

The application is hosted at: [https://hng-guest-api-grayshadow.replit.app/](https://hng-guest-api-grayshadow.replit.app/)

## Features

- Displays the user's public IP address.
- Allows users to input their name.
- Fetches the user's location using the public IP address.
- Provides current weather information for the user's location.
- Updates the URL to include the user's name.

## Usage

1. Open the hosted application at [https://hng-guest-api-grayshadow.replit.app/](https://hng-guest-api-grayshadow.replit.app/).
2. The page will display your public IP address.
3. Enter your name in the input box provided.
4. Click the "Get Weather" button.
5. The application will display your IP address, location, and a greeting with the current temperature in your location.
6. The URL will update to include your name.

## API Endpoints

- `GET /api/hello?visitor_name=<YourName>&visitor_ip=<YourIP>`: Fetches the IP, location, and weather information and returns a greeting.
