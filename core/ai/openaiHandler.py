import sys
from core.ai.env import OPENAI_API_KEY
from openai import OpenAI
import time as t

client = OpenAI(api_key=OPENAI_API_KEY)
assistants = {"Seer_resume" : "asst_Gok4cxceSXmNfNDIWBwWc4Yq", "Seer_img" : "6BtoIKz3hnfjGkVmT8JCMb7c"}

def newAiThread():
    thread = client.beta.threads.create() #On crée le thread, une conversation
    return thread

def askAIfor(msg,thread,type="txt"):
    message = client.beta.threads.messages.create(  #On crée un message de l'utilisateur sur le thread.
        thread.id,
        role="user",
        content=msg
    )

    if type == "txt":
        assistant = assistants["Seer_resume"]
    if type == "img":
        assistant = assistants["Seer_img"]

    run = client.beta.threads.runs.create( #On fait tourner l'ia sur le thread
        thread_id=thread.id,
        assistant_id=assistant
    )

    while True:  #On attend que l'ia ai fait son boulot
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status == "completed":
            messages = client.beta.threads.messages.list( #On récupère la liste des messages
                thread_id=thread.id
                )
            return messages.data[0].content[0].text.value
            break
        if run.status == "expired":
            return False
            break
        else:
            t.sleep(3)



