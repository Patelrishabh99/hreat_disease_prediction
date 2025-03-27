<?php  
session_start();
include("connect.php");
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
            background-color:black;
        }
        p{
            color:white;
        }
        h1{
            color:white;
        }
        a{
            color:blue;
            font-size:20px;
        }
    </style>
</head>
<body >
    <div style="text-align:center; padding:15px; background-colour:black;">
        <p class="p" style="font-size:50px; font-weight:bold;">
            Hello 
        </p>

        <br>
        <h1>Welcome to Heart Disease Prediction</h1>
        <br>
        <br>
        <br>
        <br>
        <button onclick="window.location.href='templates/index.html';">continue</button>


        <br>
        <br>
        <br>
        <br>
        <br>


        <a href="logout.php">Log out</a>
        


    </div>
</body>
</html>