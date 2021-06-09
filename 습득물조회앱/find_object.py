from stdafx import *
class find_object:
    def __init__(self):
        self.g_TK = Tk()
        self.g_TK.geometry("390x790+750+200")
        self.g_TK.configure(bg='white')
        self.DataList = []
        self.pageList = []
        self.page_cnt = 1
        self.page_pre = 1


        self.notebook = tkinter.ttk.Notebook(self.g_TK , width=390, height=770)
        self.notebook.pack()
        self.wall = PhotoImage(file = "아이폰첫화면.gif")
        self.wall2 = PhotoImage(file = "날짜검색.gif")
        self.wall3 = PhotoImage(file = "위치아이폰.gif")
        self.wall4 = PhotoImage(file="아이폰.gif")


        self.b1 = PhotoImage(file = "날짜버튼.gif")
        self.b2 = PhotoImage(file = "위치버튼.gif")
        self.b3 = PhotoImage(file = "물건검색버튼.gif")
        self.b4 = PhotoImage(file = "위치버튼아이콘.gif")
        self.b5 = PhotoImage(file = "지도버튼.gif")
        self.b6 = PhotoImage(file = "메일.gif")


        self.frame1=Frame(self.g_TK)
        self.notebook.add(self.frame1)
        self.pageList.append(self.frame1)
        self.label1=Label(self.frame1,bg='white',image = self.wall)
        self.label1.place(x = -10,y = -10)
        self.label1.pack()


        self.frame2 = Frame(self.g_TK)
        self.notebook.add(self.frame2)
        self.pageList.append(self.frame2)

        self.label2=Label(self.frame2,bg='white', image = self.wall2)
        self.label2.place(x = -10,y = -10)
        self.label2.pack()

        self.frame3=Frame(self.g_TK)
        self.notebook.add(self.frame3)
        self.pageList.append(self.frame3)

        self.label3=Label(self.frame3,bg='white',image = self.wall3)
        self.label3.place(x = -10,y = -10)
        self.label3.pack()

        self.frame4=Frame(self.g_TK)
        self.notebook.add(self.frame4)
        self.pageList.append(self.frame4)

        self.label4=Label(self.frame4,bg='white')
        self.label4.place(x = -10,y = -10)
        self.label4.pack()

        self.frame5 = Frame(self.g_TK)
        self.notebook.add(self.frame5)
        self.pageList.append(self.frame5)

        self.label5 = Label(self.frame5, bg='white',image = self.wall4)
        self.label5.place(x=-10, y=-10)
        self.label5.pack()

        self.key = "A762Mvt41oxxLGNbDOqSVdZ0o70TqIdu%2BasUtVXihiiC7Een2bHDYGp1CKesvBHiEda3tQ%2B5FFhfQoOY%2B0Vnfg%3D%3D"
        self.url = "http://apis.data.go.kr/1320000/LosfundInfoInqireService"
        # Define globals.
        self.date_string = ""
        self.timestamp = None
        self.da_str = ""
        self.todaystamp = None
        self.imList = []
        self.imgList = []
        self.idList = []
        self.sdList = []

        self.homepage()
        self.InitInput()
        self.InitInput2()

        self.InitRenderText()
        self.InitRenderText2()

        self.InitBackButton()
        self.InitSearch1Button()
        self.InitSearch2Button()
        self.InitSearch3Button()
        self.InitSearch4Button()
        self.InitSearch5Button()

        self.g_TK.mainloop()



    def print_sel(self, date_label, cal, root):
            cal_selection = cal.selection_get()
            date_string = cal_selection.strftime("%Y-%m-%d")
            self.da_str = cal_selection.strftime("%Y%m%d")
            # Update the text on the date label.
            date_label.configure(text=" {}".format(date_string))
            root.destroy()

    def datecheck(self, date_label):
        root = tk.Toplevel()
        s = ttk.Style(root)
        s.theme_use('clam')

        today = date.today()
        d = int(today.strftime("%d"))
        m = int(today.strftime("%m"))
        y =int(today.strftime("%Y"))
        root.geometry("280x280+770+250")
        cal = Calendar(root,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", day=d,month=m, year=y)
        cal.pack(fill="both", expand=True)
        self.print_sel_callback = partial(self.print_sel, date_label, cal, root)
        ttk.Button(root, text="ok", command=self.print_sel_callback).pack()
    def homepage(self):
        if self.date_string == "":
            self.timestamp = datetime.now().strftime("%Y-%m-%d")
            self.todaystamp = datetime.now().strftime("%d")
            self.todaystr = datetime.now().strftime("%Y%m%d")
        else:
            self.timestamp = self.date_string

        TempFont = font.Font(self.frame2, size=21, weight='bold', family="MS Gothic")
        date_label = Label(self.frame2, text="   {}   ".format(self.timestamp), bg="#C1C1C1", font=TempFont)
        date_label.pack()
        date_label.place(x=100, y=155)

        self.datecheck_callback = partial(self.datecheck, date_label)
        TempFont = font.Font(self.g_TK, size=17, weight='bold', family="MS Gothic")
        button = tk.Button(self.frame2, font = TempFont ,bg='#F4F4F4',bd = 0,
                           text="{}".format(self.todaystamp),
                           command=self.datecheck_callback)
        button.place(x=51, y=161)


    def userURIBuilder(self,uri, **user):
        str = uri + "?"
        for key in user.keys():
            str += key + "=" + user[key] + "&"
        return str

    def InitBackButton(self):
        TempFont = font.Font(self.g_TK, size=12, weight='bold', family = "MS Gothic")
        BackButton = Button(self.g_TK, font=TempFont, text="< Back", fg='#0099FF', bg='white', bd = 0 ,pady = 2, command = self.Selectbackpage)
        BackButton.pack()
        BackButton.place(x=33, y=86)


    def InitSearch1Button(self):
        Search1Button = Button(self.frame1, image = self.b1, bd = 0 ,command=self.Selectpage2)
        Search1Button.pack()
        Search1Button.place(x=42, y=218)

    def InitSearch2Button(self):
        Search2Button = Button(self.frame1,image = self.b2, bd = 0,  command=self.Selectpage3)
        Search2Button.pack()
        Search2Button.place(x=42, y=398)

    def Selectpage2(self):
        self.page_pre = self.page_cnt
        self.page_cnt = 2
        self.notebook.select(self.frame2)

    def Selectpage3(self):
        self.page_pre = self.page_cnt
        self.page_cnt = 3
        self.notebook.select(self.frame3)

    def Selectpage4(self):
        self.page_pre = self.page_cnt
        self.page_cnt = 4
        self.notebook.select(self.frame4)

    def Selectpage5(self):
        self.page_pre = self.page_cnt
        self.page_cnt = 5
        self.notebook.select(self.frame5)



    def Selectbackpage(self):
        if self.page_cnt == self.page_pre:
            if self.page_cnt > 1 and self.page_pre > 1:
                if self.page_cnt == 3 and self.page_pre == 3:
                    self.page_cnt = 1
                    self.page_pre = 1
                elif self.page_cnt == 5 and self.page_pre == 5:
                    self.page_cnt = 2
                    self.page_pre = 2
                else:
                    self.page_cnt -=1
                    self.page_pre -=1
                self.notebook.select(self.pageList[self.page_cnt - 1])
        else:
            self.page_cnt = self.page_pre
            self.notebook.select(self.pageList[self.page_cnt-1])


    def InitInput(self): # entry 입력창

        TempFont = font.Font(self.frame2, size=20, weight='bold', family = 'Consolas')
        self.Input_Entry = Entry(self.frame2, font = TempFont, width = 13, borderwidth = 0, bg='#C1C1C1')
        self.Input_Entry.pack()
        self.Input_Entry.place(x=80, y=210)


    def InitSearch3Button(self):

        Search3Button = Button(self.frame2,image = self.b3, bd = 0, bg ='#C1C1C1',  command=self.SearchButtonAction)
        Search3Button.place(x=300, y=208)

    def SearchButtonAction(self):

        self.canvas.configure(state='normal')
        self.canvas.delete(ALL)
        self.imList = []
        self.imgList = []
        self.idList = []
        self.sdList = []
        self.SearchLibrary()
        self.Searchimg()
        self.canvas.configure(state='disabled')

    def InitSearch4Button(self):
        Search4Button = Button(self.frame3,image = self.b3, bd = 0, bg ='#C1C1C1',  command=self.SearchButtonAction2)
        Search4Button.pack()
        Search4Button.place(x=300, y=207)

    def SearchButtonAction2(self):
        self.canvas2.configure(state='normal')
        self.canvas2.delete(ALL)
        self.imList = []
        self.imgList = []
        self.idList = []
        self.sdList = []
        self.SearchLibrary2()
        self.canvas2.configure(state='disabled')


    def InitSearch5Button(self):
        Search5Button = Button(self.frame3,image = self.b4, bd = 0, bg ='white',  command=self.out_point)
        Search5Button.pack()
        Search5Button.place(x=45, y=145)


    def InitInput2(self): # entry 입력창

        TempFont = font.Font(self.frame3, size=20, weight='bold', family = 'Consolas')
        self.Input_Entry2 = Entry(self.frame3, font = TempFont, width = 13, borderwidth = 0, bg='#C1C1C1')
        self.Input_Entry2.pack()
        self.Input_Entry2.place(x=80, y=210)

    def out_point(self):

        TempFont = font.Font(self.frame3, size=21, weight='bold', family="MS Gothic")
        self.point_label = Label(self.frame3, text="시흥시 신천로", bg="#C1C1C1", font=TempFont)
        self.point_label.pack()
        self.point_label.place(x=100, y=155)



    def Init_url_img(self,url):
        from io import BytesIO
        import urllib
        import urllib.request
        from PIL import Image, ImageTk
        # openapi로 이미지 url을 가져옴.
        #url = self.imgList[n]
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        print(url+'\n')
        im = Image.open(BytesIO(raw_data))
        im1 = im.resize((250, 330), Image.ANTIALIAS)
        im = im.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)
        img1 = ImageTk.PhotoImage(im1)
        self.imgList.append(img)
        self.imList.append(img1)

    def SearchimgAction(self, cnt):

        self.canvas.configure(state='normal')
        self.canvas.delete(0.0, END)
        self.Searchid(cnt)
        self.canvas.configure(state='disabled')



    def SearchLibrary(self):
        import main
        if self.Input_Entry.get() != '':
            uri = self.userURIBuilder("/getLosfundInfoAccToClAreaPd", serviceKey=self.key, START_YMD= "{}".format(self.da_str),
                                 END_YMD="{}".format(self.todaystr), N_FD_LCT_CD="LCA000", pageNo="1", numOfRows="10")
            res = requests.get(self.url+uri)
            soup = BeautifulSoup(res.content, 'xml')
            names = soup.find_all('item')
            Tcnt = soup.find('totalCount').get_text()
            y=0
            cnt = 0
            total = main.t_count(Tcnt)
            print(total)
            for i in range(1,total):
                print(i)
                uri = self.userURIBuilder("/getLosfundInfoAccToClAreaPd", serviceKey=self.key,
                                          START_YMD="{}".format(self.da_str),
                                          END_YMD="{}".format(self.todaystr), N_FD_LCT_CD="LCA000", pageNo=str(i),
                                          numOfRows="10")
                res = requests.get(self.url + uri)
                soup = BeautifulSoup(res.content, 'xml')
                names = soup.find_all('item')
                for n in names:
                    if self.Input_Entry.get() in n.find('prdtClNm').get_text():
                        self.Init_url_img(n.find('fdFilePathImg').get_text())
                        self.idList.append(n.find('atcId').get_text())
                        self.sdList.append(n.find('fdSn').get_text())
                        self.SearchimgAction_callback = partial(self.SearchimgAction, cnt)
                        cnt += 1
                        button = tkinter.Button(self.frame2, text = n.find('fdYmd').get_text() +"\n" + n.find('depPlace').get_text(),
                                                font=("Courier", 15),
                                                bg = '#F4F4F4' , bd = 0,
                                                command = self.SearchimgAction_callback)
                        self.canvas.create_window(60, y, window=button, anchor=NW)
                        y += 60
                if cnt == 0:
                    label = Label(self.frame2, text="검색 결과 없음",
                                            bg='#F4F4F4', bd=0,
                                            font=("Courier", 25))
                    self.canvas.create_window(0, y, window=label, anchor=NW)

    def Searchimg(self):
        y=0
        for n in self.imgList:
            label = tkinter.Label(self.frame2, image = n, height=50, width=50, compound=RIGHT)
            self.canvas.create_window(0,y, window=label, anchor=NW)
            y += 60

    def Searchid(self,cnt):

        uri = self.userURIBuilder("/getLosfundDetailInfo", serviceKey=self.key, ATC_ID ="{}".format(self.idList[cnt]) ,
                                  FD_SN = "{}".format(self.sdList[cnt]))
        res = requests.get(self.url + uri)
        soup = BeautifulSoup(res.content, 'xml')
        names = soup.find_all('item')

        y = 0
        y2 = 0
        dep = ''
        tel = ''
        for n in names:
            if self.Input_Entry.get() in n.find('prdtClNm').get_text():
                self.Init_url_img(n.find('fdFilePathImg').get_text())
                dep = n.find('depPlace').get_text()
                tel = n.find('tel').get_text()
                uni = n.find('uniq').get_text()
                label1 = Label(self.frame5, image = self.imList[cnt], height=250, width=320, compound=RIGHT)
                label1.pack()
                label1.place(x = 30, y =85 )

                label3 = Label(self.frame5,
                              text=uni,
                               wraplength = 330,
                              font=("Courier", 11), bg="white")
                label2 = Label(self.frame5,
                               text="보관 장소 : " + dep + "\n"
                                    + "습득 장소 : " + n.find('fdPlace').get_text() + "\n"
                                    + "습득일자 : " + n.find('fdYmd').get_text() + "\n"
                                    + "전화번호 : " + tel + "\n",
                               font=("Courier", 13), bg="white")

                label3.pack()
                label3.place(x=30, y=380)
                label2.pack()
                label2.place(x=72, y=340)


        self.map_callback = partial(self.map, dep, tel)
        map_button = Button(self.frame5, image = self.b5, bd =0, command=self.map_callback)
        map_button.pack()
        map_button.place(x=42, y=680)

        self.mail_callback = partial(self.mail, dep, tel, uni)
        mail_button = Button(self.frame5, image=self.b6, bd=0, command=self.mail_callback)
        mail_button.pack()
        mail_button.place(x=290, y=680)

        self.Selectpage5()

    def MakeHtmlDoc(self, BookList):
        from xml.dom.minidom import getDOMImplementation
        # get Dom Implementation
        impl = getDOMImplementation()

        newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
        top_element = newdoc.documentElement
        header = newdoc.createElement('header')
        top_element.appendChild(header)

        # Body 엘리먼트 생성.
        body = newdoc.createElement('body')

        for bookitem in BookList:

            # BR 태그 (엘리먼트) 생성.
            br = newdoc.createElement('br')

            body.appendChild(br)

            # create title Element
            p = newdoc.createElement('p')
            # create text node
            titleText = newdoc.createTextNode(bookitem)
            p.appendChild(titleText)

            body.appendChild(p)
            body.appendChild(br)  # line end

        # append Body
        top_element.appendChild(body)

        return newdoc.toxml()

    def InitInput3(self, root):  # entry 입력창

        self.Input_Entry3 = Entry(root,font=("Courier", 14), width=25, borderwidth=0, bg='light gray')
        self.Input_Entry3.pack()
        self.Input_Entry3.place(x=104, y=31)

    def mail(self, dep, tel, uni):
        root = tk.Toplevel()
        s = ttk.Style(root)
        s.theme_use('clam')
        root.geometry("390x70+750+250")
        M = []
        M.append(dep)
        M.append(tel)
        M.append(uni)
        html = ""

        html = self.MakeHtmlDoc(M)
        label1 = Label(root, bg = 'white', width=390, height = 70)
        label1.pack()
        label1.place(x=0, y=0)
        self.InitInput3(root)
        self.send_callback = partial(self.send, html, root)
        label = Label(root, text="보낼 주소 :", font=("Courier", 13),fg='#0099FF', bg='white', bd = 0 ,pady = 2)
        label.pack()
        label.place(x=0, y=30)
        send_button = Button(root, text="send", font=("Courier", 13), fg='white', bg='#0099FF', bd = 0 ,pady = 2 ,command=self.send_callback)
        send_button.pack()
        send_button.place(x=335, y=24)

    def send(self, html, root):
        host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
        port = "587"
        recipientAddr = ''
        title = "습득물 조회"
        senderAddr = 'jinyeong8229@gmail.com'
        recipientAddr = self.Input_Entry3.get()
        msgtext = 'kpu'
        passwd = 'jinyung8229'
        root.destroy()

        import mysmtplib
        # MIMEMultipart의 MIME을 생성합니다.
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Message container를 생성합니다.
        msg = MIMEMultipart('alternative')

        # set message
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        msgPart = MIMEText(msgtext, 'plain')
        bookPart = MIMEText(html, 'html', _charset='UTF-8')

        # 메세지에 생성한 MIME 문서를 첨부합니다.
        msg.attach(msgPart)
        msg.attach(bookPart)

        print("connect smtp server ... ")
        s = mysmtplib.MySMTP(host, port)
        # s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)  # 로긴을 합니다.
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

        print("Mail sending complete!!!")

    def map(self, dep, tel):
        import pandas as pd
        #root.destroy()
        point = "{}".format(dep)
        csv = pd.read_csv('경찰청_경찰관서위치,주소_20200409.csv', \
                          names=['청', '서', '지구대파출소', 'X좌표', 'Y좌표', '주소'], \
                          encoding='cp949')

        find_row = csv.loc[(csv['지구대파출소'] == point)]
        find_row = find_row.iloc[:, 3:5]
        x = find_row['X좌표']
        y = find_row['Y좌표']
        x_val = x.values.tolist()
        y_val = y.values.tolist()
        print(x_val)
        print(y_val)
        self.Init_map(x_val,y_val,point)

    def Init_map(self, x_val, y_val, point):
        import threading
        import sys
        from tkinter import messagebox
        # pip install folium
        import folium
        # pip install cefpython3==66.1
        from cefpython3 import cefpython as cef

        # cef모듈로 브라우저 실행
        def showMap(frame):
            sys.excepthook = cef.ExceptHook
            window_info = cef.WindowInfo(frame.winfo_id())
            window_info.SetAsChild(frame.winfo_id(), [0, 0, 390, 790])
            cef.Initialize()
            browser = cef.CreateBrowserSync(window_info, url='file:///map.html')
            cef.MessageLoop()

        def Pressed():
            # 지도 저장
            # 위도 경도 지정
            m = folium.Map(location=[float(y_val[0]), float(x_val[0])], zoom_start=40)
            # 마커 지정
            folium.Marker([float(y_val[0]), float(x_val[0])], popup=point).add_to(m)
            # html 파일로 저장
            m.save('map.html')

            # 브라우저를 위한 쓰레드 생성
            thread = threading.Thread(target=showMap, args=(self.frame4,))
            thread.daemon = True
            thread.start()
        self.Selectpage4()
        Pressed()





    def _on_mousewheel(self,event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.canvas.pack()
        self.canvas.place(x=55, y=300)

    def InitRenderText(self):
        self.canvas = Canvas(self.frame2,width = 285, height = 300 , bg= "#F4F4F4", bd=0)
        self.canvas.pack(expand=True, fill="both")
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.place(x=55, y=300)




    def SearchimgAction2(self, cnt):
        self.canvas2.configure(state='normal')
        self.canvas2.delete(0.0, END)
        self.Searchid(cnt)
        self.canvas2.configure(state='disabled')
    def SearchLibrary2(self):
        if self.Input_Entry2.get() != "":
            uri = self.userURIBuilder("/getLosfundInfoAccToLc", serviceKey=self.key, PRDT_NM = self.Input_Entry2.get(),
                                 ADDR = "경기도 시흥시 신천로", pageNo="1", numOfRows="10")
            res = requests.get(self.url+uri)
            soup = BeautifulSoup(res.content, 'xml')
            names = soup.find_all('item')
            y = 0
            cnt = 0
            for n in names:
                if self.Input_Entry2.get() in n.find('prdtClNm').get_text():
                    self.idList.append(n.find('atcId').get_text())
                    self.sdList.append(n.find('fdSn').get_text())
                    self.SearchimgAction2_callback = partial(self.SearchimgAction2, cnt)
                    cnt += 1
                    button = tkinter.Button(self.frame3,
                                            text=n.find('fdYmd').get_text()+ " "+ n.find('depPlace').get_text(),
                                            font=("Courier", 15),
                                            bg='#F4F4F4', bd=0,
                                            command=self.SearchimgAction2_callback)
                    self.canvas2.create_window(0, y, window=button, anchor=NW)
                    y += 60
            if cnt == 0:
                label = Label(self.frame3, text="검색 결과 없음",
                              bg='#F4F4F4', bd=0,
                              font=("Courier", 25))
                self.canvas2.create_window(0, y, window=label, anchor=NW)

    def _on_mousewheel2(self, event):
        self.canvas2.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.canvas2.pack()
        self.canvas2.place(x=55, y=300)


    def InitRenderText2(self):
        self.canvas2 = Canvas(self.frame3, width=285, height=300, bg="#F4F4F4", bd=0)
        self.canvas2.pack(expand=True, fill="both")
        self.canvas2.bind("<MouseWheel>", self._on_mousewheel2)
        self.canvas2.place(x=55, y=300)
find_object()















