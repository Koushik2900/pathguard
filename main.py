import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

import uvicorn
from fastapi import FastAPI

from pathguard.api import router

app = FastAPI(title="PathGuard API", version="0.1.0")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
