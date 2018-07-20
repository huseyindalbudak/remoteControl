<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>veriCekme</title>
</head>
<body>
 <!-----------------------php----------------------->   
<?php

// it can take any type of data according to html type in a website
// and the data transfer the JavaScript via innerHTML

$veri = file_get_contents("http://bigpara.hurriyet.com.tr/viop-varant/canli-varant-verileri");

//preg_match_all() is special php function
preg_match_all('@ <li class="cell048 node-c" id="h_td_fiyat_id_UZIGGV">(.*?)</li>@si',$veri,$baslik);

// $baslik variable is array 
echo $baslik[0][0];
echo "<br>" ;  //for next line in html
echo var_dump($baslik[0][0]);  // output data type via php function
?>
 <!----------------------end-of-php----------------------->   
    
    
<p id="demom">test</p>
    
    

 <!-----------------------JavaScript----------------------->   
    
<script>
var text = document.getElementById("h_td_fiyat_id_UZIGGV").innerHTML;
alert(text);
//text variable can use for any operation but data type that can converte is important 
</script>
 <!-----------------------JavaScript----------------------->   


</body>
