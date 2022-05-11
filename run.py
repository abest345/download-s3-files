# Downloads files from s3 using an input csv file.
import boto3 # For aws
import re
import csv # For importing csv file
import os # For os level functions

# Manually edited variables
s3 = boto3.client ('s3', # Defining aws service, S3 in this case
    aws_access_key_id='', # Your credentials to target bucket
    aws_secret_access_key='') # Your credentials to target bucket
bucket_name = '' # Target bucket name (e.g: 'mybucket')
object_location = '' # Target location where objects are stored (e.g: 'path/leading/to/file/')
file_save_location = 'saved-files' # Destination location for downloaded files
input = 'list.csv'

if not os.path.isdir(file_save_location):
    os.mkdir(file_save_location)

def check_duplicate_file(filename_cleaned):
    filename, extension = os.path.splitext(filename_cleaned)
    counter = 1
    while os.path.isfile('saved-files/' + filename_cleaned):
        filename_cleaned = filename + " (" + str(counter) + ")" + extension
        counter +=1
    return filename_cleaned

with open(input) as csv_file:
    csv_reader = csv.DictReader(csv_file) # Using python csv reader
    line_count = 0
    for row in csv_reader:
        if line_count == 0: # Skip heading
            print(f'Column names are {", ".join(row)}') 
            line_count += 1
        filename_str = str({row["filename"]}) # Converting csv value to string
        filename_cleaned = filename_str[2:-2] # Trimming the 2 outer characters (brackets and quotes)
        filename_appended = check_duplicate_file(filename_cleaned) # Sending to function to give unique filename if required
        tmpname = str({row["tmpname"]})
        tmpname_str = tmpname[2:-2]
        try:
            s3.download_file(bucket_name,object_location + tmpname_str,'saved-files/' + filename_appended) # Downloads the file.
            print(tmpname_str +  ' saved as ' + filename_appended)
        except Exception as error:
            print('Unable to locate file: ' + tmpname_str + ' (' + filename_appended + ')')