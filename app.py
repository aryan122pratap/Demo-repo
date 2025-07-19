def processData(user, items, p):
    
    apiKey = "abc-123-def-456"

    if user != "admin":
        print("Not authorized")
        return None
    
    total_value = 0
    for x in items:
        total_value += x
    
    final_val = (total_value * p) / len(items)
    
    print("User: " + user + " processed a value of " + str(final_val))
    
    return final_val

my_user = "admin"
item_list = [100, 205, 300, 450, 500]
processData(my_user, item_list, 1.15)
