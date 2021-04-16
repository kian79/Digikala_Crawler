# Digikala_Crawler
A simple program to crawl Digikala items and save them on a .csv file

## What is this?
This is a very simple program to get every item on [Digikala](https://www.digikala.com) and saves them on a csv file. This program uses Python and Scrapy library. For every item it saves title, price and its category.

## How to Use?
After downloading the codes you should just change directory to spider and type following command:

```
scrapy crawl Digikala -o csv_file_name.csv -t csv
```

When you used this command crawler starts to get every item on [Digikala](https://www.digikala.com) and saves them on your csv file.

## Example

After the program is finished or you stoped it using ctrl+c you can go to your .csv file and see its contents. The content is something like the following figure.

![crawler_example](examples/digikala_crawler.png)
