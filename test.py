import requests

def make_request(suffix): 
    url = "http://127.0.0.1:80"+suffix
    response = requests.request("GET", url)
    return response.json()

def test_file_request():
    assert make_request("//foo/baz") == {
    "type": "file",
    "contents": "Sept 30 (Reuters) - The ruptures on the Nord Stream natural gas pipeline system under the Baltic Sea have led to what is likely the biggest single release of climate-damaging methane ever recorded, the United Nations Environment Programme said on Friday.\n\nA huge plume of highly concentrated methane, a greenhouse gas far more potent but shorter-lived than carbon dioxide, was detected in an analysis this week of satellite imagery by researchers associated with UNEP's International Methane Emissions Observatory, or IMEO, the organization said."
    }

def test_folder_request():
    res = make_request("//foo/")
    assert res["results"][1].keys() >= {"name","dir","owner","size","permission"}
    assert type(res["results"][1]["name"]) is str
    assert type(res["results"][1]["dir"]) is bool
    assert type(res["results"][1]["size"]) is int
    assert type(res["results"][1]["permission"]) is int

def test_hidden_file_request():
    res = make_request("//.hid")
    assert res["type"] == "file"

def test_not_found():
    res = make_request("//this/does/not/exist")
    assert res["detail"] == "Directory or File not found"