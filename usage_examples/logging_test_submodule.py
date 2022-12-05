"""logging test submodule"""
import logging
from datetime import date
log = logging.getLogger(__name__)


def test_logging_submodule() -> None:
    """test logging"""
    logging.info("From test_logging_submodule()")


def run():
    """run"""
    logging.info("Hello from run() of submodule")
    test_logging_submodule()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {module} {levelname:<8}  {message}",
        style='{',
        handlers=[logging.FileHandler(f"sub_module_{str(date.today())}.txt", 'a',
                                      encoding='utf-8')]
    )
    logging.info("Hello from submodule")
    run()
