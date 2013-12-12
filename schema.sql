drop table if exists user;
create table user(
  id integer primary key autoincrement,
  version integer,
  client_ip varchar(255),
  company varchar(255),
  domain varchar(255),
  email varchar(255),
  hostname varchar(255),
  local_dns varchar(255),
  name varchar(255),
  phone varchar(255),
  url varchar(255)
);
