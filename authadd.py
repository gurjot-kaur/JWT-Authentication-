from fastapi import FastAPI, Depends
from fastapi_cloudauth.cognito import Cognito, CognitoCurrentUser, CognitoClaims
from pydantic import BaseModel, Field

app = FastAPI()


auth = Cognito(region= "us-east-1", userPoolId= "us-east-1_K7UQ0DJz9")
get_current_user_add = CognitoCurrentUser(region= "us-east-1", userPoolId= "us-east-1_K7UQ0DJz9")


@app.get("/add")
def read_item(a: int, b: int,current_user: CognitoClaims = Depends(get_current_user_add)):
    return (a+b)


    

    