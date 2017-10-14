import traceback
import re
import requests
import pymysql
from bs4 import BeautifulSoup

base_url = "https://book.douban.com/top250?start=0"
conn = pymysql.connect("localhost", "root", "123456", "test", use_unicode=True, charset="utf8")
cursor = conn.cursor()


def save_to_database(book_name, book_author, book_image, book_from, book_price, book_publisher, book_publish_date):
    sql = 'insert into c_book (book_name, book_author, book_image, book_from, book_price, book_publisher, book_publish_date) ' \
          'VALUES ("%s","%s","%s","%s","%f","%s","%s")' % \
          (book_name, book_author, book_image, book_from, book_price, book_publisher, book_publish_date)

    try:
        cursor.execute(sql)
        conn.commit()
        print('success')
    except:
        conn.rollback()
        traceback.print_exc()

def check_insert(book_name):
    def checkInsert(book_name):
        sql = 'select book_id from c_book WHERE book_name = ' + '\'' + book_name + '\''
        try:
            cursor.execute(sql)
            conn.commit()
            return cursor.fetchone()
        except:
            conn.rollback()
            traceback.print_exc()
            return None

def get_detail(url):
    global base_url
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    book_list = soup.find('div', 'indent')
    for item in book_list.find_all('tr', 'item'):
        book_name_from = item.find('div', 'pl2').a
        book_name = str(book_name_from.attrs['title'])
        book_from = str(book_name_from.attrs['href'])
        book_image = str(item.img.attrs['src'])
        message = item.find('p', 'pl').text

        msg_list = message.split('/')
        if (len(msg_list) == 4):
            book_author = str(msg_list[0])
            book_publisher = str(msg_list[1])
            book_publish_date = str(msg_list[2])
            # 通过正则表达式查找出来的是数组类型,使用join整合到字符串
            book_price = float("".join(re.findall(r"\d+\.?\d*", msg_list[3])))
        if (len(msg_list) == 5):
            book_author = str(msg_list[0])
            book_publisher = str(msg_list[2])
            book_publish_date = str(msg_list[3])
            # 通过正则表达式查找出来的是数组类型,使用join整合到字符串
            book_price = float("".join(re.findall(r"\d+\.?\d*", msg_list[4])))
        # print(book_name, book_author, book_image, book_from, book_price, book_publisher, book_publish_date)
        if(check_insert(book_name) == None):
            save_to_database(book_name, book_author, book_image, book_from, book_price, book_publisher,
                             book_publish_date)


    # 一个页面之后进行下一个页面的检索

    next_page = soup.find('span', attrs={'class': 'next'})
    if (next_page.find('a')):
        get_detail(next_page.find('a').attrs['href'])


get_detail(base_url)
