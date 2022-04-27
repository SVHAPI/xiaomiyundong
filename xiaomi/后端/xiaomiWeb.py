from flask import Flask
from flask import *
from api import login,user,ttl,register,createwxqr,captcha,reset
app = Flask(__name__)
# 17378813797
headers = {'Access-Control-Allow-Origin': '*'}

@app.route('/ttl',methods=["POST"])
def url_ttl():
   phone = request.form.__contains__('phone')
   password = request.form.__contains__('password')
   tt = request.form.__contains__('ttl')
   if phone == True and password == True and tt == True:
      if request.form['phone'] and request.form['password'] and request.form['ttl']:
         try:
            access = login.main(request.form['phone'],request.form['password'])
            if access == False:
               return jsonify({'code':0,'msg':'密码错误'}),headers
            data = user.main(access)
            print('步数:' + str(request.form['ttl']))
            ttl.main(request.form['ttl'],data['app_token'],data['user_id'])
            return jsonify({'code':1,'msg':'ok'}),headers
         except:
            return jsonify({'code':0,'msg':'参数错误'}),headers
      else:
         return jsonify({'code':0,'msg':'参数没有值'}),headers
   else:
       return jsonify({'code':0,'msg':'参数错误'}),headers
# 提交小米运动步数

@app.route('/captcha',methods=["POST"])
def url_captcha():
   phone = request.form.__contains__('phone')
   if phone == True:
      if request.form['phone']:
         try:
            msg = captcha.main(request.form['phone'])
            return jsonify({'code':1,'msg':msg}),headers
         except:
            return jsonify({'code':0,'msg':'参数错误'}),headers
      else:
         return jsonify({'code':0,'msg':'参数没有值'}),headers
   else:
       return jsonify({'code':0,'msg':'参数错误'}),headers
# 获取小米运动注册验证码

@app.route('/register',methods=["POST"])
def url_register():
   phone = request.form.__contains__('phone')
   password = request.form.__contains__('password')
   code = request.form.__contains__('code')
   if phone == True and password == True and code == True:
      if request.form['phone'] and request.form['password'] and request.form['code']:
         try:
            register.main(request.form['code'],request.form['phone'],request.form['password'])
            access = login.main(request.form['phone'],request.form['password'])
            data = user.main(access)
            url = createwxqr.main(data['app_token'],data['thirdparty_info']['third_id'],data['user_id'])
            return jsonify({'code':1,'msg':'注册成功','url': url}),headers
         except:
            return jsonify({'code':0,'msg':'参数错误'}),headers
      else:
         return jsonify({'code':0,'msg':'参数没有值'}),headers
   else:
       return jsonify({'code':0,'msg':'参数错误'}),headers
# 注册小米账号

@app.route('/createwxqr',methods=["POST"])
def url_createwxqr():
   phone = request.form.__contains__('phone')
   password = request.form.__contains__('password')
   if phone == True and password == True:
      if request.form['phone'] and request.form['password']:
         try:
            access = login.main(request.form['phone'],request.form['password'])
            if access == False:
               return jsonify({'code':0,'msg':'密码错误'}),headers
            data = user.main(access)
            url = createwxqr.main(data['app_token'],data['thirdparty_info']['third_id'],data['user_id'])
            return jsonify({'code':1,'url':url}),headers
         except:
            return jsonify({'code':0,'msg':'参数错误'}),headers
      else:
         return jsonify({'code':0,'msg':'参数没有值'}),headers
   else:
       return jsonify({'code':0,'msg':'参数错误'}),headers
# 获取小米运动微信绑定二维码

@app.route('/reset',methods=["POST"])
def url_reset():
   phone = request.form.__contains__('phone')
   if phone == True:
      if request.form['phone']:
         try:
            code = request.form.__contains__('code')
            password = request.form.__contains__('password')
            if code and password:
               if request.form['code'] and request.form['password']:
                  msg = reset.main(request.form['phone'],request.form['password'],request.form['code'])
                  return jsonify({'code':1,'msg':msg}),headers
            msg = reset.main(request.form['phone'],None,None)
            return jsonify({'code':1,'msg':msg}),headers
         except:
            return jsonify({'code':0,'msg':'参数错误'}),headers
      else:
         return jsonify({'code':0,'msg':'参数没有值'}),headers
   else:
       return jsonify({'code':0,'msg':'参数错误'}),headers
# 重置小米运动密码

if __name__ == '__main__':
   app.run(debug = True)    