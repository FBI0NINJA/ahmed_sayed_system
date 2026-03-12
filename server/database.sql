CREATE DATABASE licenses;

USE licenses;

CREATE TABLE license_keys(
id INT AUTO_INCREMENT PRIMARY KEY,
license_key VARCHAR(255),
used INT DEFAULT 0
);

INSERT INTO license_keys (license_key,used) VALUES
('AHMED-1',0),
('AHMED-2',0),
('AHMED-3',0);
('AHMED-4',0),
('AHMED-5',0),
('AHMED-5',0);
('AHMED-6',0),
('AHMED-7',0);
