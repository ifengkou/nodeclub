#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)

procnum=`ps -ef|grep "clickhouseclub/app.js"|grep -v grep|wc -l`
if [ $procnum -eq 0 ]
then
    nohup /root/.nvm/versions/node/v8.12.0/bin/node /data/clickhouse/clickhouseclub/app.js &
    echo `date +%Y-%m-%d` `date +%H:%M:%S`  "restart 服务" >>$basepath/logs/shell.log
fi
