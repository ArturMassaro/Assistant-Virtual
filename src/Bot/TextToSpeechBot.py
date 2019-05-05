from Util.IbmConfigs import IbmConfigs as ibm
import os
class TextToSpeech:

    def convert(text):

        dialogFile = open("dialog.mp3", "wb")

        dialogFile.write(
            ibm.text_to_speech.synthesize(
                text,
                voice='pt-BR_IsabelaVoice',
                accept='audio/mp3'
            ).get_result().content
        )

        dialogFile.close()

        os.system('mpg123 dialog.mp3')
