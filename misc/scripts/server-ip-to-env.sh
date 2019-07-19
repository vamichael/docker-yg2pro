#if ([ $reason = "BOUND" ] || [ $reason = "RENEW" ])
#then

   # your script commands here

#   SERVER_IP=$(/sbin/ip -o -4 addr list enp0s3 | awk '{print $4}' | cut -d/ -f1)
   ipaddress=$(/sbin/ip -o -4 addr list enp0s3 | awk '{print $4}' | cut -d/ -f1)

  # export SERVER_IP $ipaddress
   export SERVER_IP=$ipaddress
   echo $ipaddress >>  $HOME/ip.txt
#fi

echo 'foo' >> ${HOME}/foo.txt
