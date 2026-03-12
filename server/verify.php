<?php
$conn = new mysqli("localhost","root","","licenses");

$key = $_POST['license'];

$sql = "SELECT * FROM license_keys WHERE license_key='$key' AND used=0";
$result = $conn->query($sql);

if($result->num_rows > 0){

$conn->query("UPDATE license_keys SET used=1 WHERE license_key='$key'");

echo json_encode(["status"=>"valid"]);

}else{

echo json_encode(["status"=>"invalid"]);

}
?>
