from flask import Flask , request, render_template 
app = Flask(__name__)
@app.route('/',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/success',methods=['GET','POST'])
def success():
    if request.method=='POST':
        return render_template('register.html')
    else:
        return render_template('success.html')
if __name__ == '__main__':
    app.run()
    app.debug= True

