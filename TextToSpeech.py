
  # authentacation:
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1

  # setting the url and apikey
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9f75a6c7-3307-4899-96b8-1b31286ee83c'
apikey = 'dfr_E7Qp28XC928ZaS3G1nKoCkzc-0ChwL2jhmKNpqIg'


def main():

    authenticator = IAMAuthenticator(apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)

    with open('text.txt', 'r') as f:
        text = f.read()

    with open('speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3',
                             voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)


if __name__ == "__main__":
    main()