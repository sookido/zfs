PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin

0 10 * * * zpool status -x | grep 'all pools are healthy' || (zpool status | python3 /root/sendmail.py)
0 0 1 * * zpool scrub tank
