"""logging test"""
import logging
import logging_test_submodule
from datetime import date
logging.basicConfig(
    level=logging.INFO,
    format="{asctime} {module} {levelname:<8}  {message}",
    style='{',
    handlers=[logging.FileHandler(f"mainmodule_log_{str(date.today())}.txt", 'a',
                                  encoding='utf-8')]
)


def test_logging() -> None:
    """test logging"""
    logging.info("From test_logging()")


if __name__ == '__main__':
    logging.info("Hello from main module")
    test_logging()
    logging_test_submodule.run()
