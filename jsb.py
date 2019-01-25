import tkinter as tk
from tkinter import ttk,filedialog,messagebox
import os
FONTSURL=r'C:\Windows\Fonts'
def getfonts():
    result=[]
    fonts=os.listdir(FONTSURL)
    for item in fonts:
        if item.endswith(".ttf"):
            font=item[0:-4]
            result.append(font)
    return result
FONTLIST=getfonts()
FONTSTYLE=['常规','粗体','倾斜常规','倾斜粗体']
FONTSIZE=['8','9','10','11','12','14','16','18','20','22','24','26','28','36','48','72']

class Mydialog(tk.Toplevel):
    '''
    自定义字体窗口
    '''
    def __init__(self,mainwin):
        super().__init__()
        self.createface()
        self.title("字体")
        self.resizable(0,0)
        self.mainwin=mainwin
    def setfont(self):
        font_family=self.e1.get()
        font_style=self.e2.get()
        font_size=self.e3.get()
        if font_style=="粗体":
            font_style='bold'
        elif font_style=="常规":
            font_style='normal'
        elif font_style=="倾斜粗体":
            font_style='bold italic'
        elif font_style=="倾斜常规":
            font_style='normal italic'
        else:
            font_style='' 
        self.mainwin.t.config({
            "font":(font_family,font_size,font_style)  
            })
    def createface(self):
        v1=tk.StringVar()
        v1.set("微软雅黑")
        v2=tk.StringVar()
        v2.set("常规")
        v3=tk.StringVar()
        v3.set("8")

        #标题
        l1=tk.Label(self,text="字体")
        l1.grid(row=0,column=0,padx=10,pady=10)
        l2=tk.Label(self,text="字形",width=15)
        l2.grid(row=0,column=1,padx=10,pady=10)
        l3=tk.Label(self,text="大小",width=5)
        l3.grid(row=0,column=2,padx=10,pady=10)
        #输入框
        e1=tk.Entry(self,width=23,textvariable=v1)
        e1.grid(row=1,column=0,padx=10,pady=5)
        e2=tk.Entry(self,width=17,textvariable=v2)
        e2.grid(row=1,column=1,padx=10,pady=5)
        e3=tk.Entry(self,width=7,textvariable=v3)
        e3.grid(row=1,column=2,padx=10,pady=5)

        f1=tk.Frame(self)
        f1.grid(row=2,column=0,padx=10,pady=10)
        f2=tk.Frame(self,width=15)
        f2.grid(row=2,column=1,padx=10,pady=10)
        f3=tk.Frame(self,width=5)
        f3.grid(row=2,column=2,padx=10,pady=10)
        #列表
        def lx1c(e):
            index=e.widget.curselection()[0]
            val=e.widget.get(index)
            e1.delete(0,'end')
            e1.insert(tk.END,val)
            ztchange()
        def lx2c(e):
            index=e.widget.curselection()[0]
            val=e.widget.get(index)
            e2.delete(0,'end')
            e2.insert(tk.END,val)
            ztchange()
        def lx3c(e):
            index=e.widget.curselection()[0]
            val=e.widget.get(index)
            e3.delete(0,'end')
            e3.insert(tk.END,val)
            ztchange()
        def ztchange():
            font_family=self.e1.get()
            font_style=self.e2.get()
            font_size=self.e3.get()
            if font_style=="粗体":
                font_style='bold'
            elif font_style=="常规":
                font_style='normal'
            elif font_style=="倾斜粗体":
                font_style='bold italic'
            elif font_style=="倾斜常规":
                font_style='normal italic'
            else:
                font_style=''
            zt['font']=(font_family,font_size,font_style)
        lx1=tk.Listbox(f1)
        lx1.bind('<ButtonRelease-1>',lx1c)
        for item in getfonts():
            lx1.insert(tk.END,item)
        lx2=tk.Listbox(f2,width=15)
        lx2.bind('<ButtonRelease-1>',lx2c)
        for item in FONTSTYLE:
            lx2.insert(tk.END,item)
        lx3=tk.Listbox(f3,width=5)
        lx3.bind('<ButtonRelease-1>',lx3c)
        for item in FONTSIZE:
            lx3.insert(tk.END,item)
        
        self.e1=e1
        self.e2=e2
        self.e3=e3
        #列表滚动条
        s1=tk.Scrollbar(f1,command=lx1.yview)
        s2=tk.Scrollbar(f2,command=lx2.yview)
        s3=tk.Scrollbar(f3,command=lx3.yview)
        
        lx1.config({
            'yscrollcommand':s1.set
        })
        lx2.config({
            'yscrollcommand':s2.set
        })
        lx3.config({
            'yscrollcommand':s3.set
        })

        lx1.pack(side=tk.LEFT)
        s1.pack(side=tk.RIGHT,fill=tk.Y)
        lx2.pack(side=tk.LEFT)
        s2.pack(side=tk.RIGHT,fill=tk.Y)
        lx3.pack(side=tk.LEFT)
        s3.pack(side=tk.RIGHT,fill=tk.Y)
        #字体展示
        fzt=tk.Frame(self,width=200,height=70,bg="#fff")
        fzt.propagate(0)
        fzt.grid(row=4,column=1,columnspan=2,pady=20)
        zt=tk.Label(fzt,text="AaBbYyZz",bg="#fff",font = ("",20,"bold italic"))
        zt.pack(expand=1)
        #脚本下拉列表
        ls = tk.Label(self,text="脚本")
        ls.grid(row=5,column=1,pady=5)
        s1 = ttk.Combobox(self,state='readonly')
        s1['values']=("中文 GB2312","西欧语言","土耳其语","中欧字符","西里尔语")
        s1.current(0)
        s1.grid(row=6,column=1,columnspan=2)
        #按钮
        def ziti_y():
            self.setfont()
            self.destroy()
        def ziti_n():
            self.destroy()
        b1 = tk.Button(self,text="确定",command=ziti_y,width=12)
        b1.grid(row=7,column=1,pady=20)
        b2 = tk.Button(self,text="取消",command=ziti_n,width=12)
        b2.grid(row=7,column=2,padx=10,pady=20)    

