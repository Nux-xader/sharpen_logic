def build_struct_err(struct, data, validation_stack):
    if isinstance(struct, dict):
        struct[tuple(struct.keys())[0]] = tuple(struct.values())[0].__name__
    else:
        struct = struct.__name__ if isinstance(struct, type) else type(struct)
    
    validation_stack = f"validation_stack:\n{validation_stack} \n\n"
    data = f"data:\n{struct} || {data}\n{type(struct)} || {type(data)}"
    raise ValueError(validation_stack+data)

def check_structure(struct, data, validation_stack=[]):

    params = struct, data, validation_stack
    if isinstance(struct, dict) and isinstance(data, dict):
        validation_stack.append(dict())
        # struct is a dict of types or other dicts
        valid = all(k in data and check_structure(
            struct[k], data[k], validation_stack=validation_stack
            ) for k in struct)
        
        if not valid: build_struct_err(*params)
        return valid
    if isinstance(struct, list) and isinstance(data, list):
        validation_stack.append([])
        # struct is list in the form [type or dict]
        valid =  all(check_structure(
            struct[0], c, validation_stack=validation_stack
            ) for c in data)

        if not valid: build_struct_err(*params)
        return valid
    elif isinstance(struct, type):
        validation_stack.append(struct.__name__)
        # struct is the type of data
        valid = isinstance(data, struct)
        if not valid: build_struct_err(*params)
        return valid
    else:
        if type(struct) != type(data): build_struct_err(*params)
        raise ValueError(f"{check_structure.__name__} not supported {type(struct)}")


def run_struct_validator(struct, data):
    try: return check_structure(struct=struct, data=data), None
    except Exception as e: return False, e



struct = {
    "ab": int, 
    "cc": [
        {"aa": str}
    ], 
    # "sdf": tuple()
}

data = {
    "ab": 0, 
    "cc": [
        {"aa": "AWKOK"}, 
        {"aa": 0}
    ]
}



valid = run_struct_validator(struct, data)
print(valid)