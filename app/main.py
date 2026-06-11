from fastapi import FastAPI

app = FastAPI(title="fastapi-swap-learning")


@app.get("/")
def read_root():
    return {"message": "Hello from fastapi-swap-learning"}


@app.get("/health")
def health():
    return {"status": "ok"}
