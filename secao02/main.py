from fastapi import FastAPI

app = FastAPI()


@app.get('/msg')
async def mensagem():
    return {"msg": "FastAPI na Geek University"}
