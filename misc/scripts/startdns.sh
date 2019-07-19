echo "nameserver 172.16.68.75" > /etc/resolv.conf
echo "nameserver 1.1.1.1" >> /etc/resolv.conf
sudo systemctl enable systemd-resolved.service
sudo systemctl start systemd-resolved
