# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:29:58 2019

@author: HP
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json
json_string="""

[{
	"name": "khushbu",
    "photo":"https://media2.picsearch.com/is?83qFDEj-dBc0g2ODuAtwDcPO7UiPsF2pAEQmO-kwxfc&height=255"
	"last_name": "pareek",
	"contact_detail": [7007808724, "khushbu23 @gmail.com"],
	"department": "cs",
	"research_area": ["CS", "IT", "MECHANICAL"]

}, {
	"name": "kunal",
	"last_name": "srivastava",
	"contact_detail": [7007808734, "kunal44 @gmail.com"],
	"department": "MECHANICAL",
	"research_area": ["CS", "IT", "MECHANICAL"]
}]
"""

json_student="""
[{

	"name": "kiran",
	"last_name": "pareek",
	"contact_detail": [7009808724, "kiran23 @gmail.com"],
	"department": "cs",


}]
    """
with open("data_file.json", "w") as write_file:
    json.dump(json_string, write_file)
    
    
with open("data_file.json1", "w") as write_file:
    json.dump(json_student, write_file)

