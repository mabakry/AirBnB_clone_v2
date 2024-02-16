-- prepares a MySQL server for the project

-- create a database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- create a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
