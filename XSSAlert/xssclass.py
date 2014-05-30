#! /usr/bin/env python 

'''
Created on Mar 7, 2011

@author: Arjun
'''

from io import StringIO
import pycurl,cStringIO,hashlib,datetime,urllib,mimetools,os
import XSSAlert.display

hashstring=hashlib.md5(str(datetime.datetime.now())).hexdigest()
DEFAULT_XSS='">'+hashstring

class Xssalert:
    agent='Googlebot/2.1 (+http://www.google.com/bot.html)'
    headers=None
    payloads=""    
    #proxy=None  
    def __init__(self,urls=""):
        self.handle=pycurl.Curl()
        self.header=cStringIO.StringIO()
        self.payloads=""
        self.set_targeturl(urls)
        self.set_option(pycurl.SSL_VERIFYHOST, 1)
        self.set_option(pycurl.SSL_VERIFYPEER, 0)
        self.set_option(pycurl.MAXREDIRS,3)
        self.set_option(pycurl.COOKIEFILE, "/dev/null")
        self.set_option(pycurl.WRITEFUNCTION,self.payload_callback)
        self.set_option(pycurl.HEADERFUNCTION,self.header_callback)
    
    def set_option(self, *args):
        apply(self.handle.setopt, args)
    def payload_callback(self,x):
        self.payload += x
    def header_callback(self,x):
        self.header.write(x)        
    def set_targeturl(self,urls):
        self.urls=urls
        self.set_option(pycurl.URL,self.urls)
    
    def get(self, url="", params=None):
        if params:
            url += "?" + urllib.urlencode(params)
        self.set_option(pycurl.HTTPGET, 1)
        return self.__request(url)
    
    def post(self,cgi,params):
        self.set_option(pycurl.POST,1)
        self.set_option(pycurl.POSTFIELDS,params)
        return self.__request(cgi)
    
    def body(self):
        return self.payload
    def set_timeout(self,timeout):
        self.set_option(pycurl.TIMEOUT,timeout)
        self.set_option(pycurl.CONNECTTIMEOUT,timeout)
    def set_agent(self,agent):
        self.set_option(pycurl.USERAGENT,agent)
    def set_proxy(self,proxy):
        self.set_option(pycurl.PROXY,proxy)
    def set_cookie(self,cookie):
        self.set_option(pycurl.COOKIEFILE,cookie)
    def set_referer(self,referer):
        self.set_option(pycurl.REFERER,referer)
    def set_header(self,header):
        self.set_option(pycurl.HTTPHEADER,header) 
    def close(self):
        self.handle.close()
        self.header.close()
    def __del__(self):
        self.close()
    def __request(self,relative_url=None):
        if relative_url:
            self.set_option(pycurl.URL,os.path.join(self.urls,relative_url))
        self.header.seek(0,0)
        self.payload=""
        try:
            self.handle.perform()   
        except:
            print "the Host can not be resolved"
            k=XSSAlert.display.Displayresult()
            k.errordisplay("The Host can not be resolved")
            exit()
            #k.start_button.setEnabled(True)
            
        return self.payload
    def info(self):
        self.header.seek(0,0)
        url=self.handle.getinfo(pycurl.EFFECTIVE_URL)

        if url[:5]=="http:":
            self.header.readline()
            m=mimetools.Message(self.header)
        else:
            m=mimetools.Message(StringIO())
        m['http-code']=str(self.handle.getinfo(pycurl.HTTP_CODE))
        m['total-time']=str(self.handle.getinfo(pycurl.TOTAL_TIME))
        m['namelookup-time']=str(self.handle.getinfo(pycurl.NAMELOOKUP_TIME))
        m['connect-time']=str(self.handle.getinfo(pycurl.CONNECT_TIME))
        m['pretransfer-time'] = str(self.handle.getinfo(pycurl.PRETRANSFER_TIME))
        m['redirect-time'] = str(self.handle.getinfo(pycurl.REDIRECT_TIME))
        m['redirect-count'] = str(self.handle.getinfo(pycurl.REDIRECT_COUNT))
        m['size-upload'] = str(self.handle.getinfo(pycurl.SIZE_UPLOAD))
        m['size-download'] = str(self.handle.getinfo(pycurl.SIZE_DOWNLOAD))
        m['speed-upload'] = str(self.handle.getinfo(pycurl.SPEED_UPLOAD))
        m['header-size'] = str(self.handle.getinfo(pycurl.HEADER_SIZE))
        m['request-size'] = str(self.handle.getinfo(pycurl.REQUEST_SIZE))
        m['content-length-download'] = str(self.handle.getinfo(pycurl.CONTENT_LENGTH_DOWNLOAD))
        m['content-length-upload'] = str(self.handle.getinfo(pycurl.CONTENT_LENGTH_UPLOAD))
        m['content-type'] = (self.handle.getinfo(pycurl.CONTENT_TYPE) or '').strip(';')
        return m
