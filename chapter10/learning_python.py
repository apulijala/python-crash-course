"""
Will read entire file in one go and retuns the values as a
string. 
If file not found returns File Not Found String. 
"""
def read_entire_file(filename):
    try: 
        with open(filename) as file_obj:
            return file_obj.read()
    except FileNotFoundError as e:
        print(e)
        return f"{e.filename} Not Found"

def read_by_storing_lines(filename):
    try: 
        with open(filename) as f:
            contents = f.readlines()
            text = ""
            for line in contents:
                text += line
            return text
    except FileNotFoundError as e:
        print(e)
        return f"{e.filename} Not Found"

    

def read_by_looping_over_file(filename):
    try: 
        with open(filename) as f:
            text = ""
            for line in f:
                text += line.rstrip()
            return text
    except FileNotFoundError as e:
        print(e)
        return f"{e.filename} Not Found"



