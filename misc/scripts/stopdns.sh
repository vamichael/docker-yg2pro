rm /etc/resolv.conf
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved

