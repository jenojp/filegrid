from fastapi import FastAPI, HTTPException
from pathlib import Path
from .filegrid.filegrid import get_dir_contents, get_file_contents

app = FastAPI()


@app.get("/{file_path:path}")
async def explore(file_path: str):
    p = Path("./app/homedir/" + file_path)
    print(p)
    if p.is_dir():
        return get_dir_contents(p)
    elif p.exists():
        return get_file_contents(p)
    else:
        raise HTTPException(status_code=404, detail="Directory or File not found")
