CREATE DATABASE IF NOT EXISTS `knowledge_graph` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE knowledge_graph;
CREATE TABLE IF NOT EXISTS entity (
                      id varchar(20) PRIMARY KEY,
                      label varchar(20),
                      code varchar(20),
                      name varchar(100))
                      DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS manage (
                      entityfi_id varchar(20) NOT NULL,
                      title varchar(50), 
                      entityse_id varchar(20) NOT NULL,
                      type varchar(20) NOT NULL,
                      UNIQUE KEY (entityfi_id, entityse_id))
                      DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS spo (
                      subj varchar(100),
                      pred varchar(100),
                      obj varchar(500),
                      obj1 varchar(500)，
                      type varchar(20),
                      UNIQUE KEY (subj, pred, obj))
                      DEFAULT CHARSET=utf8;
 CREATE TABLE IF NOT EXISTS entitis_se (
                      id varchar(20) PRIMARY KEY,
                      label varchar(20),
                      
                      fourth varchar(500),
                      third varchar(200),
                      second varchar(200),
                      first varchar(200),
                      UNIQUE KEY (first, second, third))
                      DEFAULT CHARSET=utf8;


LOAD DATA LOCAL INFILE 'entitis_fi.txt' INTO TABLE entity CHARACTER SET utf8 FIELDS TERMINATED BY '\t' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'entitis_se.txt' INTO TABLE entitis_se CHARACTER SET utf8 FIELDS TERMINATED BY '\t' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'management_edge.txt' INTO TABLE manage CHARACTER SET utf8 FIELDS TERMINATED BY '\t' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'spo.txt' INTO TABLE spo CHARACTER SET utf8 FIELDS TERMINATED BY '\t' IGNORE 1 LINES;'\t'
LOAD DATA LOCAL INFILE 'spoo.txt' INTO TABLE spo CHARACTER SET utf8 FIELDS TERMINATED BY '\t' IGNORE 1 LINES;