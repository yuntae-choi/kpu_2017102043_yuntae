from stdafx import *

root = Tk()


colours = ['red','green','orange','white','yellow','blue']
b1 = PhotoImage(file = "물건검색버튼.gif")
r = 0

# 표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
treeview = tkinter.ttk.Treeview(root, columns=["one", "two", "three"],
                                     displaycolumns=["one", "two", "three", "four"])
treeview.pack()

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("#0", width=100, )
treeview.heading("#0", text="index")

treeview.column("#1", width=70, anchor="center")
treeview.heading("one", text="날짜", anchor="center")

treeview.column("#2", width=70, anchor="center")
treeview.heading("two", text="장소", anchor="center")

treeview.column("#3", width=70, anchor="center")
treeview.heading("three", text="설명", anchor="center")

treeview.column("#4", width=100, anchor="center")
treeview.heading("four", text="사진", anchor="center")

# 표에 삽입될 데이터
treelist = [("Tom", 80, 3), ("Bani", 71, 5), ("Boni", 90, 2), ("Dannel", 78, 4), ("Minho", 93, 1)]

# 표에 데이터 삽입
for i in range(len(treelist)):
    treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i) + "번")
    top = treeview.insert('', 'end', text="hidden index", iid="5번")
    top_mid1 = treeview.insert(top, 'end', text="5", values=["Timy", 0, 8], iid="5번-1")
    Label(root, image=b1, relief=tk.RIDGE).grid(row=r, column=0)
    Entry(root, bg=c, relief=tk.SUNKEN, width=10).grid(row=r, column=1)
    r = r + 1

root = Tk()

colours = ['red','green','orange','white','yellow','blue']
b1 = PhotoImage(file = "물건검색버튼.gif")
r = 0
for c in colours:
    Label(root,image=b1, relief=tk.RIDGE).grid(row=r,column=0)
    Entry(root,bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
    r = r + 1

tk.mainloop()



