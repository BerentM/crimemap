CREATE TABLE IF NOT EXISTS crimes (
    id SERIAL NOT NULL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    date date,
    category VARCHAR(50),
    description VARCHAR(1000),
    updated_at TIMESTAMP);

insert into crimes(description) values ('dupa3');
SELECT * FROM crimes;
