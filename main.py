from datetime import datetime
from sys import argv

from loguru import logger


class CheckDate:

    def check(self, dt: datetime.date = None) -> str:
        if dt:
            logger.info("Значение из программы")
            return self.__checker(dt)
        if len(argv) == 2:
            logger.info("Значение из консоли")
            _, dt = argv
            return self.__checker(dt)
        return "Date is None"

    def __checker(self, dt: str) -> str:
        logger.info(f"check date: {str(dt)}")
        if self.__date_validator(dt):
            return "Date is valid"
        return "Invalid date"

    @staticmethod
    def __date_validator(dt: str) -> bool:
        try:
            datetime.strptime(dt, "%d.%m.%Y").date()
            return True
        except Exception as e:
            logger.error(e)
            return False


if __name__ == '__main__':
    logger.info("start app")
    checker = CheckDate()
    res = checker.check('24.07.2023')
    logger.success(f"result: {res}")
