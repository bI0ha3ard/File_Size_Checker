import os

file_path = input("Enter file path: ")

file_size = os.path.getsize(file_path)

if file_size < 1024:
    size_str = str(file_size) + " bytes"
elif file_size < 1024**2:
    size_str = "{:.2f} KB".format(file_size/1024)
else:
    size_str = "{:.2f} MB".format(file_size/1024**2)

print("The file size at the given path {} is: {}".format(file_path, size_str))
