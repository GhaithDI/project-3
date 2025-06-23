from flet import * 
import sqlite3
conn=sqlite3.connect('student_data',check_same_thread=False)
cursor=conn.cursor()
cursor.execute('''create table if not exists  student_data(
               id integer primary key autoincrement,
               stdname text,
               stdmail text,
               stdphon text,
               stdadress text,
               stdmathamtik integer,
               stdarabic integer,
               stdfrance integer,
               stddraw integer,
               stdenglisch integer,
               stdchemistry integer
               
               
               )''')
conn.commit() 
def main(apk:Page):
          apk.window.height=800
          apk.window.width=390
          apk.window.left=990
          apk.window.top=10
          apk.bgcolor=colors.WHITE
          apk.theme_mode=ThemeMode.LIGHT
          apk.scroll='auto'
          ### data base build###
          qure=f'select count (*) from {'student_data'}'
          cursor.execute(qure)
          result=cursor.fetchone()
          row_count=result[0]
          
          def add(e):
                  cursor.execute('insert into student_data(stdname,stdmail,stdphon,stdadress,stdmathamtik,stdarabic,stdfrance,stddraw ,stdenglisch,stdchemistry) values(?,?,?,?,?,?,?,?,?,?)',(tname.value,tmail.value,tphone.value,tadress.value,mathmatik.value,arabic.value,fransh.value,draw.value,engilsch.value,chemistry.value))
                  conn.commit()
          def show(e):
                  apk.clean()
                  c=conn.cursor()
                  c.execute('select * from student_data')  
                  users=c.fetchall()
                  print(users) 
                  if  not users =='':
                          keys=['id','stdname','stdmail','stdphon','stdadress','stdmathamtik','stdarabic','stdfrance','stddraw','stdenglisch','stdchemistry']
                          result=[dict(zip(keys,valus)) for valus in users]
                          for x in result:
                                  ## marks
                                  m=x['stdmathamtik']
                                  a=x['stdarabic']
                                  f=x['stdfrance']
                                  e=x['stdenglisch']
                                  d=x['stddraw']
                                  c=x['stdchemistry']
                                  res=m+a+f+e+d+c
                                  if res <50:
                                          a=Text('😭 راسب',size=19,color=colors.RED)
                                          
                                  elif res >50:
                                          a=Text('🥰 ناجح',size=18,color=colors.GREEN)        
                                  ## end marks ##
                                  
                                  apk.add(
                                          Card(
                                                  color=colors.BLACK,
                                                  content=Container(
                                                          content=Column([
                                                                  ListTile(
                                                                          leading=Icon(icons.PERSON),icon_color=colors.PURPLE,
                                                                          title=Text('Name :'+x['stdname'],color=colors.WHITE),
                                                                          subtitle=Text('Student E-mail: '+x['stdmail'],color=colors.WHITE),

                                                                  ),
                                                                  Row([
                                                                          Text('Phone : '+x['stdphon'],color=colors.AMBER),
                                                                          Text('Adress : '+x['stdadress'],color=colors.AMBER),
                                                                  ],MainAxisAlignment.CENTER),
                                                                  Row([
                                                                          Text('رياضيات :' +str(x['stdmathamtik']),color=colors.WHITE),
                                                                          Text(' عربي :' +str(x['stdarabic']),color=colors.WHITE),
                                                                          Text(' فرنسي :' +str(x['stdfrance']),color=colors.WHITE),
                                                                  ],MainAxisAlignment.END),
                                                                  Row([
                                                                          Text('رسم :'+str(x['stddraw']),color=colors.WHITE),
                                                                          Text(' انجليزي :'+str(x['stdenglisch']),color=colors.WHITE),
                                                                          Text('كيمياء :'+str(x['stdchemistry']),color=colors.WHITE),
                                                                  ],MainAxisAlignment.END),
                                                                  Row([
                                                                          a
                                                                  ],MainAxisAlignment.CENTER)
                                                          ])
                                                  )
                                          )
                                  )
                                  apk.update()

         
          ### end data base build #####
          ### fields ###
          tname=TextField(label='اسم الطالب',height=38,rtl=True,icon=icons.PERSON)
          tmail=TextField(label='البريد الالكتروني',height=38,rtl=True,icon=icons.MAIL)
          tphone=TextField(label='رقم الهاتف',height=38,rtl=True,icon=icons.PHONE)
          tadress=TextField(label='العنوان او مكان السكن',height=38,rtl=True,icon=icons.LOCATION_CITY)
          ### fields ###
          ### marks###
          student_marks=Text('Marks Student - علامات الطالب',size=18,color=colors.BLACK,text_align='center')
          mathmatik=TextField(label='رياضيات',width=110,rtl=True,height=38)
          arabic=TextField(label='عربي',width=110,rtl=True,height=38)
          engilsch=TextField(label='انجليزي',width=110,rtl=True,height=38)
          fransh=TextField(label='فرنسي',width=110,rtl=True,height=38)
          draw=TextField(label='رسم',width=110,rtl=True,height=38)
          chemistry=TextField(label='كيمياء',width=110,rtl=True,height=38)
          ## end marks ##
          ## buttins##
          addbuttun=ElevatedButton(
                  'اضافة طالب جديد',
                  width=170,
                  style=ButtonStyle(bgcolor=colors.BLUE,color=colors.WHITE,padding=15),
                  on_click=add
          )
          showbuttun=ElevatedButton(
                  'عرض كل الطلاب ',
                  width=170,
                  style=ButtonStyle(bgcolor=colors.BLUE,color=colors.WHITE,padding=15),
                  on_click=show
          )
          ### end buttuns
         
         
          apk.add(
                  Row([
                          Image('prjeckt2 logo.gif',width=280)
                  ],MainAxisAlignment.CENTER),
                  Row([
                          Text('تطبيق الطالب والمعلم  في الجيب',size=20,font_family='Impact',color=colors.BLACK)
                  ],MainAxisAlignment.CENTER),
                  Row([
                          Text('عدد الطلاب المسجلين :',size=20,font_family='Impact',color=colors.BLUE),
                          Text(row_count,size=20,font_family='arial',color=colors.BLACK)
                  ],MainAxisAlignment.CENTER,rtl=True),
                  tname,
                  tmail,
                  tphone,
                  tadress,
                  Row([
                          student_marks
                  ],MainAxisAlignment.CENTER),
                  Row([
                          mathmatik,arabic,fransh
                  ],MainAxisAlignment.CENTER,rtl=True),
                  Row([
                          draw,engilsch,chemistry
                  ],MainAxisAlignment.CENTER,rtl=True),
                  Row([
                          addbuttun,showbuttun
                  ],MainAxisAlignment.CENTER,rtl=True),
                

          )
          
          
          apk.update()
app(main)