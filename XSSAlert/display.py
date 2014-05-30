#! /usr/bin/env python
'''
Created on Sep 5, 2010

@author: Arjun
'''

from xml.dom import minidom
from xml.dom.minidom import Document
from XSSAlert.uipy.ui_resultdisplay import Ui_resultxss
from PyQt4 import QtGui,QtCore
from XSSAlert.xssclass import Xssalert
from XSSAlert.exlib import bitly,tinyurl
import hashlib,datetime,time,webbrowser,os

finalUrl=[]
hashstring=hashlib.md5(str(datetime.datetime.now())).hexdigest()
DEFAULT_XSS='">'+hashstring
    
    
class Displayresult(QtGui.QMainWindow,Ui_resultxss):    
    
    closed=QtCore.pyqtSignal()
        
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)          
        self.parent=parent
        self.connect(self.BrowserButton,QtCore.SIGNAL('pressed()'),self.showinbrowser)
        
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
    
    def setvalue(self,urls,get,getflag,post,postflag,xmloutput,xmlfilename,fuzzvectorflag,fuzzvectors,verbose,full_reportflag,author_name,author_email,extrahttpheaderflag,extrahttpheader,extrapayloadflag,extrapayload,cookieflag,cookie,refererflag,referer,timeoutflag,timeout,URLSHORTAPIFLAG,URLSHORTAPI,agent,dpath):    
        self.urls=urls
        self.querystring=get
        self.getflag=getflag
        self.postflag=postflag
        self.poststring=post
        self.xmlfileflag=xmloutput
        self.xmlfilename=xmlfilename
        self.payloadflag=fuzzvectorflag
        self.payload=fuzzvectors
        self.verboseflag=verbose
        self.fullreportflag=full_reportflag
        self.author_name=author_name
        self.author_email=author_email
        self.extrahttpheaderflag=extrahttpheaderflag
        self.extrahttpheader=extrahttpheader
        self.extrapayload=extrapayload
        self.extrapayloadflag=extrapayloadflag
        self.cookieflag=cookieflag
        self.cookie=cookie
        self.refererflag=refererflag
        self.referer=referer
        self.timeoutvalue=timeout
        self.timeoutvalueflag=timeoutflag
        self.urlshortapi=URLSHORTAPI
        self.urlshotapiflag=URLSHORTAPIFLAG
        self.agent=agent
        self.dpath=dpath
        self.connect(self.start_button,QtCore.SIGNAL('pressed()'),self.runxssdetect)
        
    def runxssdetect(self):
        bitlyflag=0
        tinyurlflag=0
        error=0
        p=Xssalert()            
        payloads=[]
        
        if self.timeoutvalueflag:
            p.set_timeout(self.timeoutvalue)
        if self.cookieflag:
            p.set_cookie(self.cookie)
        if self.refererflag:
            p.set_referer(self.referer)
        if self.extrahttpheaderflag:
            p.set_header(self.extrahttpheader)
        p.set_agent(str(self.agent))
        
        p.close()
        
        api=""
        
        if self.urlshotapiflag==1:
            if self.urlshortapi=="Bit.ly":
                api=bitly.Api(login='arjunjain',apikey='R_391167cfede7dea1eaef94ff49c98a86')
                bitlyflag=1
            elif self.urlshortapi=="TinyUrl":
                tinyurlflag=1
        
        hash_found=[]
        hash_notfound=[]
        openbrowser=[]
        
        fquerystring=self.querystring
        fpoststring=self.poststring
        
        global hashstring
        fhash=hashstring
        
        absp= os.path.abspath(__file__)
        dirp= os.path.dirname(absp)
        if self.payloadflag:
                
            if self.payload[0]:
                try:
                    fzpath=dirp+"/fuzzvector/dcpvector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.wholeText.encode('ascii','ignore').strip())
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in dcp fuzz vector"))
            
            if self.payload[1]:
                try:
                    fzpath=dirp+"/fuzzvector/basicvector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in basic fuzz vector"))
           
            if self.payload[2]:
                try:
                    fzpath=dirp+"/fuzzvector/eventvector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in event fuzz vector"))         
            
            if self.payload[3]:
                try:
                    fzpath=dirp+"/fuzzvector/embeddedeventvector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in Embeddedevent fuzz vector"))
            
            if self.payload[4]:
                try:
                    fzpath=dirp+"/fuzzvector/charencodevector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in Character encode fuzz vector"))
            
            if self.payload[5]:
                try:
                    fzpath=dirp+"/fuzzvector/embeddedcharencodevector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in Embedded Character encode fuzz vector"))
            
            if self.payload[6]:
                try:
                    fzpath=dirp+"/fuzzvector/regularHTMLvector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in RegularHTML fuzz vector"))
            
            if self.payload[7]:
                try:
                    fzpath=dirp+"/fuzzvector/urlobfussionvector.xml"
                    v1=minidom.parse(fzpath)
                    allurl= v1.getElementsByTagName("vector")
                    dc=[]
                    for i in allurl:
                        dc.append(i.firstChild.data.encode('ascii','ignore'))
                    payloads=payloads+dc
                except:
                    error=1
                    QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error in URLobfussion fuzz vector"))
        
        else:
            payloads=[DEFAULT_XSS]
        
        
        if self.extrapayloadflag:
            payloads=payloads+self.extrapayload
        
        total_vectors=len(payloads)
        
        progress_param2_pre=0
        try:
            progress_param2_pre=100/total_vectors
        except:
            error=1
            QtGui.QMessageBox.warning(self,"Error:",str("Unexpected error"))
        
        dif=0
        
        if progress_param2_pre < 1:
            dif=1-progress_param2_pre
        progress_param2_pre+=dif
        
        self.start_button.setEnabled(False)
        self.BrowserButton.setEnabled(False)
            
        initimeS=time.gmtime().tm_sec
        initimeM=time.gmtime().tm_min
        initimeT=(initimeM*60)+initimeS

        self.outputxss.setRowCount(total_vectors*1)      
        
        i=0
        
        if not error :
            for payload in payloads:
                mod_payload=payload.strip().replace('XSS',fhash)
                c=Xssalert()
                dest_url=""
                if self.getflag:
                    final_payload=fquerystring.strip()+mod_payload
                    dest_url=self.urls.strip()+"/"+final_payload
                    c.get(dest_url)
                elif self.postflag:
                    final_payload=fpoststring.strip()+mod_payload
                    dest_url=final_payload
                    dest_url = dest_url.strip()
                    c.post(self.urls,dest_url)
                else:
                    final_payload=mod_payload
                    dest_url=self.urls.strip()+"/"+final_payload
                    c.get(dest_url)
                    
                
                if c.info()['http-code']=="200":
                    if bitlyflag==1:
                        shorturl=api.shorten(dest_url)
                        surl=QtGui.QTableWidgetItem(shorturl)
                        shttp=QtGui.QTableWidgetItem(c.info()['http-code'])
                        self.outputxss.setItem(i,0,surl)
                        self.outputxss.setItem(i,1,shttp)   
                        hash_found.append((shorturl,c.info()['http-code'],self.urls))
                        openbrowser.append((shorturl))
                    elif tinyurlflag==1:
                        shorturl=tinyurl.create_one(dest_url)
                        surl=QtGui.QTableWidgetItem(shorturl)
                        shttp=QtGui.QTableWidgetItem(c.info()['http-code'])
                        self.outputxss.setItem(i,0,surl)
                        self.outputxss.setItem(i,1,shttp)
                        hash_found.append((shorturl,c.info()['http-code'],self.urls))
                        openbrowser.append((shorturl))
                    else:
                        surl=QtGui.QTableWidgetItem(dest_url.strip())
                        shttp=QtGui.QTableWidgetItem(c.info()['http-code'])
                        self.outputxss.setItem(i,0,surl)
                        self.outputxss.setItem(i,1,shttp)
                        hash_found.append((dest_url,c.info()['http-code'],self.urls))
                        openbrowser.append((dest_url))
                    if self.verboseflag:
                            self.outputxss.setColumnCount(7)
                            stime=QtGui.QTableWidgetItem(c.info()['total-time'])
                            sheader_size=QtGui.QTableWidgetItem(c.info()['header-size'])
                            sreq_size=QtGui.QTableWidgetItem(c.info()['request-size'])
                            scontent_type=QtGui.QTableWidgetItem(c.info()['content-type'])
                            
                            shtime=QtGui.QTableWidgetItem("Total-time")
                            shheader=QtGui.QTableWidgetItem("Header-size")
                            shreq_size=QtGui.QTableWidgetItem("Request-size")
                            shcontent_type=QtGui.QTableWidgetItem("Content-type")
                            
                            self.outputxss.setHorizontalHeaderItem(3,shtime)
                            self.outputxss.setHorizontalHeaderItem(4,shheader)
                            self.outputxss.setHorizontalHeaderItem(5,shreq_size)
                            self.outputxss.setHorizontalHeaderItem(6,shcontent_type)
                            
                            self.outputxss.setItem(i,3,stime)
                            self.outputxss.setItem(i,4,sheader_size)
                            self.outputxss.setItem(i,5,sreq_size)
                            self.outputxss.setItem(i,6,scontent_type)
                            
                    sresult=QtGui.QTableWidgetItem("Successful")
                    self.outputxss.setItem(i,2,sresult)
                 
                else:
                    if bitlyflag==1:
                        shorturl=api.shorten(dest_url)
                        surl=QtGui.QTableWidgetItem(shorturl)
                        shttp=QtGui.QTableWidgetItem(c.info()['http-code'])
                        self.outputxss.setItem(i,0,surl)
                        self.outputxss.setItem(i,1,shttp)
                        hash_notfound.append((shorturl,c.info()['http-code'],self.urls))
                    elif tinyurlflag==1:
                        shorturl=tinyurl.create_one(dest_url)
                        surl=QtGui.QTableWidgetItem(shorturl)
                        shttp=QtGui.QTableWidgetItem(c.info()['http-code'])
                        self.outputxss.setItem(i,0,surl)
                        self.outputxss.setItem(i,1,shttp)
                        hash_notfound.append((shorturl,c.info()['http-code'],self.urls))
                    else:
                        surl=QtGui.QTableWidgetItem(dest_url.strip())
                        shttp=QtGui.QTableWidgetItem(c.info()['http-code'])
                        self.outputxss.setItem(i,0,surl)
                        self.outputxss.setItem(i,1,shttp)
                        hash_notfound.append((dest_url,c.info()['http-code'],self.urls))
                    if self.verboseflag:
                            self.outputxss.setColumnCount(7)
                            stime=QtGui.QTableWidgetItem(c.info()['total-time'])
                            sheader_size=QtGui.QTableWidgetItem(c.info()['header-size'])
                            sreq_size=QtGui.QTableWidgetItem(c.info()['request-size'])
                            scontent_type=QtGui.QTableWidgetItem(c.info()['content-type'])
                            
                            shtime=QtGui.QTableWidgetItem("Total-time")
                            shheader=QtGui.QTableWidgetItem("Header-size")
                            shreq_size=QtGui.QTableWidgetItem("Request-size")
                            shcontent_type=QtGui.QTableWidgetItem("Content-type")
                            
                            self.outputxss.setHorizontalHeaderItem(3,shtime)
                            self.outputxss.setHorizontalHeaderItem(4,shheader)
                            self.outputxss.setHorizontalHeaderItem(5,shreq_size)
                            self.outputxss.setHorizontalHeaderItem(6,shcontent_type)
                            
                            self.outputxss.setItem(i,3,stime)
                            self.outputxss.setItem(i,4,sheader_size)
                            self.outputxss.setItem(i,5,sreq_size)
                            self.outputxss.setItem(i,6,scontent_type)
                            
                    sresult=QtGui.QTableWidgetItem("Not injected")
                    self.outputxss.setItem(i,2,sresult)
                self.outputxss.resizeColumnsToContents()        
                i=i+1
                c.close()

                val=self.resultprogressbar.value()+progress_param2_pre
                self.resultprogressbar.setValue(val)
        
        ftimeS=time.gmtime().tm_sec
        ftimeM=time.gmtime().tm_min
        ftimeT=(ftimeM*60)+ftimeS
        if self.fullreportflag:
            f1=open(self.dpath+"/fullreport.txt","w")
            f1.write("XSS Alert\n")
            f1.write("\n@author  "+self.author_name)
            f1.write("\n@email  "+self.author_email)
            f1.write("\n@datetime  "+str(datetime.datetime.now())+"\n")
            for i in hash_found:
                f1.write("\n\n@url "+i[2])
                f1.write("\n@attack_url "+i[0])
                f1.write("\n@http-code "+i[1])
            for i in hash_notfound:
                f1.write("\n\n@url "+i[2])
                f1.write("\n@attack_url "+i[0])
                f1.write("\n@http-code "+i[1])
            f1.close()
        if self.xmlfileflag:
            dom=Document()
            x=dom.createElement("xssalert")
            dom.appendChild(x)
            fout=open(self.dpath+"/"+self.xmlfilename,"w")
            if len(hash_found)>0:
                    for line in hash_found:            
                        xa=dom.createElement("xssalertresult")
                        x.appendChild(xa)
                        ul=dom.createElement("targeturl")
                        xa.appendChild(ul)
                        ultest=dom.createTextNode(line[2])
                        ul.appendChild(ultest)
                        aul=dom.createElement("attackurl")
                        xa.appendChild(aul)
                        aultext=dom.createCDATASection(line[0])
                        aul.appendChild(aultext)
                        brw=dom.createElement("http-code")
                        xa.appendChild(brw)
                        brwtext=dom.createTextNode(line[1])
                        brw.appendChild(brwtext)
                        
                    fout.write(dom.toprettyxml(indent="  "))
                    fout.close()
            else:
                    xa=dom.createElement("xssalertresult")
                    x.appendChild(xa)
                    aul=dom.createElement("notfound")
                    xa.appendChild(aul)
                    aultext=dom.createTextNode("Not found any attack vector")
                    aul.appendChild(aultext)
                    fout.write(dom.toprettyxml(indent="  "))
                    fout.close()    
        i=0
        self.outputsuccessfull_vectors.setRowCount(len(hash_found))
        if (len(hash_found)>0):
                for line in hash_found:
                    surl=QtGui.QTableWidgetItem(line[0])
                    self.outputsuccessfull_vectors.setItem(i,0,surl)
                    i=i+1
        
        self.resultprogressbar.setValue(100)
        
        global finalUrl
        finalUrl=openbrowser
        
        self.total_vectors.setText(""+str(len(hash_found)+len(hash_notfound)))
        self.successfull_vectors.setText(""+str(len(hash_found)))
        self.failed_vectors.setText(""+str(len(hash_notfound)))
        self.total_time.setText(""+str(ftimeT-initimeT)+" S")
        if len(hash_found)>0:
            self.BrowserButton.setEnabled(True)
        
        
    def errordisplay(self,str1):
        QtGui.QMessageBox.warning(self, "Xss Alert : Error ",str(str1))
    def showinbrowser(self):
        for i in finalUrl:
            webbrowser.open_new_tab(i)
