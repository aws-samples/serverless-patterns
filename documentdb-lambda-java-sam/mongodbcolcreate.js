db = db.getSiblingDB('DOCDB_DATABASE');
db.createCollection('DOCDB_COLLECTION');
print("Collection created successfully.");

db.adminCommand({modifyChangeStreams: 1, database: "DOCDB_DATABASE", collection: "DOCDB_COLLECTION", enable: true});