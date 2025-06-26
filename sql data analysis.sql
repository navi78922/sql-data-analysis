select * from items_data
1. Total revenue
select items,  sum(quantity*price)as Total_revenue from items_data
group by items

2.Monthly Sales
 select To_char( date,'yyyy-mm')as monthly_sales,sum(quantity*price) as 
 total_revenue from items_data
 group by To_char( date,'yyyy-mm')
 order by monthly_sales;

3.Top customers by_revenue
  SELECT 
    Customer_Name,
    SUM(Quantity * Price) AS Revenue
FROM items_data
GROUP BY Customer_Name
ORDER BY Revenue DESC;

4.Best-Selling Products by _Quantity
SELECT 
    items,
    SUM(Quantity) AS Total_Quantity_Sold
FROM items_data
GROUP BY items
ORDER BY Total_Quantity_Sold DESC;

5.Sales by_Region

SELECT 
    Region,
    SUM(Quantity * Price) AS Region_Revenue
FROM items_data
GROUP BY Region;

6.Average Order_Value
  SELECT 
    AVG(Quantity * Price) AS Avg_Order_Value
FROM items_data;

7.Customer Purchase Frequency
 SELECT 
    Customer_Name,
    COUNT(*) AS Number_of_Purchases
FROM items_data
GROUP BY Customer_Name;
 