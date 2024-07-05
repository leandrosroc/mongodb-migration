from pymongo import MongoClient

#URL do MongoDB de origem
source_uri = "mongodb://root:root@86.*.*.*:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"

#URL do MongoDB de destino
destination_uri = "mongodb://admin:admin@62.*.*.*:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"

#Conectar ao MongoDB de origem
source_client = MongoClient(source_uri)
source_db = source_client.get_database('tb_exemplo')

#Obter todas as coleções do banco de dados de origem
collections = source_db.list_collection_names()

print("Coleções disponíveis no banco de dados de origem:", collections)

#Conectar ao MongoDB de destino
destination_client = MongoClient(destination_uri)
destination_db = destination_client.get_database('tb_exemplo2') #Nome do banco de dados de destino

#Copiar dados de cada coleção do MongoDB de origem para o MongoDB de destino
for collection_name in collections:
    print("Migrando coleção:", collection_name)
    source_collection = source_db[collection_name]
    destination_collection = destination_db[collection_name]

    #Apagar todos os documentos na coleção de destino (opcional)
    destination_collection.delete_many({})

    #Inserir documentos da coleção de origem na coleção de destino
    documents = source_collection.find()
    destination_collection.insert_many(documents)
    print("Coleção migrada com sucesso:", collection_name)
    print(" ")

print("Migração concluída com sucesso!")

#Fechar as conexões com o MongoDB
source_client.close()
destination_client.close()
