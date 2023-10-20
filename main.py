import app
import mapapi
import database
import buttons
import logging

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    try:
        app.start()
        logging.info('Приложение успешно запущено')
    except Exception as e:
        logging.error(f'Произошла ошибка: {str(e)}', exc_info=True)
