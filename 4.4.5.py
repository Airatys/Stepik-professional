import json
def is_correct_json(string):
    try:
        a = json.loads(string)
        return True
    except:
        return False
   
    