class Myyemian(tk.Toplevel):
    '''
    自定页面窗口
    '''
    def __init__(self):
        super().__init__()
        self.createface()
        self.title("页面设置")
        self.resizable(0,0)
    def createface(self):
        f0=tk.Frame(self,width=100,height=100)
        f0.pack()
        f1=tk.Frame(f0,width=100,height=100)
        f2=tk.Frame(f0,width=100,height=100)
        f1.pack(side=tk.LEFT,padx=10,pady=10)
        f2.pack(side=tk.RIGHT)
        
        #纸张
        lf1 = tk.LabelFrame(f1,height=6,text="纸张")
        lf1.pack()
        ls1 = tk.Label(lf1,text="大小")
        ls1.grid(row=0,column=1,padx=5,pady=5)
        s1 = ttk.Combobox(lf1,state='readonly',width=27)
        s1['values']=("A3","A4","A5","B4","B5","信纸")
        s1.current(1)
        s1.grid(row=0,column=2,padx=5,pady=5)
        ls2 = tk.Label(lf1,text="来源")
        ls2.grid(row=1,column=1,padx=5,pady=5)
        s2 = ttk.Combobox(lf1,state='readonly',width=27)
        s2['values']=("无")
        s2.current(0)
        s2.grid(row=1,column=2,padx=5,pady=5)

        #方向
        f3=tk.Frame(f1)
        f3.pack()
        lf2 = tk.LabelFrame(f3,height=6,text="方向")
        lf2.pack(side=tk.LEFT)
        zz1 = tk.Variable()
        zz1.set("纵向")
        r1 = tk.Radiobutton(lf2,text="纵向",variable=zz1,value="纵向") 
        r2 = tk.Radiobutton(lf2,text="横向",variable=zz1,value="横向")
        r1.pack(padx=7,pady=3)
        r2.pack(padx=7,pady=3)

        #页边距
        lf3 = tk.LabelFrame(f3,height=6,text="页边距(毫米)")
        lf3.pack(side=tk.RIGHT)
        lb1=tk.Label(lf3,text="左(L):")
        lb1.grid(row=0,column=0,padx=5,pady=5)
        e1=tk.Entry(lf3,width=5)
        e1.grid(row=0,column=1,padx=5,pady=5)
        lb2=tk.Label(lf3,text="右(R):")
        lb2.grid(row=0,column=2,padx=5,pady=5)
        e2=tk.Entry(lf3,width=5)
        e2.grid(row=0,column=3,padx=5,pady=5)
        lb3=tk.Label(lf3,text="上(T):")
        lb3.grid(row=1,column=0,padx=5,pady=5)
        e3=tk.Entry(lf3,width=5)
        e3.grid(row=1,column=1,padx=5,pady=5)
        lb4=tk.Label(lf3,text="下(B):")
        lb4.grid(row=1,column=2,padx=5,pady=5)
        e4=tk.Entry(lf3,width=5)
        e4.grid(row=1,column=3,padx=5,pady=5)

        #页眉页脚
        f4=tk.Frame(f1)
        f4.pack()
        lb5=tk.Label(f4,text="页眉(H)")
        lb5.grid(row=0,column=0,padx=5,pady=5)
        e5=tk.Entry(f4,width=27)
        e5.grid(row=0,column=1,padx=5,pady=5)
        lb6=tk.Label(f4,text="页脚(F)")
        lb6.grid(row=1,column=0,padx=5,pady=5)
        e6=tk.Entry(f4,width=27)
        e6.grid(row=1,column=1,padx=5,pady=5)

        #预览
        lfr = tk.LabelFrame(f2,text="预览",width=150,height=250)
        lfr.propagate(0)
        lfr.pack()

        #按钮
        lbs=tk.Frame(self,height=50)
        lbs.propagate(0)
        lbs.pack(fill=tk.X)
        def yemian_y():
            self.destroy()
        def yemian_n():
            self.destroy()
        b1 = tk.Button(lbs,text="确定",command=yemian_y,width=12)
        b1.pack(side=tk.RIGHT,padx=10,pady=10)
        b2 = tk.Button(lbs,text="取消",command=yemian_n,width=12)
        b2.pack(side=tk.RIGHT,padx=10,pady=10)

