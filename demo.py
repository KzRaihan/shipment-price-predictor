from shipment.utils.main_utils import MainUtils

# create an object of MainUtils is a class
obj = MainUtils() 

# call the read_yaml_files
# syntax: obj.read_yaml_file(file_location)
data = obj.read_yaml_file("config/model.yaml")
print(data)