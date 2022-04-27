# 使用小米运动修改微信/支付宝步数
## 无需下载小米运动即可完成小米运动注册绑定二维码和重置密码
## 安装：
### 前端
  1.下载xiaomi文件将前端上传到网站目录

  2.修改function.js里的url 反向代理的哪个网站就填哪个网站
### 后端
  1.将后端上传到服务器
  
  2.安装python所需库 requests Flask gunicorn
  
  3.cd到项目目录
  
  4.启动gunicorn -w 3 -b 0.0.0.0:5200 xiaomiWeb:app
 
  5.配置Nginx反向代理域名到http://127.0.0.1:5200
 
 注意：反向代理域名不能和前端访问域名相同所以需要两个域名一个当接口一个当网站访问域名
 
 ### 演示
  https://www.vhapi.com/xiaomi/
