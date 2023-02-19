DROP TABLE IF EXISTS invoice;

CREATE TABLE invoice 
(
    "id"	INTEGER,
	"customername"	TEXT NOT NULL,
	"customeraddress"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"invoiceno"	INTEGER NOT NULL,
	"invoicetotal"	INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
    
);