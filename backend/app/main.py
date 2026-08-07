from fastapi import FastAPI

app=FastAPI(
    title="Investor Relations Intelligence Platform"
)

@app.get("/")
def root():
    return {"message":"Investor Relations Intelligence Platform API"}


@app.get("/health")
def health():
    return {"message":"API is working fine"}