#!/bin/bash

#挂载windows的e盘

if [ 'df -h | grep /media/root/文档' ]; then
	mount  -t ntfs /dev/sda5 /media/root/e
	ln -s /media/root/e/linux /root/桌面/linux 
	
else
	ln -s /media/root/文档/linux /root/桌面/linux
fi
