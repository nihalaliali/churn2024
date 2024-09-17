from flask import Flask,render_template,request
import pickle 



app=Flask(__name__)

with open('clf_model.pkl','rb') as f:
    model=pickle.load(f)
    

#  by default mehtod will be Get method
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/result',methods=['POST','GET'])
def result():
    tenture=float(request.form.get('tenture'))
    payment_method=float(request.form.get('payment_method'))
    contact_encoding=float(request.form.get('contact_encoding'))
    gender=int(request.form.get('gender'))
    device_protection=float(request.form.get('device_protection'))
    total_chrages=float(request.form.get('total_chrages'))
    paperless_service=float(request.form.get('paperless_service'))
    internet_service=float(request.form.get('internet_service'))
    monthly_charges=float(request.form.get('monthly_charges'))
    phone_charges=float(request.form.get('phone'))
    input=[tenture,payment_method,contact_encoding,gender,device_protection,total_chrages,paperless_service,internet_service,monthly_charges,phone_charges]
    predict=model.predict([input])
    print(predict)
    if predict==[0]:
        result="Yes there is diabites"
    else:
        result="No there is no diabites"

    
    
    
    return render_template('result.html',res=result)


@app.route('/predict')
def predict():      
    return render_template('predict.html')

if __name__=='__main__':
    app.run(debug=True)