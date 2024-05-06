from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

def firstfunction()->str:
    return "Hello World"

ret:str = firstfunction()
print(ret)