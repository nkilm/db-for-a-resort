CREATE TABLE resort (
    resort_id DECIMAL(4, 0) PRIMARY KEY CHECK (resort_id > 0),
    resort_name varchar(50) NOT NULL,
    address varchar(40) NOT NULL,
    rating DECIMAL(3,2),
    price_per_day float
);
CREATE TABLE room_service (
    waiter_id DECIMAL(3, 0) PRIMARY KEY,
    waiter_name varchar(20),
    resort_id DECIMAL(4, 0),
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE
);
CREATE TABLE customer (
    cid Decimal(4, 0) PRIMARY KEY CHECK (cid > 0),
    fname VARCHAR(20),
    minit CHAR(1),
    lname VARCHAR(20),
    address varchar(30),
    email varchar(30),
    contactNo DECIMAL(10, 0),
    waiter_id DECIMAL(3, 0),
    FOREIGN KEY (waiter_id) REFERENCES room_service(waiter_id) ON DELETE CASCADE
);
CREATE TABLE offers (
    offer_id DECIMAL(2, 0),
    offer_name varchar(20),
    cid DECIMAL(4, 0) CHECK (cid > 0),
    resort_id DECIMAL(4, 0) CHECK (resort_id > 0),
    discount int,
    startdate DATE,
    enddate DATE,
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES customer(cid) ON DELETE CASCADE,
    PRIMARY KEY(resort_id, cid, offer_id)
);
CREATE TABLE reservation(
    cid DECIMAL(4, 0) CHECK (cid > 0),
    resort_id DECIMAL(4, 0) CHECK (resort_id > 0),
    checkin DATE NOT NULL,
    checkout DATE NOT NULL,
    amount float,
    CHECK (checkout > checkin),
    FOREIGN KEY (cid) REFERENCES customer(cid) ON DELETE CASCADE,
    FOREIGN KEY (resort_id) REFERENCES resort(resort_id) ON DELETE CASCADE,
    PRIMARY KEY(resort_id, cid)
);
CREATE TABLE relatives(
    cid DECIMAL(4, 0),
    relative_name VARCHAR(20),
    gender char(1),
    relationship VARCHAR(20),
    FOREIGN KEY (cid) REFERENCES customer(cid) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (cid, relative_name)
);
CREATE TABLE food_item (
    food_id decimal(2, 0),
    food_name varchar(20),
    price numeric CHECK (
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
    PRIMARY KEY (cid, item_id)
);
-- number of digits in transaction Id varies, 12 is most common
CREATE TABLE bill (
    transaction_id DECIMAL(12, 0) PRIMARY KEY,
    date DATE,
    cid DECIMAL(4, 0),
    paymentmode varchar(10),
    FOREIGN KEY(cid) REFERENCES customer(cid) ON DELETE RESTRICT
);