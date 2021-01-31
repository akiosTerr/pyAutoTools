import files.text_files
import datetime


main = "hello world!"

file_name = "test"
files.text_files.create_file(file_name)
files.text_files.append_file(datetime.datetime.now(), file_name)

