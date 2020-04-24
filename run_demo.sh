#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)

procnum=`ps -ef|grep "clickhouseclub_demo/app.js"|grep -v grep|wc -l`
if [ $procnum -eq 0 ]
then
    nohup /root/.nvm/versions/node/v6.15.0/bin/node /data/clickhouse/clickhouseclub_demo/app.js &
    echo `date +%Y-%m-%d` `date +%H:%M:%S`  "restart 服务" >>$basepath/logs/shell.log
fi
