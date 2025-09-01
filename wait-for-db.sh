#!/bin/bash
# filepath: /bonpreu-data-engineer-demo/wait-for-db.sh

set -e

host="$1"
port="$2"

echo "Esperando a MySQL en $host:$port..."
while ! nc -z "$host" "$port"; do
  sleep 2
done

echo "MySQL disponible en $host:$port. Ejecutando ETL..."
exec "${@:3}"