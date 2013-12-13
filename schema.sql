drop table if exists monkey;
CREATE TABLE monkey (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  version bigint(20) NOT NULL,
  client_ip varchar(255) DEFAULT NULL,
  commit_time datetime NOT NULL,
  company varchar(255) NOT NULL,
  description varchar(2000) DEFAULT NULL,
  domain varchar(255) NOT NULL,
  edge_server_ip varchar(255) DEFAULT NULL,
  email varchar(255) NOT NULL,
  hostname varchar(255) DEFAULT NULL,
  local_dns varchar(255) DEFAULT NULL,
  name varchar(255) NOT NULL,
  phone varchar(255) NOT NULL,
  url varchar(255) DEFAULT NULL,
  regist_id varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
);
drop table if exists role;
CREATE TABLE role (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  version bigint(20) NOT NULL,
  authority varchar(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY authority (authority)
);
drop table if exists user_role;
CREATE TABLE user_role (
  role_id bigint(20) NOT NULL,
  user_id bigint(20) NOT NULL,
  PRIMARY KEY (role_id,user_id),
  KEY `FK143BF46AFE397551` (`role_id`),
  KEY `FK143BF46AA3643931` (`user_id`),
  CONSTRAINT `FK143BF46AA3643931` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `FK143BF46AFE397551` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
);
drop table if exists user;
CREATE TABLE user (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  version bigint(20) NOT NULL,
  account_expired bit(1) NOT NULL,
  account_locked bit(1) NOT NULL,
  enabled bit(1) NOT NULL,
  password varchar(255) NOT NULL,
  password_expired` bit(1) NOT NULL,
  username varchar(255) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY username (username)
);
