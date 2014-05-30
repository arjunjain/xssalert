#! /usr/bin/env python 
#-*- coding: utf-8 -*-

'''
Created on Sep 5, 2010

@author: Arjun
'''

from PyQt4 import QtGui
from PyQt4 import QtCore
from XSSAlert.uipy.ui_mainwindow import Ui_XSS_ALERT
import sys,os,shutil,urllib2,hashlib
from XSSAlert.display import Displayresult
from XSSAlert.uipy.ui_preferences import Ui_Preferences
from XSSAlert.uipy.ui_update import Ui_Update_Dialog
from XSSAlert.uipy.ui_about import Ui_XSSAlert_about 
from xml.dom import minidom
from xml.dom.minidom import Document


Mpath=""
Magent=""
FILEPATH=os.path.join(os.environ["HOME"],".XSSAlertConfig")

class MainWindow(QtGui.QMainWindow,Ui_XSS_ALERT):
   
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)	      
        
        self.getstring_textbox.setEnabled(False)
        self.poststring_textbox.setEnabled(False)
        self.xml_textbox.setEnabled(False)
        self.extrahttpheader_textbox.setEnabled(False)
        self.extrahttpheaderfile_textbox.setEnabled(False)
        self.extrahttpheaderfile_upload_button.setEnabled(False)
        self.extrapayload_upload_button.setEnabled(False)
        self.extrapayloadvector_textbox.setEnabled(False)
        self.extrapayloadvectorfile_textbox.setEnabled(False)
        self.cookie_textbox.setEnabled(False)
        self.referer_textbox.setEnabled(False)
        self.timeout_textbox.setEnabled(False)
        self.timeout_textbox.setEnabled(False)
        self.URLencoding_comboBox.setEnabled(False)
        self.hide_frame.hide()
        self.fuzz_frame.hide()
        
        self.connect(self.getstring_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.GetStringout)
        self.connect(self.poststring_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.PostStringout)
        self.connect(self.xml_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.XmlFileout)
        self.connect(self.show_fuzz,QtCore.SIGNAL("stateChanged(int)"),self.FUZZvectors)
        self.connect(self.full_report,QtCore.SIGNAL('stateChanged(int)'),self.showframe)
        self.connect(self.extrahttpheader_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.SetExtraHttpHeader)
        self.connect(self.extrahttpheaderfile_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.SetExtraHttpHeaderFile)
        self.connect(self.extrahttpheaderfile_upload_button,QtCore.SIGNAL('pressed()'),self.UploadExtraHttpHeader)
        self.connect(self.extrapayloadvector_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.SetExtraPayload)
        self.connect(self.extrapayloadvectorfile_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.SetExtraPayloadFile)
        self.connect(self.extrapayload_upload_button,QtCore.SIGNAL('pressed()'),self.UploadExtraPayloadVector) 
        self.connect(self.referer_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.SetReferer)
        self.connect(self.cookie_checkbox,QtCore.SIGNAL('stateChanged(int)'),self.SetCookie)
        self.connect(self.timeout_checkbox, QtCore.SIGNAL('stateChanged(int)'),self.SetTimeout)
        self.connect(self.URLencoding_checkbox,QtCore.SIGNAL("stateChanged(int)"),self.URLencoding)
        self.connect(self.create_default_XML,QtCore.SIGNAL('clicked()'),self.createfilexml)
        self.connect(self.delete_default_XML,QtCore.SIGNAL('clicked()'),self.deletefilexml)
        self.connect(self.start_button,QtCore.SIGNAL('clicked()'),self.Showresult)
        self.connect(self.actionPreferences,QtCore.SIGNAL("triggered()"),self.Preferences)
        
        global Mpath,Magent,FILEPATH 
        
        if not os.path.isfile(FILEPATH):
            f1=open(FILEPATH,"w")
            Magent="Googlebot/2.1 (+http://www.google.com/bot.html)\n"
            Mpath=str(QtCore.QDir.homePath())
            f1.write(Magent)
            f1.write(Mpath)
            f1.close()
        else:
            f1=open(FILEPATH,"r")
            rd=f1.read()
            rd=rd.split("\n")
            Magent=rd[0]
            Mpath=rd[1]
            f1.close()
        
        
    def Preferences(self):
        pr=Preferences()    
        pr.exec_()
        
    def deletefilexml(self):
        homep=Mpath
        if os.path.isdir(homep+"/xssalertdefault"):
            shutil.rmtree(homep+"/xssalertdefault")
            self.file_create_alert.setText("Default XML Files Deleted")
        else:
            self.file_create_alert.setText("No Default XML Files Present ")
    
    def createfilexml(self):
        
        global Mpath,Magent
        homep=Mpath
        if not os.path.isdir(homep+"/xssalertdefault"):
            os.mkdir(homep+"/xssalertdefault")
        
        f1=open(homep+"/xssalertdefault/payload.xml","w")
        f2=open(homep+"/xssalertdefault/header.xml","w")
        f3=open(homep+"/xssalertdefault/url.xml","w")
        
        dom1=Document()
        x=dom1.createElement("xssalert")
        dom1.appendChild(x)
        i=0
        while i < 2:
            xa=dom1.createElement("xssalertvector")
            x.appendChild(xa)
            vr=dom1.createElement("vector")
            xa.appendChild(vr)
            testvr=dom1.createCDATASection("??")
            vr.appendChild(testvr)
            i=i+1
        f1.write(dom1.toprettyxml("  "))
        
        dom2=Document()
        y=dom2.createElement("xssalert")
        dom2.appendChild(y)
        i=0
        while i<2:
            xb=dom2.createElement("xssalertheader")
            y.appendChild(xb)
            hr=dom2.createElement("header")
            xb.appendChild(hr)
            testhr=dom2.createCDATASection("??")
            hr.appendChild(testhr)
            i=i+1
        f2.write(dom2.toprettyxml("  "))
        
        dom3=Document()
        z=dom3.createElement("xssalert")
        dom3.appendChild(z)
        i=0
        while i<2:
            xc=dom3.createElement("xssalerturl")
            z.appendChild(xc)
            ur=dom3.createElement("url")
            xc.appendChild(ur)
            testhr=dom3.createCDATASection("??")
            ur.appendChild(testhr)
            i=i+1
        f3.write(dom3.toprettyxml("  "))
        
        f1.close()
        f2.close()
        f3.close()
        
        self.file_create_alert.setText("Default directory with XML files Created in '"+homep+"'  \n  Replace '??' with your text")    
            
    def SetCookie(self):
        if self.cookie_checkbox.isChecked():
            self.cookie_textbox.setEnabled(True)
        else:
            self.cookie_textbox.setEnabled(False)

    def SetReferer(self):
        if self.referer_checkbox.isChecked():
            self.referer_textbox.setEnabled(True)
        else:
            self.referer_textbox.setEnabled(False)

    def SetTimeout(self):
        if self.timeout_checkbox.isChecked():
            self.timeout_textbox.setEnabled(True)
        else:
            self.timeout_textbox.setEnabled(False)    
            
    def URLencoding(self):
        if self.URLencoding_checkbox.isChecked():
            self.URLencoding_comboBox.setEnabled(True)
        else:
            self.URLencoding_comboBox.setEnabled(False)
    
    def SetExtraPayload(self):
        if self.extrapayloadvector_checkbox.isChecked():
            self.extrapayloadvector_textbox.setEnabled(True)
        else:
            self.extrapayloadvector_textbox.setEnabled(False)
            
    def SetExtraPayloadFile(self):
        if self.extrapayloadvectorfile_checkbox.isChecked():
            self.extrapayloadvectorfile_textbox.setEnabled(True)
            self.extrapayload_upload_button.setEnabled(True)
        else:
            self.extrapayloadvectorfile_textbox.setEnabled(False)
            self.extrapayload_upload_button.setEnabled(False)
    
    def UploadExtraPayloadVector(self):
        filename=str(QtGui.QFileDialog.getOpenFileName(self,self.tr('XSSAlert - Select Payload XML File'),Mpath,"*.xml"))
        self.extrapayloadvectorfile_textbox.setText(filename)
        
    def SetExtraHttpHeader(self):
        if self.extrahttpheader_checkbox.isChecked():
            self.extrahttpheader_textbox.setEnabled(True)        
        else:
            self.extrahttpheader_textbox.setEnabled(False)
    
    def UploadExtraHttpHeader(self):
        filename=str(QtGui.QFileDialog.getOpenFileName(self,self.tr('XSSAlert - Select HTTP Header XML File'),Mpath,"*.xml"))
        self.extrahttpheaderfile_textbox.setText(filename)
    
    def SetExtraHttpHeaderFile(self):
        if self.extrahttpheaderfile_checkbox.isChecked():
            self.extrahttpheaderfile_textbox.setEnabled(True)
            self.extrahttpheaderfile_upload_button.setEnabled(True)
        else:
            self.extrahttpheaderfile_textbox.setEnabled(False)
            self.extrahttpheaderfile_upload_button.setEnabled(False)        
    
    def showframe(self):
        if self.full_report.isChecked():
            self.hide_frame.show()
        else:
            self.hide_frame.hide()
    
    def FUZZvectors(self):
        if self.show_fuzz.isChecked():
            self.fuzz_frame.show()
        else:
            self.fuzz_frame.hide()
                     
    def XmlFileout(self):
        if self.xml_checkbox.isChecked():
            self.xml_textbox.setEnabled(True)
            self.xml_textbox.setText("output.xml")
        else:
            self.xml_textbox.setEnabled(False)
            self.xml_textbox.setText("")
     
    def PostStringout(self):
        if self.poststring_checkbox.isChecked():
            self.poststring_textbox.setEnabled(True)
            self.getstring_checkbox.setChecked(False)
        else:
            self.poststring_textbox.setEnabled(False)        
    
    def GetStringout(self):
        if self.getstring_checkbox.isChecked():
            self.getstring_textbox.setEnabled(True)
            self.poststring_checkbox.setChecked(False)
        else:
            self.getstring_textbox.setEnabled(False)
    
                    
    
    def Showresult(self):
        
        error=0
        urlu=""
        get=""
        post=""
        xmlfilename=""
        fuzzvectors=[]
        author_name=""
        author_email=""
        extrahttpheader=[]
        extrapayload=[]
        referer=""
        cookie=""
        timeout=30
        URLSHORTAPI=""
        
            ## Flags
        
        getflag=0
        postflag=0
        xmloutput=0
        fuzzvectorflag=0
        full_reportflag=0
        verbose=0
        extrahttpheaderflag=0
        extrapayloadflag=0
        timeoutflag=0
        cookieflag=0
        refererflag=0
        URLSHORTAPIFLAG=0     
        
        ##### URL #####
        
    
        urlu=str(self.url_textbox.text())
        urlu=urlu.strip() 
        if urlu.find(".")!=-1 and (urlu[0:7]=="http://" or urlu[0:8]=="https://") and urlu[-1]!='/':
            urlu=urlu
        else:
            error=1
            QtGui.QMessageBox.warning(self,"Error:",str("Please enter valid URL"))
            
        #####
        ####### GET AND POST STRING #####
        
        if self.getstring_checkbox.isChecked():
            get=str(self.getstring_textbox.text())
            get=get.strip()
            getflag=1
        if self.poststring_checkbox.isChecked():
            post=str(self.poststring_textbox.text())
            post=post.strip()
            postflag=1
        
        #####
        ##### OUTPUT FILE #####
        
        if self.xml_checkbox.isChecked():
            xmlfilename=str(self.xml_textbox.text())
            xmloutput=1
        
        #####
        ##### Fuzz vector , Verbose , Full Report
        
        if self.show_fuzz.isChecked():
            fuzzvectorflag=1
            if self.DCP_checkBox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.basicfuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.eventfuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.embeddedeventfuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.charencodefuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.embeddedcharencodefuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.regularfuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
            if self.urlfuzz_checkbox.isChecked():
                fuzzvectors.append(1)
            else:
                fuzzvectors.append(0)
                
        if self.verbose_checkbox.isChecked():
            verbose=1
        
        if self.full_report.isChecked():
            full_reportflag=1
            author_name=str(self.author_name_text.text())
            author_name=author_name.strip()
            author_email=str(self.author_email_text.text())
            author_email=author_email.strip()
            if author_email == "" or author_name=="":
                error=1
                QtGui.QMessageBox.warning(self,"Error",str("Enter the correct value of Email or Password"))       
                
        #####
        ########## Extra Http Header #######
        
        if self.extrahttpheader_checkbox.isChecked():
            extrahttpheader=[str(self.extrahttpheader_textbox.text())]
            extrahttpheaderflag=1
        if self.extrahttpheaderfile_checkbox.isChecked():
            filename=str(self.extrahttpheaderfile_textbox.text())
            try:
                h1=minidom.parse(filename)
                allheader=h1.getElementsByTagName("header")
                ah=[]
                for i in allheader:
                    ah.append(i.firstChild.wholeText.encode('ascii','ignore').strip())
                extrahttpheader=ah
                extrahttpheaderflag=1
            except IOError as e:
                error=1
                QtGui.QMessageBox.warning(self,"Error",str(e))       
            except:
                error=1
                QtGui.QMessageBox.warning(self,"Error",str(e))
        
        if self.default_fakeheader_checkBox.isChecked():
            tempheader=['Accept: image/gif, image/x-bitmap, image/jpeg, image/pjpeg', 'Connection: Keep-Alive', 'Content-type: application/x-www-form-urlencoded; charset=UTF-8']
            extrahttpheader+=tempheader
            extrahttpheaderflag=1
        #####
        ##### EXTRA PAYLOAD VECTORS #####
        
        if self.extrapayloadvector_checkbox.isChecked():
            extrapayload=[str(self.extrapayloadvector_textbox.text())]
            extrapayloadflag=1
        if self.extrapayloadvectorfile_checkbox.isChecked():
            finame=str(self.extrapayloadvectorfile_textbox.text())
            try:
                f1=minidom.parse(finame)
                f2=f1.getElementsByTagName("vector")
                
                for i in f2:
                    temppayload=i.firstChild.wholeText.encode('ascii','ignore').strip()
                    extrapayload.append(temppayload)
                    extrapayloadflag=1      
            except IOError as e:
                error=1
                QtGui.QMessageBox.warning(self, "Error",str(e))
            except:
                error=1
                QtGui.QMessageBox.warning(self,"Error",str("Unexpected Error"))
        
            ###########
            ########### OTHER OPTION VALUES ###########
        
        if self.cookie_checkbox.isChecked():
            cookie=str(self.cookie_textbox.text())
            cookie=cookie.strip()
            cookieflag=1
        if self.referer_checkbox.isChecked():
            referer=str(self.referer_textbox.text())
            referer=referer.strip()
            refererflag=1
        if self.timeout_checkbox.isChecked():
            try:                
                timeout=int(self.timeout_textbox.text())
                timeoutflag=1
            except:
                error=1
                QtGui.QMessageBox.warning(self, "Error:",str("Please enter valid Timeout"))
        
        if self.URLencoding_checkbox.isChecked():
                URLSHORTAPIFLAG=1
                URLSHORTAPI=self.URLencoding_comboBox.currentText()
        
            ###################
        
        if error==0:
            if urlu!="":
                xss_show_result=Displayresult(self) 
                xss_show_result.setvalue(urlu,get,getflag,post,postflag,xmloutput,xmlfilename,fuzzvectorflag,fuzzvectors,verbose,full_reportflag,author_name,author_email,extrahttpheaderflag,extrahttpheader,extrapayloadflag,extrapayload,cookieflag,cookie,refererflag,referer,timeoutflag,timeout,URLSHORTAPIFLAG,URLSHORTAPI,Magent,Mpath)
                xss_show_result.closed.connect(self.start_button.show)
                xss_show_result.show()
                self.start_button.hide()
    
    @QtCore.pyqtSignature("")
    def on_actionAbout_triggered(self):
        ab=About()
        ab.exec_()
        
    @QtCore.pyqtSignature("")
    def on_actionUpdate_triggered(self):
        ud=UpdateData()
        ud.exec_()
        
        
    @QtCore.pyqtSignature("")
    def on_actionNew_triggered(self):
        self.url_textbox.setText("")
        self.poststring_textbox.setText("")
        self.poststring_checkbox.setChecked(False)
        self.getstring_checkbox.setChecked(False)
        self.getstring_textbox.setText("")
        self.xml_checkbox.setChecked(False)
        self.xml_textbox.setText("")
        self.DCP_checkBox.setChecked(False)
        self.verbose_checkbox.setChecked(False)
        self.full_report.setChecked(False)
        self.extrahttpheader_checkbox.setChecked(False)
        self.extrahttpheader_textbox.setText("")
        self.extrahttpheaderfile_checkbox.setChecked(False)
        self.extrahttpheaderfile_textbox.setText("")
        self.default_fakeheader_checkBox.setChecked(False)
        self.extrapayloadvector_checkbox.setChecked(False)
        self.extrapayloadvector_textbox.setText("")
        self.extrapayloadvectorfile_checkbox.setChecked(False)
        self.extrapayloadvectorfile_textbox.setText("")
        self.cookie_checkbox.setChecked(False)
        self.cookie_textbox.setText("")
        self.referer_checkbox.setChecked(False)
        self.referer_textbox.setText("")
        self.timeout_checkbox.setChecked(False)
        self.timeout_textbox.setText("")        
        self.URLencoding_checkbox.setChecked(False)
        self.show_fuzz.setChecked(False)
        
