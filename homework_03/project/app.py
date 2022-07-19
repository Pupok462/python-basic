from fastapi import FastAPI


app = FastAPI()


@app.get("/ping/")
def ping():
    """
    :return:  "pong" if you will go to app
    """
    return {"message": "pong"}

