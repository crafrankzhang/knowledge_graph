# -*- coding: utf-8 -*-
#html解析器

#==============================================================================
# 解析器对外提供一个方法parse()
#==============================================================================
from bs4 import BeautifulSoup
import urlparse
import re
class HtmlParser():

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parseone(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results


    
 def parsetwo(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    for resecond in ress.find_all(a)
                    results+=resecond.get_text()

        return results

 def parsethree(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsefour(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsefive(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsesix(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseseven(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseeight(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsenine(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseten(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseeleven(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsetwelve(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsethirteen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsefourteen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsefifteen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsesixteen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseseventeen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseeighteen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parseninteen(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results

 def parsetewnty(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        results=""
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        res=soup.find_all('class=para')
        for result in res
             reults+=" "
            for ress in result.select('#label-model')
                    results+=ress.get_text()

        return results



    def parsee(html_cont):
        pattern=re.compile("^<span.*?entry.*?><a.*?href.*/(.*?).*?title.*?>(.*?).*?span>$",re.S) 
        result=re.find_all(pattern,html_cont)
         return result.group(1),result.group(2)

     def parseee(html_cont):
        pattern=re.compile("^div.*?class.*?para.*?>(.*?)<a.*?href.*/(.*?).*?title.*?>(.*?).*?span>$",re.S) 
        result=re.find_all(pattern,html_cont)
         return result.group(1)   
        

