import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="para8_1.log",
                    filemode="w",
                    format="We have next message: %(asctime)s:%(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