class Mystamp(tk.Toplevel):
    '''
    自定义打印窗口
    '''
    def __init__(self):
        super().__init__()
        self.createface()
        self['bg']='#fff'
        self.title("打印")
        self.resizable(0,0)
    def createface(self):
        f1 = tk.Frame(self,bg="#ccc")
        f1.grid(row=0,column=0,columnspan=2,sticky='e'+'w')
        l1 = tk.Label(f1,bg="#fff",text='常规')
        l1.pack(side=tk.LEFT)

        lf = tk.LabelFrame(self,bg="#fff",text='选择打印机')
        lf.grid(row=1,column=0,columnspan=2,sticky='e'+'w',padx=10,ipadx=10)

        arr1 = ['添加打印机','Fax','Microsoft Print to PDF','Microsoft XPS Document Writer']
        lx1 = tk.Listbox(lf,width=70,height=4)
        for i in arr1:
            lx1.insert('end',i)
        lx1.pack(pady=15)

        f2 = tk.Frame(lf,bg='#fff')
        f2.pack()
        l2 = tk.Label(f2,text='状态：',bg="#fff")
        l2.pack(side=tk.LEFT)
        l3 = tk.Label(f2,text='就绪',bg="#fff")
        l3.pack(side=tk.LEFT)
        l4 = tk.Label(f2,width=25,bg='#fff')
        l4.pack(side=tk.LEFT)

        b1 = tk.Button(f2,text='首选项（R）',padx=10)
        b1.pack(side=tk.RIGHT)
        c1 = tk.Checkbutton(f2,text='打印到文件（F）',bg='#fff')
        c1.pack(side=tk.RIGHT,padx=5)

        f3 = tk.Frame(lf,bg='#fff')
        f3.pack(padx=10,pady=5)
        f4 = tk.Frame(f3,bg='#fff')
        f4.pack(side=tk.LEFT)
        b2 = tk.Button(f3,text='查找打印机（D）...',width=25)
        b2.pack(side=tk.RIGHT)
        f5 = tk.Frame(f4,bg='#fff')
        f5.pack()
        l5 = tk.Label(f5,text='位置：',bg='#fff')
        l5.pack(side=tk.LEFT)
        l6 = tk.Label(f5,width=37,bg='#fff')
        l6.pack(side=tk.LEFT)
        f6 = tk.Frame(f4,bg='#fff')
        f6.pack()
        l7 = tk.Label(f6,text='备注：',bg='#fff')
        l7.pack(side=tk.LEFT)
        l8 = tk.Label(f6,width=40,bg='#fff')
        l8.pack(side=tk.LEFT)

        lf1 = tk.LabelFrame(self,text='页面范围')
        lf1.grid(row=2,column=0,padx=10,pady=10)

        v1 = tk.IntVar()
        v1.set(1)
        f7 = tk.Frame(lf1,bg='#fff')
        f7.pack()
        r1 = tk.Radiobutton(f7,text='全部（L）',variable=v1,value=1,bg='#fff')
        r1.pack(side=tk.LEFT,padx=10)
        l9 = tk.Label(f7,width=18,bg='#fff')
        l9.pack(side=tk.RIGHT,padx=10)

        f8 = tk.Frame(lf1,bg='#fff')
        f8.pack()
        r2 = tk.Radiobutton(f8,text='选定范围（T）',variable=v1,value=2,bg='#fff')
        r2.pack(side=tk.LEFT,padx=10,pady=10)
        r3 = tk.Radiobutton(f8,text='当前页面（U）',variable=v1,value=3,bg='#fff')
        r3.pack(side=tk.RIGHT,padx=10,pady=10)

        f9 = tk.Frame(lf1,bg='#fff')
        f9.pack()
        r3 = tk.Radiobutton(f9,text='页码（G）',variable=v1,value=4,bg='#fff')
        r3.pack(side=tk.LEFT,padx=20,pady=10)
        e1 = tk.Entry(f9,width=15)
        e1.pack(side=tk.RIGHT,padx=10,pady=10)

        f7 = tk.Frame(self,bg='#fff')
        f7.grid(row=2,column=1,padx=10,pady=10)
        f10 = tk.Frame(f7,bg='#fff')
        f10.pack()
        l10 = tk.Label(f10,text='份数（C）：',bg='#fff')
        l10.pack(side=tk.LEFT,pady=10)
        sp1 = tk.Spinbox(f10,bg='#fff')
        sp1.config({
            'from':1,
            'to':1000,
        })
        sp1.pack(side=tk.RIGHT,pady=10)
        f11 = tk.Frame(f7,bg='#fff')
        f11.pack()
        c2 = tk.Checkbutton(f11,text='自动分页（O）',bg='#fff')
        c2.pack(side=tk.LEFT,pady=10)
        l11 = tk.Label(f11,width=15,bg='#fff')
        l11.pack(side=tk.RIGHT,pady=10)
        f12 = tk.Frame(f7,bg='#fff')
        f12.pack()
        l12 = tk.Label(f12,text='',bg='#fff')
        l12.pack(side=tk.TOP,pady=10)

        def dayin_a():
            self.destroy()
        def dayin_n():
            self.destroy()
        def dayin_p():
            pass  
        f13 = tk.Frame(self)
        f13.grid(row=3,column=0,columnspan=2,sticky='e'+'w')
        b3 = tk.Button(f13,text='应用（A）',width=10,command=dayin_a)
        b3.pack(side=tk.RIGHT,padx=5,pady=5)
        b4 = tk.Button(f13,text='取消',width=10,command=dayin_n)
        b4.pack(side=tk.RIGHT,padx=5,pady=5)
        b5 = tk.Button(f13,text='打印（P）',width=10,command=dayin_p)
        b5.pack(side=tk.RIGHT,padx=5,pady=5)

