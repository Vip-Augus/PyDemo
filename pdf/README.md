
# **学习爬虫,将网页转成PDF**

[原地址传送门](https://github.com/lzjun567/crawler_html2pdf/tree/master/pdf)
当成入门学习，当时不想直接复制，于是手写跟着大神的思路锻炼一下。
## **系统要求**
**要使用Python3.4以上的版本**

## **使用工具**
前两个工具是用来爬虫的，大家应该都知道它的好用了。
第三个工具是用来生成pdf的，我也是第一次使用wkhtmltopdf,贼好用。
windows用户直接去[官网]( http://wkhtmltopdf.org/downloads.html)下载稳定版就可以了，个人系统是win10，下载第一个进行安装，记得要在系统变量$PATH中添加wkhtmltopdf的bin路径。
```
pip install requests
pip install beautifulsoup4
pip install pdfkit
```

## **遇到过的问题**

### **1. 提示提示OSError: No wkhtmltopdf executable found: "b''"**
这个解决方法简单，是由于你在PATH中配置中有\bin，路径含有ASCII BACKSPACE，代码中会转义，导致找不到这个路径。
```python
#在这里就注明路径名，使用r""
config = pdfkit.configuration(wkhtmltopdf=r"F:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_file(htmls, self.name + '.pdf', options=options, configuration=config)
```

### **2. 还有配置参数options=options**
当时里面的配置参数没有写对，导致报错
```python
options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': 'UTF-8',
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2')
            ],
            'outline-depth': 10,
        }

```