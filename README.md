# zfs
centos8
```sh
sed -i -e "s/^SELINUX=enforcing$/SELINUX=disabled/g" /etc/selinux/config
systemctl stop firewalld
systemctl disable firewalld 

yum update -y
yum install http://download.zfsonlinux.org/epel/zfs-release.el8_3.noarch.rpm
yum install epel-release
yum install zfs

reboot
zpool import tank2
```
