db = db.getSiblingDB('DOCDB_DATABASE');

// Safe to run again: create the collection only if it doesn't exist yet.
if (db.getCollectionNames().includes('DOCDB_COLLECTION')) {
  print("Collection already exists.");
} else {
  db.createCollection('DOCDB_COLLECTION');
  print("Collection created successfully.");
}

// The Lambda event source mapping needs change streams on this collection.
printjson(db.adminCommand({modifyChangeStreams: 1, database: "DOCDB_DATABASE", collection: "DOCDB_COLLECTION", enable: true}));
