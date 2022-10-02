# filegrid
Simple API for exploring files, packaged with Docker

If given a directory, the API will return the contents of the directory, along with common attributes (e.g., owner, size, permissions).

If given a file, the contents of the text file will be returned.

## Installation
1. Ensure Docker Daemon is running
2. Run installation script to create Docker image
```bash
#from ~/filegrid
sh install.sh
```

## Usage
1. Run script, specifying root directory in
```bash
run.sh /Users/tedison/Documents
```
2. Make HTTP request
```bash
curl --request GET 'http://127.0.0.1:80//foo/foobar'
```
Note: `/foo/foobar` is a file path. You must supply `//` between the `http://address:port` and the `{file path}` for the API to properly recognize your path.

Sample Response (Directory):
```json
{
    "type": "dir",
    "results": [
        {
            "name": "baz",
            "dir": false,
            "owner": "root",
            "size": 546,
            "permission": 33188
        },
        {
            "name": "foobar",
            "dir": true,
            "owner": "root",
            "size": 96,
            "permission": 16877
        }
    ]
}
```

Sample Response (File):
```json
{
    "type": "file",
    "contents": "Sept 30 (Reuters) - The ruptures on the Nord Stream natural gas pipeline system under the Baltic Sea have led to what is likely the biggest single release of climate-damaging methane ever recorded, the United Nations Environment Programme said on Friday.\n\nA huge plume of highly concentrated methane, a greenhouse gas far more potent but shorter-lived than carbon dioxide, was detected in an analysis this week of satellite imagery by researchers associated with UNEP's International Methane Emissions Observatory, or IMEO, the organization said."
}
```