class Myfind(tk.Toplevel):
    '''
    查找窗口
    '''
    def __init__(self):
        super().__init__()
        self.createface()
        self.title("查找")
        self.resizable(0,0)
        self.nindex=0
        self.arr=[]
    def createface(self):    
        f1 = tk.Frame(self,bg="#F0F0F0")
        f1.pack(side=tk.LEFT,padx=10,pady=10)
        
        f3 = tk.Frame(f1,bg="#F0F0F0")
        f3.pack(padx=10)
        l1 = tk.Label(f3,bg="#F0F0F0",text='查找内容:')
        l1.pack(side=tk.LEFT,pady=10) 
        self.e1 = tk.Entry(f3)
        self.e1.pack(side=tk.RIGHT,padx=10,pady=10) 
        
        f4 = tk.Frame(f1,bg="#F0F0F0")
        f4.pack()        
        self.v1 = tk.Variable()
        self.v1.set(0)
        c1 = tk.Checkbutton(f4,text='区分大小写',variable=self.v1,onvalue=1, offvalue=0)
        c1.pack(side=tk.LEFT)
        fl = tk.LabelFrame(f4,text="方向")
        fl.pack(side=tk.RIGHT)
        self.v2 = tk.Variable()
        self.v2.set(1)
        r1 = tk.Radiobutton(fl,text="向上",variable=self.v2,value=0)
        r1.pack(side=tk.LEFT)
        r2 = tk.Radiobutton(fl,text="向下",variable=self.v2,value=1)
        r2.pack(side=tk.RIGHT)

        f2 = tk.Frame(self,bg="#F0F0F0")
        f2.pack(side=tk.RIGHT,padx=10,pady=10)                

        b1 = tk.Button(f2,text="查找下一个",width=10,command=self.fn1)
        b1.pack(pady=10)
        
        b2 = tk.Button(f2,text="取消",width=10,command=self.fn2)
        b2.pack(pady=10)
    
    def fn1(self):
        d=self.v2.get()
        node=window.t.get(0.0,tk.END)
        str1=self.e1.get()
        if d==1:
            if str1!="":
                index=node.find(str1,self.nindex,len(node))
                if index!=-1:
                    self.arr.append(index)
                    sindex=str(index)
                    messagebox.showinfo(title="查找结果",message=str1+"位置在"+sindex)
                elif index==-1 or self.nindex>len(node):
                    messagebox.showwarning(message="找不到"+str1)
                self.nindex=index+len(str1)
        elif d==0:
            if str1!="":
                index=node.rfind(str1,0,self.nindex)
                if index!=-1:
                    self.arr.append(index)
                    sindex=str(index)
                    messagebox.showinfo(title="查找结果",message=str1+"位置在"+sindex)
                elif index==-1 or self.nindex<0:
                    messagebox.showwarning(message="找不到"+str1)
                self.nindex=index-1       
        print(self.arr)       
    def fn2(self):
        self.nindex=0
        self.arr=[]
        self.destroy()

