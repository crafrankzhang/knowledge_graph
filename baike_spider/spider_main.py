# -*- coding: utf-8 -*-
#总的调度器
#==============================================================================
# 提供对各个模块的调度————craw（）函数
#==============================================================================
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain():
    def __init__(self):

        self.urls = url_manager.UrlManager() #初始化url管理器对象
        self.downloader = html_downloader.HtmlDownloader() #初始化url下载器对象
        self.parser = html_parser.HtmlParser()  #初始化html解析器对象
        self.outputer = html_outputer.HtmlOutputer() #初始化html输出对象

    def craw(self, root_url):

        count = 1 #记录爬取的url数目

        self.urls.add_new_url(root_url) #将源url添加到url管理器中

            
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                results= self.parser.parsee(html_cont)
                for result in results
                 url name = result
                 self.add_new_urls(url)

                 with open(visualization/data/entities_fi, 'w') as fw:
                 for result in results
                 url name = result
                  fw.write(name)
                  fw.write('\n')
                  fw.close()

                  with open(visualization/data/entities_se, 'w') as fw:
                 for result in results
                 url name = result
                  fw.write(name)
                  fw.write('\n')
                  fw.close            

          while self.urls.has_new_url(): 
                try:
                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                results= self.parser.parseee(html_cont)
                 with open(visualization/data/entities_fi, 'w') as fw:
                 for result in results
                  intro= result
                  fw.write(intro)
                  fw.write('\n')
                  fw.close()
               
               new_url = 'https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/1450?fr=aladdin'
                html_cont = self.downloader.download(new_url) 
                results= self.parser.parsee(html_cont)
                for result in results
                 url name = result
                 self.add_new_urls(url)




                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseone(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()




                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsetwo(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsethree(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsefour(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()




                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsefive(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()




                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsesix(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseseven(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseeight(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsenine(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseten(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseeleven(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsetwelve(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsethirteen(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsefourteen(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()




                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsefifteen(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsesixteen(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()




                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseseven(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()



                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseeight(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
               
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()


                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parseninteen(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()


                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsetwenty(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()


                ew_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url) 
                result= self.parser.parsetwenty(html_cont)
                 
                 
                 with open(visualization/data/entities_se, 'w') as fw:
                 
                 first second third fourth = result
                  fw.write(first second third fourth)
                  fw.write('\n')
                  fw.close()









                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw failed'
        

if __name__=="__main__":
    root_url = 'https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/1450?fr=aladdin'
    spider = SpiderMain()
    spider.craw(root_url)


#