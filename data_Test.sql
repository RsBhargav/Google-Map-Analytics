CREATE TABLE Places
(
 [Name] nvarchar(50),
 [Place_ID] varchar(50),
 [Address] varchar(50)
 [Latitude] varchar(50),
 [Longitude] varchar(50),
 [Ratings] varchar(10),
 [Total_Ratings] varchar(10),
 [route] varchar(50),
 [sublocality_level_2] varchar(50),
 [sublocality_level_1] varchar(50),
 [locality] varchar(50),
 [administrative_area_level_1] varchar(10),
 [country] varchar(10),
 [postal_code] varchar(6)
)



select * from Places

drop table Places

truncate table Places