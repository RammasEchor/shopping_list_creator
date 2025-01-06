import gpsoauth

email = 'luis.nieto.palacios1996@gmail.com'
android_id = '10:3f:44:ab:a6:17'
token = 'oauth2_4/0AeaYSHAXZ-FKA7ACxBRjpkMOhkqBJKpFo77VLEVkKBGP1eM_JjDKOpj1pWIlM1tmrbqm3Q' # insert the oauth_token here

master_response = gpsoauth.exchange_token(email, token, android_id)
master_token = master_response['Token']

auth_response = gpsoauth.perform_oauth(
    email, master_token, android_id,
    service='sj', app='com.google.android.music',
    client_sig='...')
token = auth_response['Auth']