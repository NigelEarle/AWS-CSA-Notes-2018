<?php 
$username = "acloudguru"; 
$password = "acloudguru"; 
$hostname = "yourhostnameaddress"; 
$dbname = "acloudguru";

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) or die("Unable to connect to MySQL"); 
echo "Connected to MySQL using username - $username, password - $password, host - $hostname<br>"; 
$selected = mysql_select_db("$dbname",$dbhandle)   or die("Unable to connect to MySQL DB - check the database name and try again."); 
?>