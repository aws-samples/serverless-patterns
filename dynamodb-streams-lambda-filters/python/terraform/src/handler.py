def modify_handler(event, context):
    print(event)
    print("Hi, I have recieved your modification request. Will process your request soon.")
    return "success"

def bachelors_handler(event, context):
    print(event)
    print("Hi, I'm Bachelors Handler. I will be able to take care of your Request.")
    return "success"

def masters_handler(event, context):
    print(event)
    print("Hi, I'm Masters Handler. I will be able to take care of your Request.")
    return "success"

def remove_handler(event, context):
    print(event)
    print("Hi, I have recieved you remove request. Will process your request soon.")
    return "success"