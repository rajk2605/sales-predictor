# Task 1 :-- Sales Volume Predictor

from tkinter import *
from tkinter import messagebox
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

root = Tk()
root.title("Sales Volume Predictor By Raj")
root.geometry("500x600+50+50")
#root.configure(bg="lightblue")
f = ("Cambria", 20, "bold")

lab_header = Label(root, text="Advertising Sales Predictor", font=f)
lab_header.pack(pady=30)

lab_TV = Label(root,text="Spent on TV", font=f)
ent_TV = Entry(root, font=f)
lab_TV.pack(pady=5)
ent_TV.pack(pady=5)

lab_Radio = Label(root,text="Spent on Radio", font=f)
ent_Radio = Entry(root, font=f)
lab_Radio.pack(pady=5)
ent_Radio.pack(pady=5)

lab_Newspaper = Label(root,text="Spent on Newspaper", font=f)
ent_Newspaper = Entry(root, font=f)
lab_Newspaper.pack(pady=5)
ent_Newspaper.pack(pady=5)


def find():
	data = pd.read_csv("C:/demo/ML/internship/sales_predictor/sales.csv")
	features = data[["TV", "Newspaper", "Radio"]]  				#----> features tell us that how much budget is spent on different various advertising modes i.e. TV, Newspaper, Radio. From these advertising modes we get to see the sales volume of these three modes. 
	
	target = data["Sales"]		#---> Target is the final destination i.e. we have to find sales volume.
	x_train, x_test, y_train, y_test = train_test_split(features, target ,test_size=0.5, random_state=42)
	model = LinearRegression()
	model.fit(x_train, y_train)

	TV = (ent_TV.get())
	Radio = (ent_Radio.get())
	Newspaper = (ent_Newspaper.get())
		
	
	if not TV:
		messagebox.showerror("Error", "Please Enter TV values")
		ent_TV.focus()
		return

	if not Radio:
		messagebox.showerror("Error", "Please Enter Radio values")
		return
	
	if not Newspaper:
		messagebox.showerror("Error", "Please Enter Newspaper values")
		return


	if TV.strip() == "":
		messagebox.showerror("Error", "TV cannot be spaces")
		return

	if Radio.strip() == "":
		messagebox.showerror("Error", "Radio cannot be spaces")
		return

	if Newspaper.strip() == "":
		messagebox.showerror("Error", "Newspaper cannot be spaces")
		return

	if TV.isalpha():
		messagebox.showerror("Error", "TV cannot be text")
		return

	if Radio.isalpha():
		messagebox.showerror("Error", "Radio cannot be text")
		return

	if Newspaper.isalpha():
		messagebox.showerror("Error", "Newspaper cannot be text")
		return

	if not TV.replace('.', '', 1).isdigit():
		messagebox.showerror(f"Error", "TV cannot be Special Characters")

	if not Radio.replace('.', '', 1).isdigit():
		messagebox.showerror(f"Error", "Radio cannot be Special Characters")

	if not Newspaper.replace('.', '', 1).isdigit():
		messagebox.showerror(f"Error", "Newspaper cannot be Special Characters")


	try:
		TV = float(TV)
		Radio = float(Radio)
		Newspaper = float(Newspaper)

	except ValueError as e:
		print("Error", "Something Went Wrong!")
		return

	if (TV < 0)  :
		messagebox.showerror("Error", " TV values cannot be Negative")
		return

	if (Radio < 0)  :
		messagebox.showerror("Error", " Radio values cannot be Negative")
		return

	if (Newspaper < 0)  :
		messagebox.showerror("Error", " Newspaper values cannot be Negative")
		return
	

	if (TV < 1)  :
		messagebox.showerror("Error", " MIN. value should be 1.")
		return

	if (Radio < 1)  :
		messagebox.showerror("Error", " MIN. value should be 1.")
		return

	if (Newspaper < 1)  :
		messagebox.showerror("Error", " MIN. value should be 1.")
		return

	ent_TV.delete(0 ,'end')
	ent_Radio.delete(0, 'end')
	ent_Newspaper.delete(0, 'end')
	ent_TV.focus()


	Sales = model.predict([[TV, Radio, Newspaper]])
	msg = "Predicted Volume :" + str(round(Sales[0],2))
	lab_ans.configure(text=msg)

btn_predict = Button(root, text="Predict Sales", font=f, command=find)
lab_ans = Label(root, font=f)
btn_predict.pack(pady=5)
lab_ans.pack(pady=5)
root.mainloop()









































