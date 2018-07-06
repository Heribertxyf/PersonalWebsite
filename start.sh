#!/usr/bin/env bash

start_()
{
    cd $(pwd);
    nohup gunicorn prada.wsgi:application -b 0.0.0.0:8005 -t 60  -w 2  > /dev/null 2>&1 &
}


stop_()
{
    ps ax | grep 'gunicorn prada.wsgi:application' | grep -v 'grep' | sed 's/^\s*//g' | cut -d ' ' -f 1 | xargs -I{} kill {}
}

restart()
{
    stop_
    start_
}

help_()
{
    echo ''
    echo 'usage:'
    echo '      ./start.sh            start the program'
    echo '      ./start.sh stop       stop the program'
    echo '      ./start.sh restart    restart the program'
    echo ''
}

main()
{
    argu=$1
    if [ "$argu" = "start" ]||[ "$argu" = "" ]; then
        start_
    elif [ "$argu" = "stop" ]; then
        stop_
    elif [ "$argu" = "restart" ]; then
        restart
    else
        help_
    fi
}

main $1
