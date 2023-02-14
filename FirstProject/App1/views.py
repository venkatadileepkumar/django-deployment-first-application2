from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    print("welcome/ is requested and display() is executed successfully");
    ss='''
        <center>
            <h1 style="color:blue;">
                Hi DILEEP...!!This is "FirstProject-App1"
            </h1>
            <hr color="brown" size="5" width="50%"/>
        </center>
        ''';
    return HttpResponse(ss);
    
def show(request):
    print("welcome2/ is requested and display() is executed successfully");
    ss='''
    <!--
        HTML Webpage to display "welcome" message
    -->
            <html>
                <head>
                    <title>***Welcome-Page***</title>
                    <style>
			h1{
				color:blue;
			}
			h2{
				color:green;
			}
			h3{
				color:orange;
			}
			h4{
				color:black;
			}
			h5{
				color:red;
			}
			h6{
				color:purple;
			}
			h1,h3,h5{
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:cyan;
			}
                    </style>
                </head>
                <body>
                <center>
                        <h1>***Welcome to Django HTML-Webpage***</h1>
                            <hr color="brown" width="95%"/>
                        <h2>Welcome to Django HTML-Webpage</h2>
                            <hr color="brown" width="85%"/>
                        <h3>Welcome to Django HTML-Webpage</h3>
                            <hr color="brown" width="75%"/>
                        <h4>Welcome to Django HTML-Webpage</h4>
                            <hr color="brown" width="65%"/>
                        <h5>Welcome to Django HTML-Webpage</h5>
                            <hr color="brown" width="55%"/>
                        <h6>Welcome to Django HTML-Webpage</h6>
                            <hr color="brown" width="45%"/>	
                </center> 
                </body>
            </html>
    ''';
    return HttpResponse(ss);
def hello(request):
    print("hello/ is requested and hello() is executed successfully")
    ss='''
        <html>
            <head>
                <title>
                </title>
                <style>
                    h1{
                        color:black;
                        width:90%;
                      }
                    h2{
                        color:green;
                        width:80%;
                      }
                    h3{
                        color:red;
                        width:70%;
                      }
                    h1,h2,h3{
                                background-color:lightblue;
                                border:2px dashed brown;
                            }
                </style>
            </head>
            <body>
                <center>
                    <h1>Hello User...!!!</h1>
                        <hr color='brown' width='80%'/>
                    <h2>Welcome to DJango-App...!!</h2>
                        <hr color='red' width='60%'/>
                    <h3>Have a Nice Day...!</h3>
                        <hr color='cyan' width='40%'/>
                </center>
            </body>
        </html>
       ''';
    return HttpResponse(ss);
import time;
def senddatetime(request):
    print("dtime/ is requested and senddatetime() is executed");
    ct=time.ctime()
    print("Date & Time::",ct);
    ss='''
            <html>
                <head>
                    <title>Date & Time Webpage</title>
                    <style>
                        h1{
                            color:violet;
                            width:75%
                        }
                        h2{
                            color:lightblue;
                            width:65%
                        }
                        h3{
                            color:brown;
                            width:55%
                        }
                    </style>
                <body>
                    <center>
                        <h1>***Welcome to Django-User***</h1>
                            <hr color='brown width='80%'/>
                        <h2>Server Date & Time ::</h2>
                            <hr color='brown width='70%'/>
                        <h3>''',ct,'''</h3>
                            <hr color='brown width='60%'/>
                    </center>
                </body>
                </head>
            </html>
       '''
    return HttpResponse(ss);
def demo(request):
    print("Multiple-Requests-URLs are same response");
    Htmldata='''
            <center>
                <h1>Welcome Demo User...!!!</h1>
                    <hr/>
                <h2>This is same output for Multiple-Requests-URLs</h2>
                    <hr/>
                <h3>Have A Great Day..</h3>
                    <hr/>    
            </center>''';
    return HttpResponse(Htmldata);
def homepage(request):
    Htmldata='''
        <center>
            <h1>Welcome to Default Home-page</h1>
                <hr/>
            <h1>Your Request Page is NOT found</h1>
                <hr/>
            <h1>Please try other URLs or Links</h1>   
        </center>''';
    return HttpResponse(Htmldata);