__version__="1.0"

class UpdateData(QtGui.QDialog,Ui_Update_Dialog):
    
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        
        self.setupUi(self)
        
        self.updatevectors.hide()
        self.complete_bar.hide()
        self.initial_progressBar.hide()
        self.updateButton.hide()                
        absp= os.path.abspath(__file__)
        dirp= os.path.dirname(absp)
        
        self.crawlurl = ["http://xssalert.arjunjain.info/vector/basicvector.xml","http://xssalert.arjunjain.info/vector/charencodevector.xml","http://xssalert.arjunjain.info/vector/dcpvector.xml","http://xssalert.arjunjain.info/vector/embeddedcharencodevector.xml","http://xssalert.arjunjain.info/vector/embeddedeventvector.xml","http://xssalert.arjunjain.info/vector/eventvector.xml","http://xssalert.arjunjain.info/vector/regularHTMLvector.xml","http://xssalert.arjunjain.info/vector/urlobfussionvector.xml"]
        self.filepath = [dirp+"/fuzzvector/basicvector.xml",dirp+"/fuzzvector/charencodevector.xml",dirp+"/fuzzvector/dcpvector.xml",dirp+"/fuzzvector/embeddedcharencodevector.xml",dirp+"/fuzzvector/embeddedeventvector.xml",dirp+"/fuzzvector/eventvector.xml",dirp+"/fuzzvector/regularHTMLvector.xml",dirp+"/fuzzvector/urlobfussionvector.xml"]
        
        self.urldata=[]
        self.urldatahash=[]
        self.filedatahash=[]
        self.redata=[]
        
        self.connect(self.checkButton,QtCore.SIGNAL('pressed()'),self.ShowUpdate)
        self.connect(self.updateButton,QtCore.SIGNAL('pressed()'),self.update)
    
    
    def ShowUpdate(self):
        
        self.initial_progressBar.show()
        self.initial_progressBar.setValue(0)
        self.checkButton.setEnabled(False)
        flagupdate=0
        try:
            for i in self.filepath:
                f=open(i,'r')
                self.filedatahash.append(hashlib.md5(f.read()).hexdigest())
                f.close()
            self.initial_progressBar.setValue(25)
            
            self.updatevectors.show()
            
            for i in range(len(self.crawlurl)):
                response =urllib2.urlopen(self.crawlurl[i])
                resdata=response.read()
                self.urldata.append(resdata)
                self.urldatahash.append(hashlib.md5(resdata).hexdigest())
        
            self.initial_progressBar.setValue(50)
            
            for i in range(len(self.filedatahash)):
                if self.filedatahash[i] == self.urldatahash[i]:
                    self.redata.append(1)
                else:
                    self.redata.append(0)
            
            self.initial_progressBar.setValue(75)
            
            
            for i in range(len(self.filedatahash)):
                if not self.redata[i]:
                    flagupdate=1
                    self.updatevectors.append(self.filepath[i])
            self.updateButton.show()
            self.checkButton.hide()
            
            if not flagupdate:
                self.updatevectors.setText("Software already updated")
                self.updateButton.hide()
                self.cancelButton.setText("Close")
            self.initial_progressBar.setValue(100)
        except:
            self.updatevectors.setText("Connection Error")
    
    def update(self):
        self.initial_progressBar.hide()
        self.complete_bar.show()
        val=100/len(self.filedatahash)
        k=0
        self.complete_bar.setValue(0)
        for i in range(len(self.filedatahash)):
            if not self.redata[i]:
                f=open(self.filepath[i],'w')
                f.write(self.urldata[i])
                k=k+val
                self.complete_bar.setValue(k)
                f.close()
        self.updatevectors.setText("Software Updated")
        self.complete_bar.setValue(100)
        
        self.updateButton.setEnabled(False)
        self.cancelButton.setText("Close")
        
