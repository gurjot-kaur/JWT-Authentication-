import boto3

def sign_up_cognito(ci,upi,user,pwd):
    cidp = boto3.client('cognito-idp')

    cidp.sign_up(
        ClientId= ci,
        Username= user,
        Password= pwd)
						                          
    cidp.admin_confirm_sign_up(
        UserPoolId= upi,
        Username= user)

    r = cidp.admin_initiate_auth( #first login 
        UserPoolId= upi,
        ClientId= ci,
        AuthFlow= "ADMIN_NO_SRP_AUTH",
        AuthParameters= {
        "USERNAME": user,
        "PASSWORD": pwd
        })   
        
    m = cidp.admin_initiate_auth( #further logins
        UserPoolId= upi,
        ClientId= ci,
        AuthFlow= "REFRESH_TOKEN_AUTH",
        AuthParameters= {
        "REFRESH_TOKEN" : r["AuthenticationResult"]["RefreshToken"]
        })
	
    return(m["AuthenticationResult"]["IdToken"])
     

print("add key " + sign_up_cognito("o2rjrh1h2snpr7c4o8od020n3","us-east-1_K7UQ0DJz9","b","pass123"))#add

print(" multiply key " + sign_up_cognito("mfdrj41c4poh17dk0u3u21sck","us-east-1_ub6wJLSeX","b","pass123"))#multiply
