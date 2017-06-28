# DataComm-HTTPProxyServer
*************************************************************************************************************************************************************
AUTHOR:
*************************************************************************************************************************************************************
NAME      : Gaurav Diwate
Occupation: Student at ITP department at University of Colorado Boulder.
SID       : 105755934
IDENTIKEY : gadi5945
Contact   : Email  :  Gaurav.Diwate@coorado.edu
            Phone  :  720-345-1611
************************************************************************************************************************************************************

WELCOME!
                   
DATA COMMUNICATIONS I PROGRAMMINIG ASSIGNMENT 3 TO BUILD A WEB PROXY SERVER:

SOFTWARE VERSION :Python 2.7.10

***********************************************************************************************************************************************************
PROGRAMM FEATURES:
***********************************************************************************************************************************************************
     
1. Program builds a proxy server which handles client requests to access host server and returns data to the client. 

2. CONTENT FILTERING: Proxy server enables us to block any URL if malicious.

3. PRIVACY: Proxy server assures some privacy as client gets information of proxy but not of the actual server accessed.

4. CACHING AND TIMEOUT: Proxy server calculates SHA of requested URL and saves for a timeout value of 2 minutes. If the same URL is requested again, then
            proxy matches the sha and returns the data to the client which has been already saved into Directory. After 2 minutes the CACHE is 
            removed.  
5. THREADING: In order to handle multiple requests at the same time from multiple clients, threading is implementd in proxy server. Threading accepts a 
            function and arguments to handle the overall operation/functioning which enables proxy server to handle multiple requests at the same time.

6. SELECT MODULE: The file consists of another program file whhich is implemented with SELECT MODULE to handle multiple requests from multiple clients at 
            the same time.   
  
***********************************************************************************************************************************************************

