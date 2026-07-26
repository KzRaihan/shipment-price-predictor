from shipment.configuration.mongo_operations import MongoDBOperation 

obj = MongoDBOperation()

df = obj.get_collection_as_dataframe(db_name="Shipment_Kz", collection_name="shipment_collection")

