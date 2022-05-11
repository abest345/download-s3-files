## Description
Download files from S3 specified in the included list.csv file. The list.csv file needs to include the files tmpname and desired filename.

### Files
- list.csv = an example input list. Columns need to be surrounded with quotes and be comma seperated.
- run.py = Python3 script that will download the files from list.csv

### User defined variables

1. Your aws access key
aws_access_key_id

2. You aws secret
aws_secret_access_key

3. Target bucket to copy file from
bucket_name

4. Location within the bucket where the file is
object_location

5. Destination to save the file locally
file_save_location

### Prereqs
1. boto3
```
apt install pip
pip install boto3
```

### Usage:
```python3
python3 run.py
```
Script will create the folder specified in the script by 'file_save_location'. Ensure you have enough space.