class Mychange(tk.Toplevel):
    '''
    替换窗口
    '''
    def __init__(self):
        super().__init__()
        self.createface()
        self.title("查找")
        self.resizable(0,0)
        self.nindex=0
        self.arr=[]
    def createface(self): 
        l1=tk.Label(self,bg="#F0F0F0",text='查找内容:',anchor="w",width=8)
        l1.grid(row=0,column=0,padx=5,pady=5)
        self.e1=tk.Entry(self)
        self.e1.grid(row=0,column=1,padx=5,pady=5)
        l2=tk.Label(self,bg="#F0F0F0",text='替换为:',anchor="w",width=8)
        l2.grid(row=1,column=0,padx=5,pady=5)
        self.e2=tk.Entry(self)
        self.e2.grid(row=1,column=1,padx=5,pady=5)
        b1=tk.Button(self,text="查找下一个",width=9,command=self.fn1)
        b1.grid(row=0,column=2,padx=5,pady=5)
        b2=tk.Button(self,text="替换",width=9,command=self.fn3)
        b2.grid(row=1,column=2,padx=5,pady=5)
        b3=tk.Button(self,text="全部替换",width=9,command=self.fn4)
        b3.grid(row=2,column=2,padx=5,pady=5)
        v1 = tk.Variable()
        v1.set(0)
        c1=tk.Checkbutton(self,text="区分大小写",variable=v1)
        c1.grid(row=3,column=0,padx=5,pady=5)
        b4=tk.Button(self,text="取消",width=9,command=self.fn2)
        b4.grid(row=3,column=2,padx=5,pady=5)

    def fn1(self):
        con1=self.e1.get()#被改内容
        node=window.t.get(0.0,tk.END)
            
        if con1!="":
            index=node.find(con1,self.nindex,len(node))
            if index!=-1:
                self.arr.append(index)
            elif index==-1 or self.nindex>len(node):
                messagebox.showwarning(message="找不到"+con1)
            self.nindex=index+len(con1)   
        print(self.arr) 
    def fn3(self):#替换下一个
        con1=self.e1.get()#被改内容
        con2=self.e2.get()#替换内容内容 
        node=list(window.t.get(0.0,tk.END))   
        if self.arr!=[]:
            index=self.nindex-len(con1)
            for i in range(len(con1)):
                del node[index]
            node.insert(index,con2)
            s=''.join(node)
            window.t.delete(0.0,tk.END)
            window.t.insert('end',s)
    def fn4(self):#全部替换
        node=window.t.get(0.0,tk.END)
        con1=self.e1.get()#被改内容
        con2=self.e2.get()#替换内容内容
        node=node.replace(con1,con2)
        window.t.delete(0.0,tk.END)
        window.t.insert('end',node)
    def fn2(self):
        self.nindex=0
        self.arr=[]
        self.destroy()
