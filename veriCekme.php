<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>veriCekme</title>
</head>
<body>
<?php

// it can take any type of data according to html type in a website
// and the data transfer the JavaScript via innerHTML

$veri = file_get_contents("http://bigpara.hurriyet.com.tr/viop-varant/canli-varant-verileri");

//echo strip_tags($veri);
preg_match_all('@ <li class="cell048 node-c" id="h_td_fiyat_id_UZIGGV">(.*?)</li>@si',$veri,$baslik);
//preg_match_all('@<span id="priceblock_ourprice" class="a-size-medium a-color-price">(.*?)</span>@si',$veri,$ucret);

//print_r($baslik);
$veri= $baslik[0][0];
echo $veri  ;
echo "\n"; // bir sonraki satir icin
echo "<br>" ;
echo var_dump($baslik[0][0]);
//echo $ucret[0][0];
?>
<p id="demom">test</p>

<script>
var text = document.getElementById("h_td_fiyat_id_UZIGGV").innerHTML;
alert(text);
</script>

</body>
