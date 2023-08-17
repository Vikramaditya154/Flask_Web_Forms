from flask import Flask,render_template,request

from flask_wtf import Form

from wtforms import StringField,SubmitField,IntegerField

from wtforms.validators import DataRequired

app=Flask(__name__)

# create a Web_Forms or django_forms 

# creating Django Forms in flask we import  Forms in "flask_wtf"  
       # from  flask_wtf import Form

# inside a flask we can use wtforms Field

# in flask we import validators in datarequired

class NameForm(Form):
    name=StringField()
    age=IntegerField()
    submit=SubmitField()

@app.route('/web_forms',methods=['GET','POST'])
def flask_web_form():
    form=NameForm()
    if request.method=='POST':
        FWF=NameForm(request.form)
        if FWF.validate():
            return FWF.data



    return render_template('Web_Forms.html',form=form)





if __name__=='__main__':
    app.run(debug=True)