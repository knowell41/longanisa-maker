sudo mv sausageparty.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable sausageparty
sudo systemctl start sausageparty
