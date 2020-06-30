from tkinter import *
import os
import create_folder as cf
import open_camera as rc
import cammodi as cm
import trainner as tr
from PIL import Image, ImageTk
import time

# PATH DEFINING:-

PATH="D:\\Project" #PATH FOR YOUR OVERALL PROJECT
logo='D:\\secure.png' #PATH FOR COMPANY LOGO
mainlogo="D:\\main.png" #PATH FOR MAIN SCREEN LOGO
login_img="D:\\login.png" #PATH FOR LOGIN IMAGE
reg_img="D:\\register.png" #PATH FOR REG IMAGE
cross_button="D:\\button.png" #PATH FOR CROSS BUTTON
cam_img="D:\\camera.png" #PATH FOR CAMERA IMAGE
dash_img="D:\\dashboard.png" #PATH FOR DASHBOARD IMAGE
smile="D:\\veri.png" #PATH FOR VERIFIED IMAGE
not_ver="D:\\sad.png" #PATH FOR NOT VERIFIED IMAGE


#tr.trained()
def check_face(obt,accuracy):
	scrcheck=Toplevel(screen1)
	scrcheck.title("Result")
	scrcheck.geometry("300x200")
	scrcheck.configure(bg='#49A')
	scrcheck.iconphoto(False, ImageTk.PhotoImage(file=logo))
	#Label(scrcheck,text=obt).pack()
	#Label(scrcheck,text=obt).pack()

	if( obt==username1):
		Label(scrcheck,text="Username Verified",bg='#49A').place(x=90,y=50)
		image = Image.open(smile)
		image=image.resize((40,40), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(image)
		label = Label(scrcheck,image=photo)
		label.image = photo # keep a reference!
		label.place(x=120,y=80)
		session()
	elif(obt=="no face"):
		Label(scrcheck,text="No face detected",bg='#49A').place(x=100,y=50)
		image = Image.open(not_ver)
		image=image.resize((40,40), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(image)
		label = Label(scrcheck,image=photo)
		label.image = photo # keep a reference!
		label.place(x=130,y=80)
	else:
		Label(scrcheck, text="Username is not correctly verified \n You have to verify again",bg='#49A').pack();
		Label(scrcheck,text="click camera for verify",bg='#49A').pack()
		Label(scrcheck,text=obt,bg='#49A').pack()
		image = Image.open(not_ver)
		image=image.resize((40,40), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(image)
		label = Label(scrcheck,image=photo)
		label.image = photo # keep a reference!
		label.place(x=130,y=80)
		#Button(scrcheck,text="open camera",command=cammodi).pack()





def cammodi():
	usernam_obtain,accuracy=cm.recog()
	check_face(usernam_obtain,accuracy)

def open_camera():
	global username_info1
	start=time.time()
	username_info1=username.get()
	rc.open_camera(PATH+"\\"+username_info1)
	tr.trained()
	Label(screen2, text="Register Succesfully :)", bg="green").place(x=220,y=440)

	
def reg_user():
	username_info=username.get()
	password_info=password.get()
	if(username_info=="" or password_info==""):
		Empty()
	elif(validation(password_info,len(password_info))):
		Label(screen2,text="Invalid", bg="#49A").place(x=370,y=140)
	else:
		existing_user=os.listdir(PATH)
		if username_info in existing_user:
			Label(screen2, text="Username not Available",bg='#49A').place(x=220,y=330)
		#Label(screen2,text=os.getcwd()).pack()
		else:
			cf.create_folder(PATH+"\\"+username_info)
			file=open(PATH+"\\"+username_info+"\\"+username_info,"w")
			file.write(username_info+"\n")
			file.write(password_info)
			file.close()
			image = Image.open(cam_img)
			image=image.resize((30,30), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(image)
			label = Label(screen2,image=photo)
			label.image = photo # keep a reference!
			Label(screen2,text="Username Succesfully Registered", bg='#49A').place(x=200,y=330)
			Label(screen2, text="Click To Open Camera For Complete Registration \n & Wait Untill Complete Reg Done ",bg='#49A').place(x=150,y=360)
			Button(screen2,image=photo, command=open_camera).place(x=260,y=400)


	


def destroy4():
	screen4.destroy()

def destroy5():
	screen5.destroy()

def destroy6():
	screen6.destroy()

def save():
	new_file1=new_file.get()
	notes1=notes.get()
	data=open(PATH+"\\"+username1+"\\"+new_file1,"w")
	data.write(notes1)
	data.close()

	Label(screen8,text="Saved",bg='#49A').place(x=300,y=330)

def view():
	screen10=Toplevel(screen1)
	screen10.title("View")
	screen10.geometry("300x200")
	screen10.configure(bg='#49A')
	screen10.iconphoto(False, ImageTk.PhotoImage(file=logo))
	openfile1=openfile.get()
	data1=open(PATH+"\\"+username1+"\\"+openfile1,"r")
	data2=data1.read()
	Label(screen10,text=data2,bg='#49A').pack()


def delete():
	deletefile1=deletefile.get()
	screen12=Toplevel(screen1)
	screen12.title("Delete")
	screen12.configure(bg='#49A')
	screen12.geometry("300x200")
	screen12.iconphoto(False, ImageTk.PhotoImage(file=logo))
	if(deletefile1==username1):
		Label(screen12,text="Access Denied ",bg='#49A').pack()
	else:
		os.remove(PATH+"\\"+username1+"\\"+deletefile1)
		Label(screen12,text="Note is deleted",bg='#49A').pack()

	

	

def NEW():
	global screen8
	screen8=Toplevel(screen1)
	screen8.title("Dashboard")
	screen8.geometry("500x350")
	screen8.configure(bg='#49A')
	screen8.iconphoto(False, ImageTk.PhotoImage(file=logo))
	global new_file
	new_file=StringVar()
	global notes
	notes=StringVar()

	Label(screen8, text="Enter note name",bg='#49A').place(x=100,y=70)
	Entry(screen8, textvariable=new_file).place(x=220,y=70)
	Label(screen8, text="Note",bg='#49A').place(x=100,y=140)
	Entry(screen8, textvariable=notes).place(x=220,y=140,height=100,width=200)
	Button(screen8, text="Save", command=save).place(x=300,y=300)


def OPEN():
	screen9=Toplevel(screen1)
	screen9.title("Dashboard")
	screen9.geometry("300x200")
	screen9.configure(bg='#49A')
	screen9.iconphoto(False, ImageTk.PhotoImage(file=logo))
	directory=PATH+"\\"+username1
	allfile=os.listdir(directory)
	global openfile
	openfile=StringVar()
	Label(screen9, text="Existing File are",bg='#49A').place(x=10,y=10)
	j=40
	k=1
	for i in allfile:
		if i.endswith("png") or i.endswith("jpg") or i.endswith("jpeg"):
			pass
		else:
			txt=str(k)+")  "+i
			Label(screen9, text=txt,bg='#49A').place(x=10,y=j)
			j=j+40
			k=k+1


	Label(screen9, text="Wtite The File Name \nWhich You Want To Open",bg='#49A').place(x=150,y=10)
	Label(screen9, text=username1,bg='#49A').place(x=150,y=30)
	Entry(screen9, textvariable=openfile).place(x=150,y=60)
	Button(screen9, text="open",command=view).place(x=190,y=100)

def DEL():
	screen11=Toplevel(screen1)
	screen11.title("Delete  Notes")
	screen11.geometry("300x200")
	screen11.configure(bg='#49A')
	screen11.iconphoto(False, ImageTk.PhotoImage(file=logo))
	directory=PATH+"\\"+username1
	allfile=os.listdir(directory)
	global deletefile
	deletefile=StringVar()
	Label(screen11, text="Existing File are",bg='#49A').place(x=10,y=10)
	j=40
	k=1
	for i in allfile:
		if i.endswith("png") or i.endswith("jpg") or i.endswith("jpeg"):
			pass
		else:
			txt=str(k)+")  "+i
			Label(screen11, text=txt,bg='#49A').place(x=10,y=j)
			j=j+40
			k=k+1
	Label(screen11, text="Wtite The File Name \nWhich You Want To Delete",bg='#49A').place(x=150,y=10)
	Entry(screen11, textvariable=deletefile).place(x=150,y=60)
	Button(screen11, text="delete",command=delete).place(x=190,y=100)


def session():
	screen7=Toplevel(screen1)
	screen7.title("Dashboard")
	screen7.geometry("400x420")
	screen7.configure(bg='#49A')
	screen7.iconphoto(False, ImageTk.PhotoImage(file=logo))


	Label(screen7,bg="grey94",width="300", height="12").place(x=0,y=0)
	Label(screen7,text="Welcome to Dashboard",bg="grey94").place(x=130,y=173)
	image = Image.open(dash_img)
	image=image.resize((140,140), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(screen7,image=photo)
	label.image = photo # keep a reference!
	label.place(x=125,y=0)

	image1 = Image.open(logo)
	image1=image1.resize((30,30), Image.ANTIALIAS)
	photo1 = ImageTk.PhotoImage(image1)
	label1 = Label(screen7,image=photo1)
	label1.image1 = photo1# keep a reference!
	label1.place(x=173,y=370)
	Button(screen7, text="NEW",bg='grey54',command=NEW).place(x=90,y=270)
	Button(screen7, text="OPEN",bg='grey54',command=OPEN).place(x=245,y=270)
	Button(screen7, text="DELETE",bg='grey54',command=DEL).place(x=165,y=320)


def login_sucess():
	global screen4
	screen4=Toplevel(screen1)
	screen4.title("Open Camera")
	screen4.geometry("300x200")
	screen4.configure(bg='#49A')
	screen4.iconphoto(False, ImageTk.PhotoImage(file=logo))
	Label(screen4, text="Click To Open Camera",bg='#49A').place(x=90,y=20)
	#usernam_obtain=cm.recog()
	image = Image.open(cam_img)
	image=image.resize((30,30), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(screen4,image=photo)
	label.image = photo # keep a reference!
	Button(screen4, image=photo, command=cammodi).place(x=140,y=70)
	#Label(screen4, text="Login Sucess").pack()
	#Button(screen4, text="OK", command=session).pack()


def Empty():
	global screen5
	screen5=Toplevel(screen1)
	screen5.title("Empty")
	screen5.geometry("300x200")
	screen5.configure(bg='#49A')
	image = Image.open(cross_button)
	image=image.resize((30,30), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(screen5,image=photo)
	label.image = photo # keep a reference!
	screen5.iconphoto(False, ImageTk.PhotoImage(file=logo))
	Label(screen5, text="Please Completely Fill The Form",bg='#49A').place(x=90,y=20)
	Button(screen5, image=photo, command=destroy5).place(x=140,y=70)

def usernot():
	global screen6
	screen6=Toplevel(screen1)
	screen6.title("UNM")
	screen6.geometry("300x200")
	screen6.configure(bg='#49A')
	screen6.iconphoto(False, ImageTk.PhotoImage(file=logo))
	image = Image.open(cross_button)
	image=image.resize((30,30), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(screen6,image=photo)
	label.image = photo # keep a reference!
	Label(screen6, text="Username Or Password not matched",bg='#49A').place(x=60,y=20)
	Button(screen6,image=photo,command=destroy6,compound=LEFT).place(x=140,y=70)


def login_verify():
	global username1
	username1=username_verify.get()
	password1=password_verify.get()
	if(username1=="" or password1==""):
		Empty()
	else:
		list_of_files=os.listdir(PATH)
		if username1 in list_of_files:
			file1=open(PATH+"\\"+username1+"\\"+username1,"r")
			verify=file1.read().splitlines()
			if password1 in verify:
				login_sucess()
			else:
				usernot()
		else:
			usernot()

def validation(password,L):
	flag = 0
	while True: 
		if (L<8): 
			flag = -1
			break
		elif not re.search("[a-z]", password): 
			flag = -1
			break
		elif not re.search("[A-Z]", password): 
			flag = -1
			break
		elif not re.search("[0-9]", password): 
			flag = -1
			break
		elif not re.search("[_@$]", password): 
			flag = -1
			break
		elif re.search(" ", password): 
			flag = -1
			break
		else: 
			flag = 0
			return False
			break
	if flag ==-1: 
		return True


def Register():
	global screen2
	screen2 = Toplevel(screen1)
	screen2.title("registration Page")
	screen2.geometry("550x550")
	screen2.configure(bg='#49A')
	screen2.iconphoto(False, ImageTk.PhotoImage(file=logo))
	global username
	global password
	username=StringVar()
	password=StringVar()

	Label(screen2, text="Please Enter The Following Details:",bg="#49A").place(x=180,y=10)
	Label(screen2, text="Username *",bg="#49A").place(x=100,y=70)
	Entry(screen2, textvariable=username).place(x=220,y=70)
	Label(screen2, text="Only small letter allowed",bg="#49A").place(x=220,y=100)
	Label(screen2, text="password *",bg='#49A').place(x=100,y=140)
	Entry(screen2, textvariable=password,show="*").place(x=220,y=140)
	Label(screen2, text="1)Minimum 8 characters.",bg='#49A').place(x=220,y=180)
	Label(screen2, text="2)The alphabets must be between [a-z].",bg='#49A').place(x=220,y=200)
	Label(screen2, text="3)At least one alphabet should be of Upper Case [A-Z].",bg='#49A').place(x=220,y=220)
	Label(screen2, text="4)At least 1 number or digit between [0-9].",bg='#49A').place(x=220,y=240)
	Label(screen2, text="5)At least 1 character from [ _ or @ or $ ].",bg='#49A').place(x=220,y=260)
	Button(screen2, text="Username Register",command=reg_user).place(x=230,y=300)
	image = Image.open(reg_img)
	image=image.resize((40,40), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(screen2,image=photo)
	label.image = photo # keep a reference!
	label.place(x=260,y=500)



	#Label(screen2, text="password *",bg='#49A').place(x=200,y=320)
	


def Login():
	global screen3
	screen3=Toplevel(screen1)
	screen3.title("Login")
	screen3.geometry("500x300")
	screen3.configure(bg='#49A')
	screen3.iconphoto(False, ImageTk.PhotoImage(file=logo))
	global username_verify
	global password_verify
	username_verify=StringVar()
	password_verify=StringVar()

	Label(screen3, text="Please Enter the details below for login",bg='#49A').place(x=180,y=10)
	
	Label(screen3, text="Username *",bg='#49A').place(x=100,y=70)
	Entry(screen3, textvariable=username_verify).place(x=220,y=70)
	Label(screen3, text="password *",bg='#49A').place(x=100,y=140)
	Entry(screen3, textvariable=password_verify, show="*").place(x=220,y=140)

	Button(screen3, text="Login verify",command=login_verify).place(x=230,y=180)
	image = Image.open(login_img)
	image=image.resize((30,30), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(image)
	label = Label(screen3,image=photo)
	label.image = photo # keep a reference!
	label.place(x=245,y=240)
	#image = Image.open("D:\\shield.png")
	#img=image.resize((30,30), Image.ANTIALIAS)
	#photo = ImageTk.PhotoImage(img)
	#Label(screen3,image=photo).place(x=245,y=240)
	screen3.mainloop()



def main_screen():
	global screen1
	screen1 = Tk()
	screen1.geometry("500x500")
	screen1.title("SECURE*")
	screen1.configure(bg='grey54')
	screen1.iconphoto(False, ImageTk.PhotoImage(file=logo))
	
	Label(text="", bg="grey94", width="300", height="12").place(x=0,y=0)
	image = Image.open(mainlogo)
	img=image.resize((140,140), Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(img)
	Label(screen1,image=photo).place(x=190,y=0)
	Label(text="Wel-Come! \n We are here to secure your wallet:)",bg='grey94').place(x=150,y=160)
	Label(text="\n\n\n\nClick Here To Login And Start Creating Notes",bg='grey54').place(x=60,y=200)
	Button(text="Login", command=Login).place(x=400,y=260)
	Label(text="\n\n\n\nIf You Dont Have An Account, Click Here",bg='grey54').place(x=60,y=280)
	Button(text="Register",command=Register).place(x=390,y=340)
	image2 = Image.open(logo)
	img2=image2.resize((30,30), Image.ANTIALIAS)
	photo2 = ImageTk.PhotoImage(img2)
	Label(screen1,image=photo2).place(x=230,y=410)
	Label(screen1,text="Copyright © 2020 HHAR. All Rights Reserved",bg="grey54").place(x=130,y=450)
	screen1.mainloop()

main_screen()
