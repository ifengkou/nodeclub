## Github 注册失败

在通过Github 授权后，有两个选项，一个是注册新账号，一个是关联旧账号

如果注册新账号，但是Github 获取用户信息时，不能获取到邮箱，或者邮箱之前已经被创建，那么就会提示 状态码为500异常的页面（正常网站页面），
但是之前Nginx 对官网和clickhouse 做了统一的异常拦截，如果是500状态的，统一拦截到 维护中的页面，所以正确的业务异常提示未能展现给用户

nginx 当时的设置如下：  
```
        proxy_intercept_errors on;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
                root   html;
        }
        location = /xitongweihu.png {
                root   html;
        }
```

如果提示邮箱不存在，则提示让客户 在github 中，将邮箱开放出来，具体为 头像-> setting -> profile -> public email -> 选择邮箱 -> 下方 update profile
如果邮箱已存在，那么提示客户邮箱冲突，可以试试绑定旧账号

解决方案：关闭Nginx 统一异常拦截