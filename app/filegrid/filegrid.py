from pathlib import Path
import sys


def get_dir_contents(p: object) -> dict:
    results = list()
    for child in p.iterdir():
        try:
            owner = child.owner()
        except:
            owner = "unknown"
        results.append(
            {
                "name": child.name,
                "dir": child.is_dir(),
                "owner": owner,
                "size": child.stat().st_size,
                "permission": child.stat().st_mode,
            }
        )
    directory_results = {"type": "dir", "results": results}
    return directory_results


def get_file_contents(p: object) -> dict:
    text = p.read_text()
    return {"type": "file", "contents": text}

def add_folder(p: object) -> dict:
    p.mkdir()
    return {"message":"folder successfully created"}

def add_file(p: object, contents: str) -> dict:
    p.write_text(contents)
    return {"message":"file successfully created"}

def delete_folder(p: object) -> dict:
    p.rmdir()
    return {"message":"folder successfully deleted"}

def delete_file(p: object) -> dict:
    p.unlink()
    return {"message":"file successfully deleted"}