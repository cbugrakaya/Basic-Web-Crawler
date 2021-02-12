# Basic-Web-Crawler
This is a basic web crawler with  Scrapy library in Python. In this project, Our aim  collect  information for some products in https://www.spx.com.tr/.


## Used Tech-Stack
- Scrapy for Web Crawling
- Pandas for Read Excel File
- Python

OS : Windows 10<br/>
Editor : VS Code
## The challenges I faced
In this project, I've overcome the two problems. These are;

- Some products page have different HTML structure to collect, So I had to write different conditions to detect this differences.
- Write results to excel file with separate columns, But after some research I found a library for this purpose.

## What I learned from this project

- How ı can write my results to excel file.

- How to get data faster and more efficiently.

## Additional Questions
1.There are several ways to get  more data faster. Things you can do for this purpose;

- Instead of crawling data with a single large spider, you can be split into smaller pieces and pulled data simultaneously with these smaller pieces.

- When upload or write data to databases or some files, You can use batching logic. These means instead of write each data to file in each loop, you can collect these all data in dataFrame or dictionary then upload all data in one go. 

- In the settings file to avoid problems arising from internet speed, you can change *CONCURRENT_REQUESTS*, *DOWNLOAD_TIMEOUT*, *DOWNLOAD_DELAY*.

2. We can call APIs the WhatsApp of programs in systems. The purpose of APIs is to enable programs to communicate with each other. For example, You wanted to get a drink from Getir and opened the mobile app.Then, you have chosen a drink and ordered.In fact, placing this order, checking whether it is in the warehouse (or database), or reporting this order to the warehouse is done entirely via API.
