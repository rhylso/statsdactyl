# 📊 | StatsDactyl
[![donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/rhylso/donate)
[![license](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge)](./LICENSE)
[![license](https://img.shields.io/badge/latest-V0.1.1-green?style=for-the-badge)](https://github.com/rhylso/statsdactyl/releases)

- Display the Statistics of your Pterodactyl Panel.

## 👀 | Overview
![image](https://media.discordapp.net/attachments/1028963752588083243/1090263547264635011/image.png?width=1246&height=701)

---

## 💿 | Supported OS
- You can run StatsDactyl as long as the dependencies are installed and can be ran.
- Here's the list of Operating System's that we tried to run and it perfectly works.

| Operating System      | Support |
| ----------- | ----------- |
| Ubuntu 22.04      | ✅       |

## 🔗 | Dependencies
- Python
- Pip
- Nginx

## 💻 | Installation
<br>

> ### Installing dependencies
```bash
sudo apt install python3 python3-pip nginx certbot python3-certbot-nginx
```

<br>

> ### Downloading files
```bash
mkdir /var/www/statsdactyl
cd /var/www/statsdactyl
curl -Lo statsdactyl.tar.gz https://github.com/rhylso/statsdactyl/releases/latest/download/statsdactyl.tar.gz
tar -xzvf statsdactyl.tar.gz
```

<br>

> ### StatsDactyl Configuration
- Edit the `.env` file using nano.
```bash
nano .env
```
> `.env`
```yml
TITLE = "StatsDactyl"
ALERT = "This site shows the statistics of our Panel."

PANEL_URL = "your_panel_url"
APPLICATION_API_KEY = "you_api_key"
```

<br>

> ### Installing pip packages
```bash
pip install -r requirements.txt
```

> ### Worker
- Create a `statsdactyl.service` in `/etc/systemd/system`

> `statsdactyl.service`
```yml
[Unit]
Description=Statsdactyl Service
After=multi-user.target

[Service]
Type=simple
Restart=always
WorkingDirectory=/var/www/statsdactyl
Environment="PATH=/var/www/statsdactyl/statsdactylenv/bin"
ExecStart=/usr/bin/python3 /var/www/statsdactyl/app.py

[Install]
WantedBy=multi-user.target
```
- After that, run the following command.
```bash
sudo systemctl start statsdactyl.service
```

<br>

> ### Adding SSL
- Run the following command.
```bash
sudo certbot --nginx -d <domain>
```

<br>

> ### Webserver configuration
- Create a `statsdactyl.conf` in `/etc/nginx/sites-available`

> `statsdactyl.conf`
```yml
server {
    listen 80;
    server_name <domain>;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name <domain>;

    ssl_certificate          /etc/letsencrypt/live/<domain>/fullchain.pem;
    ssl_certificate_key      /etc/letsencrypt/live/<domain>/privkey.pem;
    ssl_trusted_certificate  /etc/letsencrypt/live/<domain>/chain.pem;

    location / {
        proxy_set_header   X-Forwarded-For $remote_addr;
        proxy_set_header   Host $http_host;
        proxy_pass         http://0.0.0.0:5000;
    }
}
```
- After that, run the following command.
```bash
sudo ln -s /etc/nginx/sites-available/statsdactyl.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

<br>

---
- Congratulations 🥳! You have successfully installed StatsDactyl. You can now access StatsDactyl to the domain you specified.

## ⚒️ | Contributing
- Your contributions are welcome and will help me to make StatsDactyl better.
```
git clone https://github.com/rhylso/statsdactyl.git
cd server
pip install -r requirements.txt
python main.py
cd client
npm install
npm run dev

# And finally, made some changes and create a pull request.
```

## 🤝 | Donate
- [Liberapay](https://liberapay.com/rhylso/donate)
Any amount will be greatly appreciated, this will help me to pay my expenses and keep the development alive. 🙂

## 🪪 | License
- This project is distributed under the [MIT License](LICENSE)

> StatsDactyl 2023 - made with ❤️ by [rhylso](https://github.com/rhylso)