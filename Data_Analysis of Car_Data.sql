## Analyzing Car_sales_dataa
 step 01:Create the Table
        CREATE TABLE car_sales (
    Car_Name VARCHAR(100),
    Year INT,
    Selling_Price FLOAT,
    Present_Price FLOAT,
    Kms_Driven INT,
    Fuel_Type VARCHAR(50),
    Seller_Type VARCHAR(50),
    Transmission VARCHAR(50),
    Owner INT
);
 step 02: Insert_the_Data
    COPY car_sales FROM '/path/to/Car Sell Dataset.csv' DELIMITER ',' CSV HEADER;
 
 step 03: Basic Analysis Queries
     ## Total Records
	   SELECT COUNT(*) FROM car_sales;
  step  04: Average Selling Price
       SELECT AVG(Selling_Price) AS Avg_Selling_Price
	   FROM car_sales;

  step 05:Cars  Fuel_Type
       SELECT Fuel_Type, COUNT(*) AS Count FROM car_sales
	   GROUP BY Fuel_Type;

   step 06:Cars by_Year
        SELECT Year, COUNT(*) AS Count FROM car_sales
		GROUP BY Year ORDER BY Year DESC;

  step 07:Most Expensive Cars Sold
        SELECT * FROM car_sales
		ORDER BY Selling_Price DESC 
		LIMIT 5;
  
  step 08:Cars with Manual Transmission
         SELECT * FROM car_sales 
		 WHERE Transmission = 'Manual';
   