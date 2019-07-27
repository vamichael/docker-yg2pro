PIHOLE_IP=$(docker inspect --format '{{ .NetworkSettings.Networks.docker_pihole_sub.IPAddress }}' $(docker ps -aqf "name=pihole"))
VPN_CLIENT_NAME="suttondr.net"

#init OpenVPN
docker run -v ${USERDIR}/docker/openvpn:/etc/openvpn --log-driver=none --rm kylemanna/openvpn ovpn_genconfig -u udp://vpn.${VPN_CLIENT_NAME} -n ${PIHOLE_IP}
docker run -v ${USERDIR}/docker/openvpn:/etc/openvpn --log-driver=none --rm -it kylemanna/openvpn ovpn_initpki


#### MAKE SURE OpenVPN serivce from docker-compose.yml is running!!!

#Generate a client certificate without a passphrase
docker run -v ${USERDIR}/docker/openvpn:/etc/openvpn --log-driver=none --rm -it kylemanna/openvpn easyrsa build-client-full ${VPN_CLIENT_NAME} nopass

#Retrieve the client configuration with embedded certificates
docker run -v ${USERDIR}/docker/openvpn:/etc/openvpn --log-driver=none --rm kylemanna/openvpn ovpn_getclient ${VPN_CLIENT_NAME} > ${VPN_CLIENT_NAME}.ovpn

