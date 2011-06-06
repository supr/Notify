<html>
	<head>
		<title> Register </title>
	</head>
	<body>
		<form method="POST" action="${request.route_path('subscribe')}">
		<input type="text" name="handle"/>
		<input type="submit" value="Register"/>
		</form>
	</body>
</html>