DROP TABLE IF EXISTS invoice;

CREATE TABLE invoice 
(
    "id"	INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	"customername"	NVARCHAR(255) NOT NULL,
	"customeraddress"	NVARCHAR(255) NOT NULL,
	"date"	DATE NOT NULL,
	"description"	NVARCHAR(255) NOT NULL,
	"invoiceno"	INT NOT NULL,
	"invoicetotal"	INT,
);