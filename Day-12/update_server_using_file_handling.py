# We are updating the values in server conf file where file_path is the  path of the server conf file, key is the part where the changes will happen with the value provided

def update_server_conf(file_path, key, value):
    # Opening the file in read mode as file alias name
    with open(file_path , 'r') as file:
        # Reading all the lines in the file and storing all in lines variable
        lines = file.readlines()
    
    # Opening the file in write mode 
    with open(file_path , 'w') as file:
        
        # Looping through all the lines present in the file
        for line in lines:
            # while looping if the key is match in the line then it is replaced with the value
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

# Declaring the Arguments as the variables
server_config_file_path = "Day-12\server.conf"
key_to_update = "MAX_CONNECTIONS"
value_to_update = "1000"

# Calling the function with the set variables
update_server_conf(server_config_file_path, key_to_update, value_to_update)