from flask import Flask,render_template,redirect,url_for,flash,request,session,logging
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,IntegerField
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from functools import wraps

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "aquarium"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
app.secret_key = "aquarium"

# Kullanıcı Kayıt Formu
class KullaniciKayitFormu(Form):
    Adi_Soyadi = StringField("Adı Soyadı",validators=[validators.DataRequired()])
    Email = StringField("Email", validators=[validators.Email()])
    Sifre = PasswordField("Şifre", validators=[validators.DataRequired()])

# Giriş Sayfası Formu
class GirisFormu(Form):
    Email = StringField("E-Mail")
    Sifre = PasswordField("Şifre")

# Veri Ekleme Sayfası
class VeriEkleme(Form):
    Baslik = StringField("Başlık",validators=[validators.DataRequired()]) 
    Kh = IntegerField("Kh",default=0)
    Alkalinity = IntegerField("Alkalinity",default=0)  
    Ca = IntegerField("Ca",default=0)
    Mg = IntegerField("Mg",default=0)
    Fosfat = IntegerField("Fosfat",default=0)
    NO3 = IntegerField("NO3",default=0)
    PH = IntegerField("PH",default=0) 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın!","danger") 
            return redirect(url_for("login"))    
    return decorated_function    

# AnaSayfa
@app.route('/')
def index():
    return render_template("index.html")  

# Kayıt Sayfası
@app.route('/register',methods=["GET","POST"])
def register():
    form = KullaniciKayitFormu(request.form)
   
    if request.method == "POST" and form.validate():
        Adi_Soyadi = form.Adi_Soyadi.data
        Email = form.Email.data
        Sifre = sha256_crypt.encrypt(form.Sifre.data) 

        cursor = mysql.connection.cursor()
        sorgu = "select * from Users where Email=%s"
        result = cursor.execute(sorgu,(Email,))

        if result == 0:
            cursor = mysql.connection.cursor()
            sorgu2 = "insert into Users (Adi_Soyadi,Email,Sifre) values (%s,%s,%s)"
            cursor.execute(sorgu2,(Adi_Soyadi,Email,Sifre))
            mysql.connection.commit()
            cursor.close()
            flash("Kaydınız Tamamlandı.","success")
            return redirect(url_for("login"))
        else:
            flash("Bu E-Mail sistemde kayıtlıdır!","warning")  
            return render_template("login.html",form=form)  
    else:
        return render_template("register.html",form=form)

# Giriş Sayfası
@app.route('/login',methods=["GET","POST"])
def login():
    form = GirisFormu(request.form)

    if request.method == "POST":
        Email = form.Email.data
        Sifre = form.Sifre.data

        cursor = mysql.connection.cursor()
        sorgu = "select * from Users where Email = %s"
        result = cursor.execute(sorgu,(Email,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["Sifre"]  

            if sha256_crypt.verify(Sifre,real_password):
                flash("Başarıyla Giriş Yaptınız.","success")

                session["logged_in"] = True
                session["username"] = Email

                return redirect(url_for("index"))
            else:
                flash("Kullanıcı adınız ve şifreniz eşlemiyor!","danger")
                return render_template("login.html",form=form)
        else:
            flash("Bu E-Mail ile ilgili kayıt bulunmuyor!","warning") 
            return render_template("login.html",form=form)  
             
    return render_template("login.html",form=form)

# Çıkış İşlemi
@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for("index"))

# Kontrol Paneli Sayfası
@app.route('/dashboard')
@login_required
def dashboard():
   return render_template("dashboard.html")

# Veri Ekleme Sayfası
@app.route('/adddata',methods=["GET","POST"])
@login_required
def adddata():
    form = VeriEkleme(request.form)

    Baslik = form.Baslik.data
    Kullanici = session["username"]
    Kh = form.Kh.data
    Alkalinity = form.Alkalinity.data
    Ca = form.Ca.data
    Mg = form.Mg.data
    Fosfat = form.Fosfat.data
    NO3 = form.NO3.data
    PH = form.PH.data

    if request.method == "POST" and form.validate():
        cursor = mysql.connection.cursor()
        sorgu = "insert into Inputs (Baslik,Kullanici,Kh,Alkalinity,Ca,Mg,Fosfat,NO3,PH) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sorgu,(Baslik,Kullanici,Kh,Alkalinity,Ca,Mg,Fosfat,NO3,PH))
        mysql.connection.commit()
        cursor.close()
        flash("Veriler Kaydedildi.","success")
        return redirect(url_for("adddata"))

    return render_template("adddata.html",form = form)

# Verileri Listele
@app.route('/alldata')
def alldata():
    cursor = mysql.connection.cursor()
    sorgu = "select * from Inputs"
    result = cursor.execute(sorgu)

    if result > 0:
        data = cursor.fetchall()
        return render_template("alldata.html",veri=data)
    else: 
        flash("Henüz kayıt eklenmemiş!","warning")   
        return render_template("alldata.html")

# Veri Detay Sayfası
@app.route('/alldata/<string:ID>')
def data(ID):
    cursor = mysql.connection.cursor()
    sorgu = "select * from Inputs where ID = %s"
    result = cursor.execute(sorgu,(ID,))

    if result > 0:
        data = cursor.fetchone()
        return render_template("data.html",veri=data)  
    else:
        return render_template("data.html")     

@app.route('/graphic')
def graphic():
    cursor = mysql.connection.cursor()
    sorgu = "select * from Inputs"
    result = cursor.execute(sorgu)
    if result > 0:
        data = cursor.fetchall()
        return render_template('graphic.html', values=data)
    """legend = 'Temperatures'
    temperatures = [100, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
             '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
             '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
    return render_template('graphic.html', values=temperatures, labels=times, legend=legend)"""


if __name__ == "__main__":
    app.run(debug=True)