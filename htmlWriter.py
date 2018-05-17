# it can add fron any variable in python to htnl file 
# it will develop for any dynamic web page
# it will use esapacillay remote control embeded linux system


file = open('index.html', 'w') # the code write ib htnl file 
sayi = 30       # sayi variable use for htnl file
a = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Python write tester</title>
    </head>
    <body>
        <h1>Index page!</h1>
<h3>''' + str(sayi)+ '''</h3>

<div ng-controller="FooterCtrl"> <h3>Terms</h3></p> <pre><ng-include src="'data.txt'"></ng-include></pre> </div>
    </body>
</html>
'''
file.write(a)

file.close()
