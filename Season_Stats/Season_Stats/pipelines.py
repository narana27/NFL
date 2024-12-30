# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class SeasonStatsPipeline:
    def open_spider(self, spider):
        self.file = open("output.csv", "w", newline="", encoding= "utf-8")
        self.csv_writer = None

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        if not self.csv_writer:
            self.csv_writer = csv.DictWriter(self.file, fieldnames = item.keys())
            self.csv_writer.writeheader()

        self.csv_writer.writerow(item)
        return item