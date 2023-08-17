-- Create Root User
Create USER IF NOt EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
Grant ALL PRIVILEGES ON *.* to 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;