from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from MCP server on Railway!"}

@app.post("/mcp")
async def mcp(request: Request):
    body = await request.json()
    print("Received:", body)

    # 仮の応答（ここに tax-law-mcp のロジックを組み込める）
    return JSONResponse(content={
        "type": "mcp_response",
        "content": {
            "law": "所得税法",
            "articles": [
                {"id": "1", "title": "第1条"},
                {"id": "2", "title": "第2条"}
            ]
        }
    })
