import requests 

UPLOAD_ENDPOINT_URL = "https://kxn3fbykyd.execute-api.ap-southeast-1.amazonaws.com/v1/coughsound/"
NEW_UPLOAD_ENDPOINT_URL = "https://4tm1htfzw1.execute-api.ap-southeast-1.amazonaws.com/v1/swinburne-cofe/"

def send_to_aws(audio_buffer, filename):
    headers = {
        'Content-Type': 'audio/wave'
    }
    r = requests.put(
        NEW_UPLOAD_ENDPOINT_URL + filename,
        headers=headers,
        data=audio_buffer
    )
    return r