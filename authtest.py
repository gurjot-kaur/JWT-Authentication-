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

    r = cidp.admin_initiate_auth(
        UserPoolId= upi,
        ClientId= ci,
        AuthFlow= "ADMIN_NO_SRP_AUTH",
        AuthParameters= {
        "USERNAME": user,
        "PASSWORD": pwd
        })
	
    return(r["AuthenticationResult"]["IdToken"])

print("both key " + sign_up_cognito("c5f6c663b8iao253ldma34hg3","us-east-1_EOLt1gUue","b","pass123"))#both

print("add key " + sign_up_cognito("o2rjrh1h2snpr7c4o8od020n3","us-east-1_K7UQ0DJz9","b","pass123"))#add

print(" multiply key " + sign_up_cognito("mfdrj41c4poh17dk0u3u21sck","us-east-1_ub6wJLSeX","b","pass123"))#multiply