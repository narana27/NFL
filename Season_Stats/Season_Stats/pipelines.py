# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class SeasonStatsPipeline:
    def open_spider(self, spider):
        self.files = {
            "output": open("output.csv", "w", newline="", encoding= "utf-8"),
            "Stats_labels": open("Stats_labels.csv", "w", newline="", encoding= "utf-8")
        }
        self.csv_writers = {
            "output": None,  # Placeholder for the writer to output.csv
            "Stats_labels": None  # Placeholder for the writer to Stats_labels.csv
        }

    def close_spider(self,spider):
        for file in self.files.values():
            file.close()

    def process_item(self, item, spider):
        if len(item) == 10:
            file_key = "Stats_labels"
        else:
            file_key = "output"
        if not self.csv_writers[file_key]:
            self.csv_writers[file_key] = csv.DictWriter(self.files[file_key], fieldnames=item.keys())
            self.csv_writers[file_key].writeheader()

            # Write the item to the appropriate file
        self.csv_writers[file_key].writerow(item)
        return item
