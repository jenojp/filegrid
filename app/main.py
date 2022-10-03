from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
from pathlib import Path
from .filegrid.filegrid import get_dir_contents, get_file_contents, add_folder, add_file, delete_folder, delete_file

app = FastAPI()

class Item(BaseModel):
    dir: bool
    contents: Union[str, None] = None

@app.get("/{file_path:path}")
def explore(file_path: str):
    p = Path("./app/homedir/" + file_path)
    if p.is_dir():
        try:
            return get_dir_contents(p)
        except:
            raise HTTPException(
                status_code=404,
                detail="Unable to provide directory listing. This may be due to a permissions issue.",
            )
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

@app.post("/{file_path:path}")
def add(file_path: str, item: Item):
    p = Path("./app/homedir/" + file_path)
    if item.dir == True:
        try:
            return add_folder(p)
        except:
            raise HTTPException(
                status_code=404,
                detail="Unable to create directory. This directory may exist already, the parent directory may not exist or you may not have permissions to perform this operation.",
            )
    else:
        try:
            return add_file(p, item.contents)
        except:
            raise HTTPException(
                status_code=404,
                detail="Unable to write file. This may be due to a permissions issue.",
            )
        
    

@app.delete("/{file_path:path}")
def remove(file_path: str, item: Item):
    p = Path("./app/homedir/" + file_path)
    if item.dir == True:
        try:
            return delete_folder(p)
        except:
            raise HTTPException(
                status_code=404,
                detail="Unable to delete directory. This directory may not be empty or you may not have permissions to perform this operation.",
            )
    else:
        try:
            return delete_file(p)
        except:
            raise HTTPException(
                status_code=404,
                detail="Unable to remove file. This file may not exist or you may not have the permissions to perform this operation.",
            )