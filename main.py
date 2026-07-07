
import os
from datetime import date
from random import randint
from huggingface_hub import InferenceClient
from PIL import PngImagePlugin
from randst import generate_random_string as ras
from dotenv import load_dotenv
load_dotenv()

hf_token = os.getenv("HF_TOKEN")

models=["flux","krea","flux-real"]
model_dir={
    "flux":{
        "x_model":"black-forest-labs/FLUX.1-schnell",
        "x_provider":"nscale"
    },
    "flux-real":{
        "x_model":"XLabs-AI/flux-RealismLora",
        "x_provider":"fal-ai"
    },
    "krea":{
        "x_model":"krea/Krea-2-Turbo",
        "x_provider":"fal-ai"
    }
}
req_new=True

def generate(client,x_model):
    prompt = input("Enter your prompt >>> ")
    while True:
        try:
            h , w = input("Dimentions [h w]>>> ").split()
        except:
            print('Error')
            continue
        else:
            break
            
    # output is a PIL.Image object
    image = client.text_to_image(
        prompt,
        height= int(h),
        width= int(w),
        model=x_model,
    )
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Prompt",prompt)

    name = str(date.today())+"_"+str(prompt[:20]).replace(" ","_")+"_model--"+models[sel_model_key]+"_"+ras(randint(0,10))
    image.save("gen/"+name+".png", format="PNG",pnginfo=meta)
    print("Saved as >> ",name,".png")

def choose_model():
    print("Choose a model:")
    i=0
    for mod in models:
        print(i," " ,mod)
        i=i+1
    sel_model_key=int(input(">>> "))
    print(model_dir[models[sel_model_key]]["x_model"]," selected")

    client = InferenceClient(
        provider=model_dir[models[sel_model_key]]["x_provider"],
        api_key=hf_token,
    )

    return client,sel_model_key

while True:

   if req_new==True:
    client,sel_model_key = choose_model()
    req_new=False

    generate(client,model_dir[models[sel_model_key]]["x_model"])

    print("Do you want an another round:")
    print("y - Yes with the same model\nY - Yes with another model\nn - No")
    redo = input('>>> ')
    if redo=='y':
        continue
    elif redo=='Y':
        req_new=True
        continue
    elif redo=='n':
        print('------------------\n==== GOOD DAY ====\n------------------')
        break
    else:
        print('command not found\n------------------\n==== GOOD DAY ====\n------------------')
        break