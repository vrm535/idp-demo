from fastapi import FastAPI

app = FastAPI(title="IDP-Demo-APP")


@app.get("/")
def say_hello():
    return {"message": "Hello IDP User!"}
