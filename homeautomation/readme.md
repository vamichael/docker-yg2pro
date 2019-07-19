In order to use the external database with home assistant, you need to create a databae and user.

You need to run a sql script in the container.  To enter the container, use:

    docker exec -it mariadb /bin/bash
    
And the following script to create the db and user:

    config/runme.sh
    
(Optionsl) you can enter the sql console with:

    mysql -u root -p${MYSQL_ROOT_PASSWORD}
