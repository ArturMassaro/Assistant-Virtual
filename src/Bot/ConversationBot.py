import json
import ibm_watson
from Util.IbmConfigs import IbmConfigs as ibm

class botConversation():

    def Conversation(dialog):
        response = ibm.assistant.message(
         workspace_id=ibm.workspace_id,
            input={
                'text': dialog
            }
        ).get_result()
        result = response["output"]["text"]
        return result