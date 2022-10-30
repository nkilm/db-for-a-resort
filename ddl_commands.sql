CREATE SCHEMA resortpro;
SET search_path TO resortpro;
/* state= MH, KA */
CREATE TABLE city (
    pincode integer PRIMARY KEY,
    name varchar(30) NOT NULL,
    state CHAR(2) NOT NULL
);
CREATE TABLE resort (
    resort_id DECIMAL(4, 0) PRIMARY KEY CONSTRAINT resort_id_cons CHECK (resort_id > 0),
    resort_name varchar(50) NOT NULL,
    pincode int,
    address varchar(40) NOT NULL,
    rating varchar(10),
    FOREIGN KEY (pincode) REFERENCES city(pincode) ON DELETE RESTRICT
);
CREATE TABLE waiter (
    waiter_id DECIMAL(3, 0) PRIMARY KEY,
    waiter_name varchar(20),
    resort_id DECIMAL(4, 0),
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE
);
CREATE TABLE customer (
    cid Decimal(4, 0) PRIMARY KEY CONSTRAINT cid_cons CHECK (cid > 0),
    fname VARCHAR(20),
    minit CHAR(1),
    lname VARCHAR(20),
    address varchar(30),
    email varchar(320),
    contactNo DECIMAL(15, 0),
    waiter_id DECIMAL(3, 0),
    FOREIGN KEY (waiter_id) REFERENCES waiter(waiter_id) ON DELETE CASCADE
);
CREATE TABLE offers (
    offer_id DECIMAL(2, 0),
    offer_name varchar(20),
    cid DECIMAL(4, 0) CONSTRAINT cid_cons CHECK (cid > 0),
    resort_id DECIMAL(4, 0) CONSTRAINT resort_id_cons CHECK (resort_id > 0),
    discount int,
    startdate DATE,
    enddate DATE,
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES customer(cid) ON DELETE CASCADE,
    PRIMARY KEY(resort_id, cid, offer_id)
);
-- Price range can be changed
CREATE TABLE room (
    resort_id DECIMAL(4, 0) CONSTRAINT resort_id_cons CHECK (resort_id > 0),
    room_no decimal(3, 0) PRIMARY KEY CONSTRAINT room_no_cons CHECK (room_no > 0),
    category varchar(6) CONSTRAINT category_cons CHECK (category IN ('single', 'double', 'suite')),
    floor SMALLINT,
    price numeric CONSTRAINT price_cons CHECK (
        price BETWEEN 0.00 AND 10000.00
    ),
    PRIMARY KEY(room_no, resort_no),
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE
);
CREATE TABLE reservation(
    cid DECIMAL(4, 0) CONSTRAINT cid_cons CHECK (cid > 0),
    resort_id DECIMAL(4, 0) CONSTRAINT resort_id_cons CHECK (resort_id > 0),
    checkin DATE NOT NULL,
    checkout DATE NOT NULL,
    CONSTRAINT stay_duration CHECK (checkout > checkin),
    FOREIGN KEY (cid) REFERENCES customer(cid) ON DELETE CASCADE,
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE,
    PRIMARY KEY(resort_id, cid)
);
CREATE TABLE relatives(
    cid DECIMAL(4, 0),
    relative_name VARCHAR(20),
    sex char(1),
    relationship VARCHAR(20),
    FOREIGN KEY (cid) REFERENCES customer(cid) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (cid, relative_name)
);
CREATE TABLE food_item (
    food_id decimal(2, 0),
    food_name varchar(20),
    price numeric CONSTRAINT price_cons CHECK (
        price BETWEEN 0.00 AND 500.00
    ),
    PRIMARY KEY(food_id)
);
-- customer orders food via some food delivery app
CREATE TABLE orders (
    cid DECIMAL(4, 0),
    item_id DECIMAL(3, 0),
    quantity INT,
    time DATETIME,
    FOREIGN KEY(cid) REFERENCES customer(cid) ON DELETE RESTRICT,
    FOREIGN KEY(item_id) REFERENCES food_item(food_id) ON DELETE RESTRICT,
    PRIMARY KEY (cid, itemid)
);
-- number of digits in transaction Id varies, 12 is most common
CREATE TABLE bill (
    transaction_id DECIMAL(12, 0) PRIMARY KEY,
    date DATE,
    cid DECIMAL(4, 0),
    paymentmode varchar(10),
    FOREIGN KEY(cid) REFERENCES customer(cid) ON DELETE RESTRICT
);