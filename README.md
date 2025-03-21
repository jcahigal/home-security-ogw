# Home Security Project - Docker Execution Guide

## Prerequisites

- Docker installed on your system.
- local connection with home assistant

## Build the Docker Image
To build the Docker image, run the following command in the project directory:

> docker build -t home-security-ogw .


## Running the Container

The application requires the following environment variables:

- OGW_CLIENT_ID: Your OpenGateway API client ID
- OGW_CLIENT_SECRET: Your OpenGateway API client secret
P- HONES: Comma-separated list of phone numbers to check (in international format)
- HOME_COORDINATES: Comma-separated latitude and longitude of your home (e.g., "40.4168,3.7038")
- ALL_OUTDOORS_WEBHOOK_ID: The ID of the webhook to call when all phones are outdoors
- SOMEONE_HOME_WEBHOOK_ID: The ID of the webhook to call when someone is homes

Run with environment variables:

```
docker run -e OGW_CLIENT_ID=your_client_id \
           -e OGW_CLIENT_SECRET=your_client_secret \
           -e PHONES="+34600000000,+34611111111" \
           -e HOME_COORDINATES="40.4168,-3.7038" \
           -e ALL_OUTDOORS_WEBHOOK_ID=your_all_outdoors_webhook_id \
           -e SOMEONE_HOME_WEBHOOK_ID=your_someone_home_webhook_id \
           home-security-ogw
```


## TODOs
- Packaging the code
- Manage mobiles as devices in Home Assistant with state *at-home*, *outdorrs*
  - Service from Telefonica to manage all devices from a contract
- Google home integration with OGW to get precise in/out home   