import sys
from openai import OpenAI
import time as t
from pathlib import Path
from .env import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)
assistants = {"Seer_resume" : "asst_oM08cV3EApkYChIY39JV24zI", "Seer_img" : "asst_v25VFWtDYmeluDwi7C5PzyMV"}


def newAiThread():
    thread = client.beta.threads.create() #On crée le thread, une conversation
    return thread

def askAIfor(target,thread,type="txt"):

    if type == "txt":
        assistant = assistants["Seer_resume"]
        contentSent=target
    if type == "img":
        assistant = assistants["Seer_img"]
        target = "media/"+target
        file_path = Path(__file__).parent.parent.parent / target
        img = client.files.create(file= open(file_path, "rb"),purpose="vision")
        id = img.id
        contentSent=[{
            "type": "image_file",
            "image_file" : {
                "file_id": id,
                "detail": "low"
            }
        }]

    message = client.beta.threads.messages.create(  #On crée un message de l'utilisateur sur le thread.
    thread.id,
    role="user",
    content=contentSent
    )

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
            if type == "img":
                client.files.delete(id)
            return messages.data[0].content[0].text.value
            break
        if run.status == "expired":
            return False
            break
        else:
            t.sleep(3)



