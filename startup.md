mongodb启动

nohup /usr/local/mongodb/bin/mongod --dbpath=/usr/local/mongodb/data &


node 版本检测，需要用 v6.15.0

nvm use v6.15.0


再启动clickhouseclub
在clickhouseclub目录执行：

nohup node app.js &
