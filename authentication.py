# Define the function to check user credentials
def signin(username,password,file):
# Initialize empty lists for user IDs and passwords
    user_id = []
    user_password = []
    # Open the credentials file and read in each line
    credential = open(file, "r")
    for cred in credential:
        #  Split each line into a user ID and password
        value = cred.strip().split(":")
        # Add the user ID and password to their respective lists
        user_id.append(value[0])
        user_password.append(value[1])
    #     Check if the entered username and password match any in the file
    for i in range(len(user_id)):
        if username == user_id[i] and password == user_password[i]:
            # If there's a match, return True
            return True
    #     If there's no match, return False
    else:
        return False

