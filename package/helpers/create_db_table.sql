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
	id text,
	category text,
	title text,
	body text,
	amenities text,
	bathrooms float,
	bedrooms float,
	currency text,
	fee text,
	has_photo text,
	pets_allowed text,
	price int,
	price_display text,
	price_type text,
	square_feet int,
	address text,
	cityname text,
	state text,
	latitude float,
	longitude float,
	source text,
	time int
);