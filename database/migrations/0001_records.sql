create table if not exists Records (
    id integer primary key,
    text varchar(250),
    time datetime default current_timestamp
);