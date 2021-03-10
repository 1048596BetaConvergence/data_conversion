import sys
import urllib.request
import json

def iterate_json_file(json_file):
    result = []
    for key, value in json_file.items():
        if key == "data":
            result = result + iterate_class_object(value)
        else:
            sys.sterr.write("json object must start with key \"data\"")
    return result

def iterate_class_object(class_array):
    result = []
    for class_object in class_array:
        for key, value in class_object.items():
            result = result + merge_class(key, iterate_findings(value))
    return result

def merge_class(class_name, object_array):
    for item in object_array:
        item["class"] = class_name
    return object_array

def iterate_findings(finding_object):
    result = []
    for key, value in finding_object.items():
        if key == "findings":
            result = iterate_finding_object(value)        
        else:
            sys.stderr.write("class object must start with key \"findings\"")
    return result

def iterate_finding_object(finding_array):
    result_array = []
    for item in finding_array:
        result_object = {}
        for key, value in item.items():
            if key == "startLineNumber":
                result_object[key] = value
            elif key == "endLineNumber":
                result_object[key] = value
            elif key == "location":
                path = value.rsplit("/", 1)
                if len(path) == 2:
                    result_object["repository"] = path[0]
                    result_object["file"] = path[1]
                else:
                    result_object["repository"] = ""
                    result_object["file"] = path[0]
            elif key == "type":
                result_object[key] = value
            else:
                print("unrecognized key: ", key)
                sys.exit()
        result_array.append(result_object)
    return result_array


if __name__ == "__main__":
    _source_url = ""
    _repo = ""
    _class = ""
    _type = ""

    for command in sys.argv:
        single_command = command.split("=")
        
        if command == "cli.py":
            continue
        elif len(single_command) > 2:
            sys.stderr.write("Unrecognized command format: " + command + "\n")
            sys.exit()
        elif single_command[0] == "--sourceUrl":
            if(len(_source_url)) > 0:
                sys.stderr.write("Duplicate command --sourceUrl")
            _source_url = single_command[1]
        elif single_command[0] == "--repo":
            if(len(_repo)) > 0:
                sys.stderr.write("Duplicate command --repo")
            _repo = single_command[1]
        elif single_command[0] == "--class":
            if(len(_class)) > 0:
                sys.stderr.write("Duplicate command --class")
            _class = single_command[1]
        elif single_command[0] == "--type":
            if(len(_type)) > 0:
                sys.stderr.write("Duplicate command --type")
            _type = single_command[1]
        else:
            sys.stderr.write("Unrecognized command: " + command + "\n")
            sys.exit()
    
    if len(_source_url) == 0:
        sys.stderr.write("sourceUrl not found from command")

    with urllib.request.urlopen(_source_url) as _source_file:
        result = iterate_json_file(json.load(_source_file))
        if len(_repo) > 0:
            result = list(filter(lambda x: (_repo in x["repository"]), result))
        if len(_class) > 0:
            result = list(filter(lambda x: (_class == x["class"]), result))
        if len(_type) > 0:
            result = list(filter(lambda x: (_type == x["type"]), result))
        sys.stdout.write(str(result) + "\n")