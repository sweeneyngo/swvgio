import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


def validateOAuth2():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client_secret = "client_secret.json"
    scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]
    port = 8080

    credentials = None

    # Retrieves user's credentials from previous auth
    if os.path.exists("token.pickle"):
        print("Loading credentials . . .")
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

    # Check valid credentials
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("Refreshing access token . . .")
            credentials.refresh(Request())
        else:
            print("Fetching new tokens . . .")
            flow = InstalledAppFlow.from_client_secrets_file(client_secret, scopes)
            flow.run_local_server(port=port, prompt="consent", authorization_prompt_message="")
            credentials = flow.credentials

            # save credentials
            print("Saving for future use . . .")
            with open("token.pickle", "wb") as token:
                pickle.dump(credentials, token)

    youtube = build("youtube", "v3", credentials=credentials)
    return youtube
