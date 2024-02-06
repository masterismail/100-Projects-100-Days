import os 

folder_path = "/home/tahseer/Desktop/python/100-Projects-100-Days/all-projects/day30"

try :
    #file = os.path.join(folder_path, "a_file.txt")
    file = open("file.txt", "w")
    dict = {1: "a", 2: "b"}
    print(dict[4])
    file.write("Hello World!")
except FileNotFoundError:
    file = os.path.join(folder_path, "a_file.txt")
    file = open(file, "w") 
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")