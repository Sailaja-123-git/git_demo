import json 
file_path = r"C:\users\dabbi\Desktop\json\book.json"
with open (file_path,"r") as json_file:
    data=json.load(json_file)
    print("this book is selected as",data)
