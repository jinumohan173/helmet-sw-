<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="refresh" content="3">
<style>
.item1 { grid-area: header; }
.item2 { grid-area: menu; }
.item3 { grid-area: main; }
.item4 { grid-area: right; }
.item5 { grid-area: footer; }
.grid-container {
  display: grid;
  grid-template-areas:
    'header header header header header header'
    'menu main main main right right'
    'menu footer footer footer footer footer';
  grid-gap: 10px;
  background-color: #2196F3;
  padding: 10px;
}
.grid-container > div {
  background-color: yellow;
  text-align: center;
  padding: 20px 0;
  font-size: 30px;
}
h1{text-align: center;
	text-shadow: 3px 2px red;}
</style>
</head>
<body>

<h1>ATM THEFT DETECTION </h1>


<p>The person who entered with helmet </p>

<div class="grid-container">
  <div class="item1"><img src="image2.jpg" alt="Mountain View" width="250" height="200">
  
 
 </div>


</body>
</html>
