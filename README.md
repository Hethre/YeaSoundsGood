YeaSoundsGood
=============

A team from SheHacks Sydney

Running Application Locally
===========================

On Mac:

Download Tomcat: http://apache.mirror.serversaustralia.com.au/tomcat/tomcat-7/v7.0.52/bin/apache-tomcat-7.0.52.tar.gz
Unzip file

Run the following commands:

sudo mkdir -p /usr/local 
sudo mv ~/[location_of_tomcat_folder]/apache-tomcat-7.0.52 /usr/local 
sudo rm -f /Library/Tomcat     
udo ln -s /usr/local/apache-tomcat-7.0.52 /Library/Tomcat
sudo chmod +x /Library/Tomcat/bin/*.sh

Configure Tomcat on your IDE to use the Tomcat application server found in /Library/Tomcat and the war file from your project.


