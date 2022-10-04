import requests 

UPLOAD_ENDPOINT_URL = "https://kxn3fbykyd.execute-api.ap-southeast-1.amazonaws.com/v1/coughsound/%7Bfilename%7D"
def send_to_aws(audio_buffer, filename):
    headers = {
        'Content-Type': 'audio/wave'
    }
    r = requests.put(
        UPLOAD_ENDPOINT_URL + filename,
        headers=headers,
        data=audio_buffer
    )
    return r