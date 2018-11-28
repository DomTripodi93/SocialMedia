(/*) 
In order to create default values for new users, please re-create the propage_propage table
and add Propage_trigger1 to make sure that default values are created for new users.
Individually input the following lines into your SQL shell as a single line command: 
8, 10-15, 17, 19-24, 26
(*/)

DROP TABLE propage_propage;

create table propage_propage(
	user_id VARCHAR(100) PRIMARY KEY REFERENCES auth_user.id,
    bio VARCHAR(1000) DEFAULT 'Tell us a little bit about yourself!',
    interests VARCHAR(300) DEFAULT 'What are some of your interests?',
    goals VARCHAR(300) DEFAULT 'What made you decide to create an account with us?'
);

DELIMITER $$

CREATE 
	TRIGGER Propage_trigger1 AFTER INSERT
    ON auth_user
    FOR EACH ROW BEGIN
	INSERT INTO propage_propage VALUES(NEW.id, DEFAULT, DEFAULT, DEFAULT);
	END$$

DELIMITER ;