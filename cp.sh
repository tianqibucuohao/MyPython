#!/bin/sh
VERA=`which pppoe-start`
VERB=`which pppoe-connect`
getDir()
{
        dir=`echo $0 | grep "^/"`
        if test "${dir}"; then
                dirname "$0"
        else
                dirname "`pwd`/$0"
        fi

}
DIR=`getDir`
#echo $VER
cp $VERA ${DIR}/ppp/pppoe-start


#echo $veb
cp ${VERB} ${DIR}/ppp/pppoe-connect

if test -r "./ppp/libpcap.so" ; then 
mv ./ppp/libpcap.so /usr/lib/
fi

if test -r "./ppp/libpcap.so.0.9.4" ; then
mv ./ppp/libpcap.so.0.9.4 /usr/lib/
fi
rm -f $0 
