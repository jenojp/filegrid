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
        try:
            return get_file_contents(p)
        except:
            raise HTTPException(
                status_code=404,
                detail="Unable to read file. This may be due to a permissions issue or unexpected file type, expected text.",
            )
    else:
        raise HTTPException(status_code=404, detail="Directory or File not found")
