-- 1. Create a database
DROP DATABASE IF EXISTS ContactDB;
CREATE DATABASE ContactDB;

-- 2. Use the database
USE ContactDB;

-- 3. Create a table
CREATE TABLE participant (
    Id int  PRIMARY KEY not NULL,
    Name VARCHAR(50) NOT NULL,
    Contact VARCHAR(15) NOT NULL,
    Email VARCHAR(100) NOT NULL
)

-- Create the 'event' table
CREATE TABLE event (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- Auto-incrementing ID
    name VARCHAR(100) NOT NULL,          -- Name of the event
    venue VARCHAR(100) NOT NULL,         -- Venue of the event
    startDate DATE NOT NULL,            -- Start date of the event
    endDate DATE NOT NULL,              -- End date of the event
    description TEXT                     -- Description of the event
);

CREATE TABLE Event_Participation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    eventid INT NOT NULL,
    participationid INT NOT NULL,
    FOREIGN KEY (eventid) REFERENCES Event(id) ON DELETE CASCADE,
    FOREIGN KEY (participationid) REFERENCES Participant(id) ON DELETE CASCADE
);


-- Insert some sample data into the 'event' table
INSERT INTO event (name, venue, startDate, endDate, description)
VALUES 
    ('Music Festival', 'City Park', '2024-12-25', '2024-12-27', 'A three-day music festival featuring local and international artists.'),
    ('Art Exhibition', 'Downtown Gallery', '2024-11-15', '2024-11-20', 'An exhibition showcasing contemporary art pieces.'),
    ('Tech Conference', 'Convention Center', '2024-10-05', '2024-10-07', 'A gathering of tech enthusiasts to discuss AI and emerging technologies.'),
    ('Food Fair', 'Community Hall', '2024-09-10', '2024-09-12', 'A fair featuring cuisines from around the world.'),
    ('Charity Run', 'Central Park', '2024-08-20', '2024-08-20', 'A charity event to support local organizations.');

-- 4. Insert data into the table
INSERT INTO participant (Id, Name, Contact, Email) VALUES
(1, 'Pranshu', '9784387385', 'panshu2002@gmail.com'),
(2, 'Neelam', '0000000000', 'mumma2000@gmail.com'),
(3, 'Jahanvi', '7404777777', 'jahanvi2005@gmail.com'),
(4, 'Jyoti', '7404777385', 'jyoti2004@gmail.com'),
(5, 'Navin', '7000000000', 'army2000@gmail.com'),
(6, 'Bhumika', '7777777777', 'didi2002@gmail.com');

INSERT INTO Event_Participation (eventid, participationid) VALUES 
(1, 1),
(1, 2),
(2, 3);

-- 5. Display the inserted data
SELECT * FROM participant;
SELECT * FROM event;