class Application(tk.Tk):
    '''
    程序逻辑
    '''
    def __init__(self):
        super().__init__()
        self.title("记事本") #设置窗口名
        self.geometry("900x600") #设置窗口尺寸
    def ziti(self):
        mdg=Mydialog(self)
        self.wait_window(mdg)
    def yemian(self):
        mym=Myyemian()
        self.wait_window(mym)
    def dayin(self):
        mdy=Mystamp()
        self.wait_window(mdy) 
    def chazhao(self): 
        mfd=Myfind()
        self.wait_window(mfd) 
    def tihuan(self):
        mth=Mychange()
        self.wait_window(mth)
    def newfile(self):
        val=self.t.get(0.0,tk.END)
        if val:
            boo=messagebox.askyesno(title="",message="是否新建并保存现有内容？")
            if boo:
                filename=filedialog.asksaveasfilename()
                with open(filename,"w") as f:
                    f.write(val)
        self.t.delete(0.0,tk.END)
    def openfile(self):
        boo=messagebox.askyesno(title="",message="是否打开新的文件？")
        if boo:
            self.t.delete(0.0,tk.END)
            filename = filedialog.askopenfilename()
            with open(filename,"r")  as f:
                val=f.read()
            self.t.insert('end',val)
    def lsavefile(self):
        val=self.t.get(0.0,tk.END)
        if val:
            boo=messagebox.askyesno(title="",message="是否保存现有内容？")
            if boo:
                filename=filedialog.asksaveasfilename()
                with open(filename,"w") as f:
                    f.write(val) 
    def savefile(self):
        pass 
    def close(self):
        boo=messagebox.askyesno(title="",message="确定退出吗？")
        if boo:
            self.destroy()
    def fnum(self,e):
        str1=""
        str1+=(window.t.get(0.0,tk.END))
        linenum=str1.count("\n")
        num=len(str1)-linenum
        var1.set(num)

