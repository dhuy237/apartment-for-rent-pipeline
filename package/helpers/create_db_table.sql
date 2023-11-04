CREATE DATABASE homebase
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE IF NOT EXISTS apartments_for_rent (
    id int,
	category varchar(256),
	title varchar(256),
	body varchar(256),
	amenities varchar(256),
	bathrooms float,
	bedrooms float,
	currency varchar(256),
	fee varchar(256),
	has_photo varchar(256),
	pets_allowed varchar(256),
	price int,
	price_display varchar(256),
	price_type varchar(256),
	square_feet int,
	address varchar(256),
	cityname varchar(256),
	state varchar(256),
	latitude float,
	longitude float,
	source varchar(256),
	time int
);