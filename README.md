# Brightspace Project Extractor

## The Problem
When multiple students submit a project to Brightspace, the projects files are downloaded in batch as a giant zip file. This file is unzipped into a set of folders - one for each student containing their submitted project files. But what happens if the student zips up their project files and submits that? You end up with a zip file inside each student's folder. The instructor then has to go and manually unzip each zip file in each student's folder. What a mess.

This python script automates this by going into each student's folder and unzipping the project files

## Usage
Copy the extract.py file into the folder containing the student folders. Then run the script using the following command in the terminal:

```
python extract.py
``` 

The script will go through all folders in the directory and unzip any zip files it finds within them

## Requirements
- Python 3.6 or higher

## Options
The script has the following options:
- aaa
- bbb
- ccc