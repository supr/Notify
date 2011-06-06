<html>
	<head>
		<title> publisher for ${uid} </title>
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js"></script>
		<script src="http://cdn.socket.io/stable/socket.io.js"></script>
	</head>
	<body>
		<h1>Publisher page for ${uid} </h1>
		<script>
		<!--
			var uid = "${uid}";
			var socket = null;
			$(document).ready(function() {
				socket = new io.Socket(null, {});
				socket.on('connect', function() {
					console.log("Connected!");
					socket.send({type: "connect", uid: uid});
				});
				socket.on('message', function(obj) {
					console.log("Message", JSON.stringify(obj))
					if(obj.type == "chat") {
						$("#chat_box").append(obj.data + "<br/>");
					}
				});
				socket.connect();

				$("#webmsg").submit(function() {
					socket.send({type: "chat", data: $("input:first").val(), uid: uid});
					console.log("Submit Clicked!");
					return false;
				});
			});
		//-->
		</script>
		<div id="chat_box" style="width:400px;height:200px;"></div>
		<form id="webmsg">
			<input type="text" name="msg"/>
			<input type="submit"/>
		</form>
	</body>
</html>