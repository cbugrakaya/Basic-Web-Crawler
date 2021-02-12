import scrapy
import pandas as pd


class SportSpider(scrapy.Spider):
    name = "sport"

    start_urls = []

    excel_df = pd.read_excel('urls.xlsx',"Sheet4",header=None)
    start_urls= ["https://www.spx.com.tr" + url for url in excel_df[0].tolist()]


    def parse(self, response):
        product_brand = response.css('.product__brand::text').extract_first()
        product_name = response.css('.product__title::text').extract_first().strip()
        product_price = response.css('.product__price::text').extract_first().strip()
        product_code =  response.css('.product__code.d-none.d-lg-block::text').extract_first().strip()
        product_inventory = response.xpath('//a[@class="d-flex align-items-center justify-content-center text-reset product__variant product__size-variant mb-3 js-variant"]/@data-value').extract() 
        
        #for ski 
        if len(product_inventory) == 0:                               
            product_inventory = response.xpath('//a[@class="d-flex align-items-center justify-content-center text-reset product__variant product__size-variant mb-3 js-variant selected font-weight-bold"]/@data-value').extract()
            #for watch
            if len(product_inventory) == 0: 
                product_inventory = response.xpath('//a[@class="d-flex flex-column align-items-center text-reset product__variant product__color-variant js-variant p-1 border-black selected"]/@data-variant-value').extract()


        yield{
                "Product Code" : product_code,
                "Product Brand" : product_brand,
                "Product Name" : product_name,
                "Product Price" : product_price,
                "Product Inventory" : product_inventory
        }
        