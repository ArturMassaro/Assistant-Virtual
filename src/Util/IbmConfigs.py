import ibm_watson

class IbmConfigs:

    assistant = ibm_watson.AssistantV1(
        version='2019-02-28',
        iam_apikey='eApq7I0WsadxpNbGtJ-M1pvKz57KYUdWlrL8EU_2g2lf',
        url='https://gateway.watsonplatform.net/assistant/api'
    )
    workspace_id="2c1f36de-d1da-40b5-a8fc-be80de734b0c"

    text_to_speech = ibm_watson.TextToSpeechV1(
    iam_apikey='sUtFWeqRIF_NHzKtMGR0WmzJhzquLUcQ68DddiGVKNGK',
    url='https://gateway-wdc.watsonplatform.net/text-to-speech/api'
    )   

