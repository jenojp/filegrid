# filegrid
[![Build Status](https://dev.azure.com/jenopizzaro/negspacy/_apis/build/status/jenojp.filegrid?branchName=main)](https://dev.azure.com/jenopizzaro/negspacy/_build/latest?definitionId=4&branchName=main)

Simple API for exploring files, packaged with Docker.

If given a directory, the API will return the contents of the directory, along with common attributes (e.g., owner, size, permissions).

If given a file, the contents of the text file will be returned.

## Installation
1. Ensure Docker daemon is running
2. Run installation script to create Docker image
```bash
#from ~/filegrid
sh install.sh
```

## Usage
1. Clone repo
2. Run script, specifying root directory (absolute link needed)
```bash
run.sh /Users/tedison/Documents
```
3. Make HTTP request to view files or folders
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
4. Make HTTP request to add a folder.
```bash
curl --location --request POST 'http://localhost:80//foo/newfolder' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dir": true
}'
```
5. Make HTTP request to add a file.
```bash
curl --location --request POST 'http://localhost:80//foo/newfile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dir": false,
    "contents":"this is a new file"
}'
```
6. Make HTTP request to delete a file or folder. Modify "dir" parameter in body of request to be `true` (deleting a folder) or `false` (deleting a file).
```bash
curl --location --request DELETE 'http://localhost:80//foo/newfolder' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dir": true
}'
```


## API Documentation
Navigate to `localhost:80/docs` to view Swagger API documentation.

## Uninstall and cleanup
Simply execute the following to teardown the docker container and remove the built image
```bash
sh cleanup.sh
```