#What happens when you type https://google.com into a browser?

the user enters the url in the browser then browser performs DNS Lookup to translate the domain name into IP adreess then browser establishes the connection using TCP and then sends the HTTPS request contains the http method,path, HTTPS headers,and optinnaly body. The server recives the request and performs the required bussness logic,database operations,and generated the HTTPS Response.

The responce contains status code, https headers and respoce body the brower receives the responce and parces the HTML, downlpads refencing css and javascript and constructs the page and renders it to users.

