from flask import Flask, render_template,request,redirect,url_for
import os,pymysql,glob
import glob
# from PIL import Image 제 컴퓨터에서 에러가나서 잠시 주석처리

app= Flask(__name__)
print(__name__) #__main__ 값이 나온다.

@app.route('/') # 메인페이지
def index():
    return render_template("index.html")


@app.route('/dest11') # 여행지 전체
def dest11():
    return render_template("dest11.html")  

@app.route('/detail01') # 디테일 01
def detail01():
    return render_template("detail01.html") 

@app.route('/detail02') # 디테일 02
def detail02():
    return render_template("detail02.html")  

@app.route('/detail03') # 디테일 03
def detail03():
    return render_template("detail03.html")  

@app.route('/detail04') # 디테일 04
def detail04():
    return render_template("detail04.html")

@app.route('/detail05') # 디테일 05
def detail05():
    return render_template("detail05.html")  

@app.route('/detail06') # 디테일 06
def detail06():
    return render_template("detail06.html")  

@app.route('/detail07') # 디테일 07
def detail07():
    return render_template("detail07.html")  

@app.route('/detail08') # 디테일 08
def detail08():
    return render_template("detail08.html")  

@app.route('/detail09') # 디테일 09
def detail09():
    return render_template("detail09.html")  

@app.route('/detail10') # 디테일 10
def detail10():
    return render_template("detail10.html")  

@app.route('/detail11') # 디테일 11
def detail11():
    return render_template("detail11.html")

@app.route('/accom') # 숙소 전체
def accom():
    return render_template("accom.html")


@app.route('/detail_acc01') # 숙소 디테일01
def detail_acc01():
    return render_template("detail_acc01.html") 

@app.route('/detail_acc02') # 숙소 디테일 02
def detail_acc02():
    return render_template("detail_acc02.html")  

@app.route('/detail_acc03') # 숙소 디테일 03
def detail_acc03():
    return render_template("detail_acc03.html")  

@app.route('/detail_acc04') # 숙소 디테일 04
def detail_acc04():
    return render_template("detail_acc04.html")

@app.route('/detail_acc05') # 숙소 디테일 05
def detail_acc05():
    return render_template("detail_acc05.html")  

@app.route('/detail_acc06') # 숙소 디테일 06
def detail_acc06():
    return render_template("detail_acc06.html")  

@app.route('/detail_acc07') # 숙소 디테일 07
def detail_acc07():
    return render_template("detail_acc07.html")  

@app.route('/detail_acc08') # 숙소 디테일 08
def detail_acc08():
    return render_template("detail_acc08.html")  

@app.route('/detail_acc09') # 숙소 디테일 09
def detail_acc09():
    return render_template("detail_acc09.html")  

@app.route('/detail_acc10') # 숙소 디테일 10
def detail_acc10():
    return render_template("detail_acc10.html")  

@app.route('/map_case')
def map_case():
    return render_template("map_case.html")  

@app.route('/memcreate',methods=['GET','POST'])
def memcreate():
    if request.method == 'GET':
        return render_template('memcreate.html')
    else:
        # print(type(request.values)) #딕셔너리임을 확인
        # for key in request.values:
        #     print(key,":",request.values[key])
        f = request.files['imgpath']
        imgpath = os.path.dirname(__file__)+'/uploads/'+request.values['Name']+'_'+f.filename
        filename = request.values['Name']+'_'+f.filename
        print(imgpath)
        f.save(imgpath)
        import datetime
        now = datetime.datetime.now()
        try:
        ####### 데이터베이스 쿼리.txt 참고해주세요
            conn = pymysql.connect(host='localhost',
                        user='root',
                        password='1234',
                        db='pract1',
                        cursorclass=pymysql.cursors.DictCursor)
            with conn.cursor() as cursor:
                sql = "INSERT INTO untacttrip VALUES(%s, %s, %s, %s, %s, %s, %s, %s)" # image path 넣을 부분 %s 넣어야함
                cursor.execute(sql,(request.values['Email'],request.values['여행후기'],filename,request.values['Name'],request.values['Password'],request.values['Phone'],request.values['Address'],now)) 
                conn.commit()
        finally:
            conn.close()
        return redirect('/list')
@app.route('/list')
def list():
    import datetime
    now = datetime.datetime.now()         
    try:
        conn = pymysql.connect(host='localhost',
                        user='root',
                        password='1234',
                        db='pract1',
                        cursorclass=pymysql.cursors.DictCursor)
        with conn.cursor() as cursor:
           
            sql = "select 여행후기, imgpath, Name, Create_data from untacttrip" # imgpath 써야함 # list.html에도 넣어줘야함
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            conn.commit()
    finally:
        conn.close()

    return render_template('list.html',data = result) # data라는 이름으로 result를 보낸다.


if __name__ == '__main__':
    app.run(debug=True,port = 5000) 
# debug=True,port = 5000