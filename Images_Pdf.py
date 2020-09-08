from tkinter import *
import tkinter.filedialog
from PIL import ImageTk
from PIL import *

from pathlib import Path
import tkinter.messagebox
from fpdf import FPDF
import os
from os import listdir
from os.path import isfile, join 
#from pgmagick import Image
import img2pdf



class pdfconverter:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x300")
        self.root.title("Images 2 PDF CONVERTER")
        self.root.resizable(0,0)
        self.root.iconbitmap("index.ico")

        paths=StringVar()


#============================================================================================


        def on_enter1(e):
            But_open['background']="black"
            But_open['foreground']="cyan"
               
               

        def on_leave1(e):
            But_open['background']="SystemButtonFace"
            But_open['foreground']="SystemButtonText"



        def on_enter2(e):
            But_ctp['background']="black"
            But_ctp['foreground']="cyan"
               
               

        def on_leave2(e):
            But_ctp['background']="SystemButtonFace"
            But_ctp['foreground']="SystemButtonText"


        def open_dir():
            paths.set("")
            fold=tkinter.filedialog.askdirectory(title="choose folder")
            paths.set(fold)
            self.root.update()
            Lab.config(text="file is selected")



        def extract():
            path=paths.get()
            if path==" ":
                tkinter.messagebox.askretrycancel("error","please add url")
            else:
                try:
                    #for each_file in listdir(path):
                        #if isfile(join(mypath,each_file)):
                        #    image_path = os.path.join(mypath,each_file)
                        #    pdf_path =  os.path.join(mypath,each_file.rsplit('.', 1)[0]+'.pdf')
                        #    img = Image(image_path)
                        #    img.write(pdf_path)




                    dirname = path
                    
                    
                    #files=tkinter.filedialog.asksaveasfile(filetypes = [('PDF', '*.pdf')],defaultextension=[("PDF","*.pdf")])
                    
                    
                    
            
                    with open("hello.pdf","wb") as f:
                        try:
                            imgs = []
                            for fname in os.listdir(dirname):
                                if not fname.endswith(".png"):
                                    continue
                                path = os.path.join(dirname, fname)
                                if os.path.isdir(path):
                                    continue
                                imgs.append(path)
                            f.write(img2pdf.convert(imgs))
                        except:
                            tkinter.messagebox.askretrycancel("info","The excentention is not png")


                        try:
                            imgs = []
                            for fname in os.listdir(dirname):
                                if not fname.endswith(".jpg"):
                                    continue
                                path = os.path.join(dirname, fname)
                                if os.path.isdir(path):
                                    continue
                                imgs.append(path)
                            f.write(img2pdf.convert(imgs))
                        except:
                            tkinter.messagebox.askretrycancel("info","The excentention is not jpg")


                        try:
                            imgs = []
                            for fname in os.listdir(dirname):
                                if not fname.endswith(".jpeg"):
                                    continue
                                path = os.path.join(dirname, fname)
                                if os.path.isdir(path):
                                    continue
                                imgs.append(path)
                            f.write(img2pdf.convert(imgs))
                        except:
                            tkinter.messagebox.askretrycancel("info","The excentention is no jpeg")

                        


                    
                    #entries=Path(path)
                    #names=[ ]
   
                    #for entry in entries.iterdir():
          
                    #  names.append(entry.glob())
                    #imageslist=names
                    #print(imageslist)

                    #with open("name.pdf","wb") as f:
	                #    f.write(img2pdf.convert(imageslist))
     
                    #imagelist= '[%s]' % ', '.join(map(str, names))
                    #print(entry.names)
                    
                    #pdf = FPDF()
                    # imagelist is the list with all image filenames
                    #for image in imagelist:
                    #    pdf.add_page()
                    #    pdf.image(image) #x,y,w,h
                    #pdf.output("yourfile.pdf", "F")

                except Exception as e:
                    #tkinter.messagebox.askretrycancel("error","internal error")
                    print(e)







#===========================================


        


        Mainframe=Frame(self.root,width=500,height=300,relief="sunken",bd=3,bg="gray")
        Mainframe.place(x=0,y=0)



        self.original1 = Image.open ("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\imgtopdf\\hqd.jpg")
        resized1 = self.original1.resize((495, 300),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(resized1)
        bglab1=Label(Mainframe,image=self.image1,bd=1).place(x=0,y=0)


        Lab=Label(Mainframe,text="Select the file",font=("times new roman",12,"bold"),bg="black",fg="cyan")
        Lab.place(x=200,y=20)

        Ent=Entry(Mainframe,textvariable=paths,width=50,font=("times new roman",13,"bold"),bd=3)
        Ent.place(x=20,y=70)



        But_open=Button(Mainframe,text="Open file",command=open_dir,width=15,font=("times new roman",12,"bold"),bd=3,cursor="hand2")
        But_open.place(x=50,y=210)
        But_open.bind("<Enter>",on_enter1)
        But_open.bind("<Leave>",on_leave1)


        But_ctp=Button(Mainframe,text="Convert to pdf",command=extract,width=15,font=("times new roman",12,"bold"),bd=3,cursor="hand2")
        But_ctp.place(x=300,y=210)
        But_ctp.bind("<Enter>",on_enter2)
        But_ctp.bind("<Leave>",on_leave2)



if __name__ == "__main__":
    root=Tk()
    app=pdfconverter(root)
    root.mainloop()
