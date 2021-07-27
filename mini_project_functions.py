import csv
from pprint import pprint

def whitespace():
    print('\n')


#READ FILES 
def read_csv_file (file_name, csv_to_read):
    with open (file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row) 
        return csv_list


#PRINT FILES 
def print_csv_file (file_name, *csv_file):
    with open(file_name, 'r') as csv_print:
        csv_file = csv.DictReader(csv_print)
        for row in csv_file:
            pprint(dict(row))
    



#Dictionary Append
def append_dict(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)


#Write in python file
field_names = ['Id','Name','Course','City','Session']
row_dict = {'Id': 81,'Name': 'Sachin','Course':'Maths','City':'Mumbai','Session':'Evening'}
# Append a dict as a row in csv file
append_dict_as_row('students.csv', row_dict, field_names)



#Write in python file
field_names = ['Id','Name','Course','City','Session']
row_dict = {'Id': 81,'Name': 'Sachin','Course':'Maths','City':'Mumbai','Session':'Evening'}
# Append a dict as a row in csv file
append_dict_as_row('students.csv', row_dict, field_names)