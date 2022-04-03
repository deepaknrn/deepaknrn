import tkinter

window=tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)

dummy_label=tkinter.Label(text="")
dummy_label.grid(column=0,row=0)

input=tkinter.Entry()
input.config(text=0)
input.grid(column=1,row=0)

dummy_label2=tkinter.Label(text="Miles",font=("Arial",8,"bold"))
dummy_label2.grid(column=2,row=0)

dummy_label3=tkinter.Label(text="is equal to", font=("Arial",10,"bold"))
dummy_label3.grid(column=0,row=1)

output=tkinter.Entry()
output.grid(column=1,row=1)

dummy_label4=tkinter.Label(text="Km",font=("Arial",8,"bold"))
dummy_label4.grid(column=2,row=1)

def convert():
  in1=input.get()
  print(in1)
  if in1=="":
    output.insert(0,string="0")
  else:
    in2=int(in1)*10
    output.insert(0,string=str(in2))

button = tkinter.Button(text="Calculate",command=convert)
button.grid(column=1,row=2)


window.mainloop()
