-- database requirements for python app to select from

CREATE TABLE students ( listID int PRIMARY KEY,
                        FirstName varchar(50),
                        Surname varchar(50),
                        MobileNumber varchar(20)
					   );


CREATE TABLE students ( listID int PRIMARY KEY, FirstName varchar(50), Surname varchar(50), MobileNumber varchar(20));


INSERT INTO students VALUES ('1', 'Amie', 'Hall', '078658887671');
INSERT INTO students VALUES ('2', 'Mark', 'Jones', '09234817674');
INSERT INTO students VALUES ('3', 'Leanne', 'King', '0345387676');
INSERT INTO students VALUES ('4', 'Martin', 'Munn', '0450878887634');
INSERT INTO students VALUES ('5', 'Gareth', 'Cooper', '0760878887672');
INSERT INTO students VALUES ('6', 'Kian', 'Smith', '0890871887676');
INSERT INTO students VALUES ('7', 'Max', 'Marks', '0897817623');
INSERT INTO students VALUES ('8', 'Matthew', 'Arnold', '0897817623');
INSERT INTO students VALUES ('9', 'Claire', 'Cooper', '05643227623');
INSERT INTO students VALUES ('10', 'Madeline', 'Bergman', '034317623');
INSERT INTO students VALUES ('11', 'Matthew', 'Anderson', '02343227623');
INSERT INTO students VALUES ('12', 'Stuart', 'Ali', '0234457623');
INSERT INTO students VALUES ('13', 'Sam', 'Allen', '02343227623');
INSERT INTO students VALUES ('14', 'Stuart', 'Armstrong', '07673227623');
INSERT INTO students VALUES ('15', 'Alfie', 'Armstrong', '045564227623');
INSERT INTO students VALUES ('16', 'Ben', 'Armstrong', '09863227623');
INSERT INTO students VALUES ('17', 'Frank', 'Armstrong', '0454227623');