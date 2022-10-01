from pathlib import Path
import sys


def get_dir_contents(p: object) -> dict:
    results = list()
    for child in p.iterdir():
        results.append({
            "name":child.name,
            "dir":child.is_dir(),
            "owner":child.owner(),
            "size":child.stat().st_size,
            "permission":child.stat().st_mode
        })
    directory_results = {
        "type":"dir",
        "results":results}
    return directory_results

def get_file_contents(p: object) -> dict:
    text = p.read_text()
    return {
        "type":"file",
        "contents":text
    }


if __name__ == "__main__":
    p = Path(sys.argv[1])
    print(get_file_contents(p))