import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Ocean-Blue-Storage/dp/B07HGJKDQL?ref_=Oct_s9_apbd_orecs_hd_bw_b1yBwdz&pf_rd_r=55ER8G6AQWTCQRMB1Q3V&pf_rd_p=94baa1a4-2f06-554d-82db-8b9866e02276&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1805560031&tag=coa_in-21",
        "name": "Samsung M31",
        "target_price": 16000
    },
    {
        "product_url": "https://www.amazon.in/Test-Exclusive-668/dp/B07HGH88GL/ref=psdc_1805560031_t1_B07HGJKDQL",
        "name": "Samsung M21 6GB 128RAM",
        "target_price":12000
    },
    {
        "product_url": "https://www.amazon.in/Test-Exclusive-553/dp/B0784D7NFQ/ref=sr_1_12?crid=2RE70JAZ07V4M&dchild=1&keywords=redmi+note+9&qid=1599449618&s=electronics&sprefix=redmi+%2Celectronics%2C-1&sr=1-12",
        "name": "Redmi Note 9 Pro",
        "target_price":14000
    },
    {
        "product_url":"https://www.amazon.in/Realme-narzo-Laser-Storage-Without/dp/B08Y6K9FGT/ref=sxin_2_hcs-la-in-1?cv_ct_cx=realme&dchild=1&keywords=realme&pd_rd_i=B08Y6K9FGT&pd_rd_r=a0ef6f40-ef8c-4a44-852b-ff5ff234f97f&pd_rd_w=gzpxJ&pd_rd_wg=KE3pa&pf_rd_p=d031f178-1441-40fa-8c98-e0853f028cc4&pf_rd_r=W3KKNT5Q6NFMG96FPS2K&qid=1620908655&sr=1-1-99b054f1-0e42-4e3b-b375-028105b26bc6",
        "name":"Realme nazro",
        "target_price":9940

    },
    {
        "product_url":"https://www.amazon.in/Test-Exclusive_2020_1128-Multi-3GB-Storage/dp/B089MVC437/ref=sr_1_1?dchild=1&keywords=mi&qid=1620908874&s=electronics&sr=1-1",
        "name":"MI 10i 5G",
        "target_price":21999

    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }
    page = requests.get(URL, headers=headers)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")



    return product_price.getText()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/70.0.3728.106"
    }
    page = requests.get(URL, headers=headers)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_ourprice")



    return product_price.getText()

    result_file=open('my_result_file_txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally :
    result_file.close()




