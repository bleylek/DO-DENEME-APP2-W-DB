#!/bin/bash
# Sunucuda bu scripti çalıştırın: debug.sh

echo "=== CONTAINER DURUMU ==="
docker ps

echo -e "\n=== APP2 CONTAINER LOGS ==="
docker logs app2

echo -e "\n=== PORT KONTROLÜ ==="
netstat -tulpn | grep :5002

echo -e "\n=== FIREWALL DURUMU ==="
sudo ufw status

echo -e "\n=== DOCKER NETWORK ==="
docker network ls