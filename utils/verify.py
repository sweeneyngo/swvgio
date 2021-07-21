import requests


def grab(url, params=None):
    try:
        r = requests.get(url, params=params, stream=True)
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print("Timed out...")
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print("Invalid URL, check its validity first.")
    except requests.exceptions.RequestException as e:
        print("Unknown error, exiting immediately.")
        raise SystemExit(e)

    return r
