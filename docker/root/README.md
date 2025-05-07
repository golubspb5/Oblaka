# Docker IoT Practice

## Задание
Развернуть систему передачи, хранения и визуализации данных от симуляторов датчиков через Docker-контейнеры.

## Структура репозитория
```
- assets/
- vms/
  - client/simulator
  - gateway/mosquitto
  - server/
- report.md
```

## Инструкция
1. Перейти в папку vms/server.
2. Запустить:
```
docker-compose up --build
```
3. Открыть Grafana: http://localhost:3000 (admin/admin).

## Описание
- 6 симуляторов датчиков публикуют данные в MQTT.
- Mosquitto принимает сообщения.
- Telegraf сохраняет в InfluxDB.
- Grafana отображает данные в реальном времени.

## Контейнеры
- Simulator Sensors
- Mosquitto Broker
- InfluxDB
- Telegraf
- Grafana