class Face():
    '''
    界面部分
    '''
    def __init__(self,win):
        self.win=win
        self.addmenu()
        self.textarea()
        self.addstate()
        # self.addyoujian()
    def addmenu(self):
        '''
        创建菜单栏
        '''
        window=self.win
        menubar=tk.Menu(window,tearoff=0)
        #文件
        filemenu=tk.Menu(window,tearoff=0)
        filemenu.add_command(label="新建",command=window.newfile)
        filemenu.add_command(label="打开",command=window.openfile)
        filemenu.add_command(label="保存",command=window.lsavefile)
        filemenu.add_command(label="另存为",command=window.lsavefile)
        filemenu.add_separator()
        filemenu.add_command(label="页面设置",command=window.yemian)
        filemenu.add_command(label="打印",command=window.dayin)
        filemenu.add_separator()
        filemenu.add_command(label="退出",command=window.close)
        menubar.add_cascade(label="文件",menu=filemenu)
        
         #编辑
        editsmenu=tk.Menu(window,tearoff=0)
        editsmenu.add_command(label="撤销")
        editsmenu.add_separator()
        editsmenu.add_command(label="剪切")
        editsmenu.add_command(label="复制")
        editsmenu.add_command(label="粘贴")
        editsmenu.add_command(label="删除")
        editsmenu.add_separator()
        editsmenu.add_command(label="查找",command=window.chazhao)
        editsmenu.add_command(label="查找下一个")
        editsmenu.add_command(label="替换",command=window.tihuan)
        editsmenu.add_command(label="转到")
        editsmenu.add_separator()
        editsmenu.add_command(label="全选")
        editsmenu.add_command(label="事件/日期")
        menubar.add_cascade(label="编辑",menu=editsmenu)
        
        #格式
        gsmenu=tk.Menu(window,tearoff=0)
        gsmenu.add_checkbutton(label="自动换行")
        gsmenu.add_command(label="字体",command=window.ziti)
        menubar.add_cascade(label="格式",menu=gsmenu) 
        
        #查看
        listmenu=tk.Menu(window,tearoff=0)
        listmenu.add_command(label="状态栏")
        menubar.add_cascade(label="查看",menu=listmenu)
        #帮助
        helpmenu=tk.Menu(window,tearoff=0)
        helpmenu.add_command(label="查看帮助")
        helpmenu.add_separator()
        helpmenu.add_command(label="关于记事本")
        menubar.add_cascade(label="帮助",menu=helpmenu)
        
        window.configure(menu=menubar)
    def textarea(self):
        window=self.win
        f=tk.Frame(window,bg="#ccc")
        f.pack(fill=tk.BOTH,expand=1)
        
        t=tk.Text(f)
        t.insert(tk.END,"")
        t.pack(fill=tk.BOTH,expand=1,side=tk.LEFT)
     
        t.bind('<KeyRelease>',window.fnum)

        s=tk.Scrollbar(f,command=t.yview)
        s.pack(fill=tk.Y,side=tk.RIGHT)
        
        t.config({
            'yscrollcommand':s.set
        })
        self.win.t=t

    def addstate(self):
        '''
        添加状态栏
        '''
        window=self.win
        f=tk.Frame(window)
        f.pack(fill=tk.X)
        l1=tk.Label(f,text="字数:")
        l1.pack(side=tk.LEFT)
        l2=tk.Label(f,textvariable=var1)
        l2.pack(side=tk.LEFT)
    
    # def addyoujian(self):
    #     '''
    #     添加右键菜单
    #     '''
    #     t=window.t
    #     menubar=tk.Menu(t,tearoff=0)
    #     for item in ['css','html','javascript','python']:
    #         menubar.add_command(label=item)
    #     def click(e):
    #         menubar.post(e.x_root,e.y_root)
    #         window.bind('<Button-3>',click)


if __name__ =="__main__":
    window=Application()
    var1=tk.Variable()
    var1.set(0)
    Face(window)
    window.mainloop()