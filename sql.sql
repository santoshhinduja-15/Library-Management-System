create table library
(
	member varchar(50),
    PRN_NO varchar(45),
    ID varchar(45),
    first_name varchar(45),
    last_name varchar(45),
    address1 varchar(45),
    address2 varchar(45),
    postid varchar(45),
    mobile varchar(45),
    bookid varchar(45),
    booktitle varchar(100),
    author varchar(45),
    data_borrowed datetime,
    date_due datetime,
    dayasofbook varchar(45),
    latereturnfine varchar(45),
    dateoverdue varchar(45),
    finalprice varchar(45)
);

select * from library;