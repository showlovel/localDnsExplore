drop table if exists monkey;
create table monkey (
  id integer primary key autoincrement,
  version integer not null,
  client_ip varchar(255) default null,
  commit_time timestamp not null,
  company varchar(255) not null,
  description varchar(2000) default null,
  domain varchar(255) not null,
  edge_server_ip varchar(255) default null,
  email varchar(255) not null,
  hostname varchar(255) default null,
  local_dns varchar(255) default null,
  name varchar(255) not null,
  phone varchar(255) not null,
  url varchar(255) default null,
  regist_id varchar(255) default null
);

drop table if exists role;
create table role(
  id integer primary key autoincrement,
  version integer not null,
  authority varchar(255) unique not null
);

drop table if exists user_role;
create table user_role(
  role_id integer,
  user_id integer,
  primary key (role_id,user_id)
);

drop table if exists user;
create table user (
  id integer primary key autoincrement,
  version integer not null,
  account_expired bit(1) not null,
  account_locked bit(1) not null,
  enabled boolean not null,
  password varchar(255) not null,
  password_expired boolean not null,
  username varchar(255) unique not null
);
