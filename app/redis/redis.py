import os
import logging
import redis
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class RedisClient:
    def __init__(self):
        self.host = os.getenv("REDIS_HOST", 'localhost')
        self.port = int(os.getenv("REDIS_PORT", 6379))
        self.db = int(os.getenv("REDIS_DB", 0))
        self.redis_conn = None

    def connect(self):
        try:
            self.redis_conn = redis.Redis(host=self.host, port=self.port, db=self.db)
            self.redis_conn.ping()  # Проверка подключения
            logging.info(f"Успешное подключение к Redis на {self.host}:{self.port}, база данных {self.db}.")
        except Exception as e:
            logging.error(f"Ошибка при подключении к Redis: {e}")
            self.redis_conn = None

    def push_data(self, key, value):
        if self.redis_conn:
            if key is None or value is None:
                logging.error(f"Ошибка: ключ или значение не могут быть None (ключ: {key}, значение: {value})")
                return

            try:
                result = self.redis_conn.set(name=str(key), value=str(value))
                if result:
                    logging.info(f"Данные с ключом '{key}' успешно добавлены.")
                else:
                    logging.warning(f"Не удалось добавить данные с ключом '{key}'.")
            except Exception as e:
                logging.error(f"Ошибка при добавлении данных в Redis: {e}")
        else:
            logging.warning("Отсутствует подключение к Redis.")

    def delete_data(self, key):
        if self.redis_conn:
            try:
                result = self.redis_conn.delete(key)
                if result == 1:
                    logging.info(f"Данные с ключом '{key}' успешно удалены.")
                else:
                    logging.warning(f"Данные с ключом '{key}' не найдены.")
            except Exception as e:
                logging.error(f"Ошибка при удалении данных из Redis: {e}")
        else:
            logging.warning("Отсутствует подключение к Redis.")

    def publish_message(self, channel, message):
        if self.redis_conn:
            try:
                result = self.redis_conn.publish(channel, message)
                logging.info(f"Сообщение '{message}' успешно опубликовано в канал '{channel}'.")
            except Exception as e:
                logging.error(f"Ошибка при публикации сообщения в канал '{channel}': {e}")
        else:
            logging.warning("Отсутствует подключение к Redis.")
            
    def push_to_queue(self, queue_name, value):
        if self.redis_conn:
            try:
                result = self.redis_conn.rpush(queue_name, value)  # Добавляем в конец очереди
                if result:
                    logging.info(f"Значение '{value}' успешно добавлено в очередь '{queue_name}'.")
                else:
                    logging.warning(f"Не удалось добавить значение '{value}' в очередь '{queue_name}'.")
            except Exception as e:
                logging.error(f"Ошибка при добавлении данных в очередь Redis: {e}")
        else:
            logging.warning("Отсутствует подключение к Redis.")

    def close(self):
        if self.redis_conn:
            self.redis_conn.close()
            logging.info("Соединение с Redis закрыто.")
