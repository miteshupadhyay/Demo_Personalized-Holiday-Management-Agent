from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holiday_team import team

class PlanRequest(BaseModel):
    content: str
    source: str  = "User"


app = FastAPI(title="Holiday Management API")


# Serve static files from ./static
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/plan")
async def plan(req: PlanRequest):
    try:
        print("1. Request received")
        print(f"Content = {req.content}")
        print(f"Source = {req.source}")

        task = TextMessage(
            content=req.content,
            source=req.source
        )

        print("2. TextMessage created")
        print("3. Calling team.run()...")

        result = await team.run(task=task)

        print("4. team.run() completed")

        messages = [
            {
                "source": m.source,
                "content": m.content
            }
            for m in result.messages
        ]

        print("5. Messages created")
        print(messages)

        return {"messages": messages}

    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
