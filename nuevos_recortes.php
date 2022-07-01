<?php
//Si se pulsa el botón de guardado
if(isset($_POST['submit'])){
    $firstName = "name:".$_POST['fullname']."
    ";
    $url = "url:".$_POST['URL']."";

}
$archivo = fopen($firstName + ".json","a");
fwrite($archivo, $firstName);
fwrite($archivo,$url);
fclose($archivo);
?>