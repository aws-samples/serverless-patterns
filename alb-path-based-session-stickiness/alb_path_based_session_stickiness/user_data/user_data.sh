#!/bin/bash
dnf update -y --security
dnf install -y httpd
cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cookies and Hostname</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
        ul {
            background-color: #fff;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>Cookies and Hostname Information</h1>
    <h2>Cookies:</h2>
    <ul id="cookieList"></ul>
    <h2>Hostname:</h2>
    <p id="hostname"></p>

    <script>
        // Function to get and display cookies
        function displayCookies() {
            const cookieList = document.getElementById('cookieList');
            const cookies = document.cookie.split(';');
            
            if (cookies.length === 1 && cookies[0] === "") {
                cookieList.innerHTML = "<li>No cookies found</li>";
            } else {
                cookies.forEach(cookie => {
                    const li = document.createElement('li');
                    li.textContent = cookie.trim();
                    cookieList.appendChild(li);
                });
            }
        }

        // Function to get and display hostname
        function displayHostname() {
            const hostnameElement = document.getElementById('hostname');
            hostnameElement.textContent = $(hostname);
        }

        // Call the functions when the page loads
        window.onload = function() {
            displayCookies();
            displayHostname();
        };
    </script>
</body>
</html>
EOF
cat <<EOF > /etc/httpd/conf.d/rewrite.conf
<Directory /var/www/html>
    ReWriteEngine On
    ReWriteRule ^ index.html [L]
</Directory>
EOF

systemctl start httpd
systemctl enable httpd