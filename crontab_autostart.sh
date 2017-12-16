#!/usr/bin/env bash

basepath=$(cd `dirname $0`; pwd)

    procnum=`ps -ef|grep "clickhouseclub/app.js"|grep -v grep|wc -l`
    if [ $procnum -eq 0 ]
    then
        nohup /usr/bin/node /data/clickhouse/github/clickhouseclub/app.js &
        echo `date +%Y-%m-%d` `date +%H:%M:%S`  "restart 服务" >>$basepath/logs/shell.log
    fi
    sleep 20