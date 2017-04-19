#coding:utf-8
import Tkinter
import tkMessageBox
import tkFont
from Tkinter import *
from tkSimpleDialog import *
from tkFileDialog  import *
from tkMessageBox import *

#quit button
class Quitter(Frame):            
  def __init__(self, parent=None):     
    Frame.__init__(self, parent)
    self.pack()
    widget = Button(self, text='Quit', command=self.quit,activebackground="HotPink")
    widget.pack(expand=YES, fill=BOTH, side=LEFT)
  def quit(self):
    ans = askokcancel('confirm', "Really quit?")
    if ans: Frame.quit(self)

#scroll
class ScrolledText(Frame):
  def __init__(self, parent=None, text='', file=None):
    Frame.__init__(self, parent)
    self.pack(expand=YES, fill=BOTH)        
    self.makewidgets()
    self.settext(text, file)
  def makewidgets(self):
    sbar = Scrollbar(self)
    text = Text(self, relief=SUNKEN)
    sbar.config(command=text.yview)         
    text.config(yscrollcommand=sbar.set)      
    sbar.pack(side=RIGHT, fill=Y)          
    text.pack(side=LEFT, expand=YES, fill=BOTH)   
    self.text = text
  def settext(self, text='', file=None):
    if file: 
      text = open(file, 'r').read()
    self.text.delete('1.0', END)          
    self.text.insert('1.0', text)         
    self.text.mark_set(INSERT, '1.0')       
    self.text.focus()                
  def gettext(self):                
    return self.text.get('1.0', END+'-1c')
#top bar   
class SimpleEditor(ScrolledText):            
  def __init__(self, parent=None, file=None): 
#menu bar
    menu_frame = Tkinter.Frame(parent,bd =5,bg="LightBlue",highlightcolor="Pink")
    menu_frame.pack(fill=X, side=TOP,padx=5)
    menu_frame.tk_menuBar(self.file_menu(menu_frame), self.action_menu(menu_frame), self.help_menu(menu_frame),Quitter(menu_frame).pack(side=RIGHT,padx=20,pady=1))

    frm = Frame(parent)
    frm.pack(fill=X)
    # frm_x = Frame(frm)
    # frm_x.pack(side=LEFT)
    # Button(frm_x, text='Open', command=self.onOpen).pack(side=LEFT,expand=100)
    # Button(frm_x, text='Save', command=self.onSave).pack(side=LEFT)
    # Button(frm_x, text='Save As', command=self.onSaveAS).pack(side=LEFT)
    # udl=Text(frm)
    # udl.insert(INSERT,"00000000000")
    # udl.tag_add("start", "1.0", "1.20")
    # udl.tag_config("start", background="yellow", foreground="blue")
    # udl.pack()
    # Label(frm,text="                                                                                  ",
    # 	background="Grey",font="Red",height=1).pack()
    frm_x2 = Frame(frm)
    frm_x2.pack(side=RIGHT)
    Button(frm_x2, text='Cut',  command=self.onCut).pack(side=LEFT)
    Button(frm_x2, text='Paste', command=self.onPaste).pack(side=LEFT)
    search=Text(frm_x2,height=1)
    search.insert(INSERT,"search for ... ")
    search.tag_add("start","1.0","1.14")
    search.tag_config("start",background="Beige",foreground="LightBlue")
    search.pack(side=LEFT)
    Button(frm_x2, text='Find', command=self.onFind).pack(side=LEFT)
    
    ScrolledText.__init__(self, parent, file=file) 
    self.text.config(font=('courier', 16, 'normal'))
#menu button
  def help_menu(self,parent):
    help_btn = Tkinter.Menubutton(parent, text='Help', underline=10)
    help_btn.pack(side=LEFT, padx="1")
    help_btn.menu = Tkinter.Menu(help_btn)
    help_btn.menu.add_command(label="How To", underline=0, command=self.HowTo)
    help_btn.menu.add_command(label="About", underline=0, command=self.About)
    help_btn['menu'] = help_btn.menu
    return help_btn

  def file_menu(self ,parent):
    file_btn = Tkinter.Menubutton(parent, text='File', underline=100)
    file_btn.pack(side=LEFT, padx="1")
    file_btn.menu = Tkinter.Menu(file_btn)
    file_btn.menu.add_command(label="open", underline=0, command=self.onOpen)
    file_btn.menu.add_command(label="new project", underline=0, command=self.About)
    file_btn.menu.add_command(label="new file", underline=0, command=self.HowTo)
    file_btn.menu.add_command(label="save", underline=0, command=self.onSave)
    file_btn.menu.add_command(label="save as", underline=0, command=self.onSaveAS)
    file_btn['menu'] = file_btn.menu
    return file_btn

  def action_menu(self,parent):
    action_btn = Tkinter.Menubutton(parent, text='Help', underline=10)
    action_btn.pack(side=LEFT, padx="1")
    action_btn.menu = Tkinter.Menu(action_btn)
    action_btn.menu.add_command(label="How To", underline=0, command=self.HowTo)
    action_btn.menu.add_command(label="About", underline=0, command=self.About)
    action_btn['menu'] = action_btn.menu
    return action_btn

  def HowTo(self):
    tkMessageBox.showinfo("REMINDER","not finish")

  def About(self):
    tkMessageBox.showinfo("About", "________________________________\n"\
                                   "A simple python editor      \n"\
                                   "Author :\tbob                      \n"\
                                   "Email :583532940@qq.com\n"\
                                   "Gtihub :\tbob-young           \n"\
                                   "Version :1.1\n"\
                                   "________________________________")


  def onOpen(self):
    open_path = askopenfilename()
    if open_path:
	  print open_path
    SimpleEditor(file=open_path)

  def onSave(self):
    print 'save'
    open(self.file, 'w').write(alltext)

  def onSaveAS(self):
    filename = asksaveasfilename()
    if filename:
      alltext = self.gettext()           
      open(filename, 'w').write(alltext)
   
  def onCut(self):
    text = self.text.get(SEL_FIRST, SEL_LAST)    
    self.text.delete(SEL_FIRST, SEL_LAST)      
    self.clipboard_clear()       
    self.clipboard_append(text)

  def onPaste(self):                  
    try:
      text = self.selection_get(selection='CLIPBOARD')
      self.text.insert(INSERT, text)
    except TclError:
      pass                  

  def onFind(self):
    target = askstring('SimpleEditor', 'Search String?')
    if target:
      where = self.text.search(target, INSERT, END) 
      if where:                  
        print where
        pastit = where + ('+%dc' % len(target))  
        #self.text.tag_remove(SEL, '1.0', END)   
        self.text.tag_add(SEL, where, pastit)   
        self.text.mark_set(INSERT, pastit)     
        self.text.see(INSERT)          
        self.text.focus()

  
if __name__ == '__main__':
  try:
    SimpleEditor(file=sys.argv[1]).mainloop()  
  except IndexError:
    SimpleEditor().mainloop()
