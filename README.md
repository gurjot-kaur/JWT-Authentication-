# JWT-Authentication

The authtest file contains a function that will create a user in the userpool, confirm user access, generate a refresh token(license key) and generate the access token for the api's secure end point. Once the refresh token is created for the first time, only the contructs for the access token can be ran the subsequent times until the expiration of the refresh token.


Run python authtest.py


Copy and save keys 

Run uvicorn authadd:app --reload --port 8000

Run uvicorn authmultiply:app --reload --port 8001