class About(QtGui.QDialog,Ui_XSSAlert_about):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        
class Preferences(QtGui.QDialog,Ui_Preferences):
    
    def __init__(self,parent=None):
        
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        
        global Mpath,Magent,FILEPATH
        if not os.path.isfile(FILEPATH):
            f1=open(FILEPATH,"w")
            Magent="Googlebot/2.1 (+http://www.google.com/bot.html)"
            Mpath=str(QtCore.QDir.homePath())
            f1.write(Magent+"\n")
            f1.write(Mpath)
            f1.close()
        else:
            f1=open(FILEPATH,"r")
            rd=f1.read()
            rd=rd.split("\n")
            Magent=rd[0]
            Mpath=rd[1]
            f1.close()
        self.UserAgentText.setText(Magent)
        self.default_file_path.setText(Mpath)
        self.connect(self.SaveButton,QtCore.SIGNAL('pressed()'),self.Savepreferences)
        self.connect(self.ResetButton,QtCore.SIGNAL('pressed()'),self.Reset)
        self.connect(self.change_proxy,QtCore.SIGNAL('pressed()'),self.ChangeProxy)
        self.connect(self.change_path_pushButton,QtCore.SIGNAL('pressed()'),self.setPath)
    
    def setPath(self):
        dirname=str(QtGui.QFileDialog.getExistingDirectory(self,self.tr('XSSAlert - Select Path'),Mpath))
        if dirname:
            self.default_file_path.setText(dirname)
    
    def ChangeProxy(self):
        os.system("gnome-network-properties &")
    
    def Savepreferences(self):    
        global Mpath,Magent,FILEPATH
        f1=open(FILEPATH,"w")
        Mpath=str(self.default_file_path.text())
        Magent=str(self.UserAgentText.text())
        f1.write(Magent+"\n")
        f1.write(Mpath)
        f1.close()
    
    def Reset(self):
        global Mpath,Magent,FILEPATH
        Magent="Googlebot/2.1 (+http://www.google.com/bot.html)"
        Mpath=str(QtCore.QDir.homePath())
        self.UserAgentText.setText(Magent)
        self.default_file_path.setText(Mpath)
        
def run():
    """
    commands= ["pyuic4 -o uipy/ui_mainwindow.py ui/main.ui","pyuic4 -o uipy/ui_resultdisplay.py ui/result_display.ui","pyuic4 -o uipy/ui_preferences.py ui/preferences.ui","pyuic4 -o uipy/ui_update.py ui/update.ui","pyuic4 -o uipy/ui_about.py ui/about.ui","pyrcc4 -o uipy/xss_rc.py ui/xss.qrc"]
    for command in commands:
        os.system(command)
    """
    app=QtGui.QApplication(sys.argv)
    app.setApplicationName("XSSAlert")
    window1=MainWindow()
    window1.show()
    sys.exit(app.exec_())    
