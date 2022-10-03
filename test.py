import requests
from pathlib import Path

def make_request(suffix:str, method:str, headers:dict = {}, payload:dict = {}): 
    url = "http://localhost:8000/"+suffix
    response = requests.request(method, url, headers=headers, json=payload)
    return response.json(), response.status_code

def test_file_request():
    assert make_request("/foo/baz","GET")[0] == {
    "type": "file",
    "contents": "Sept 30 (Reuters) - The ruptures on the Nord Stream natural gas pipeline system under the Baltic Sea have led to what is likely the biggest single release of climate-damaging methane ever recorded, the United Nations Environment Programme said on Friday.\n\nA huge plume of highly concentrated methane, a greenhouse gas far more potent but shorter-lived than carbon dioxide, was detected in an analysis this week of satellite imagery by researchers associated with UNEP's International Methane Emissions Observatory, or IMEO, the organization said."
    }

def test_folder_request():
    res = make_request("/foo/", "GET")[0]
    assert res["type"] == "dir"
    assert res["results"][1].keys() >= {"name","dir","owner","size","permission"}
    assert type(res["results"][1]["name"]) is str
    assert type(res["results"][1]["owner"]) is str
    assert type(res["results"][1]["dir"]) is bool
    assert type(res["results"][1]["size"]) is int
    assert type(res["results"][1]["permission"]) is int

def test_hidden_file_request():
    res = make_request("/.hid", "GET")[0]
    assert res["type"] == "file"

def test_not_found():
    res = make_request("/this/does/not/exist", "GET")
    assert res[0]["detail"] == "Directory or File not found"
    assert res[1] == 404

def test_add_folder():
    path = "/foo/newfolder"
    headers = {"Content-Type":"application/json"}
    payload = {"dir":True}
    res = make_request(path, "POST", headers, payload)
    assert res[1] == 200
    p = Path("./app/homedir/"+path)
    assert p.exists()
    assert p.is_dir()

def test_add_file():
    path = "/foo/newfile"
    headers = {"Content-Type":"application/json"}
    payload = {"dir":False, "contents":"text mctexty text"}
    res = make_request(path, "POST", headers, payload)
    assert res[1] == 200
    p = Path("./app/homedir/"+path)
    assert p.exists()
    assert p.is_dir() == False

def test_rm_folder():
    path = "/foo/newfolder"
    headers = {"Content-Type":"application/json"}
    payload = {"dir":True}
    res = make_request(path, "DELETE", headers, payload)
    assert res[1] == 200
    p = Path("./app/homedir/"+path)
    assert p.exists() == False

def test_rm_file():
    path = "/foo/newfile"
    headers = {"Content-Type":"application/json"}
    payload = {"dir":False}
    res = make_request(path, "DELETE", headers, payload)
    assert res[1] == 200
    p = Path("./app/homedir/"+path)
    assert p.exists() == False

