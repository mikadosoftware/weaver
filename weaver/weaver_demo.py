#! -*- config:UTF-8 -*-

# weaver demo

import weaver_logging
from weaver_exception import WeaverBaseError
log = weaver_logging.getLogger(__name__)

def run():
    log.info("This is a log")
    try:
        raise WeaverBaseError("Oops a problem")
    except WeaverBaseError, e:
        log.error("There was an error raised - it said %s", str(e))

if __name__ == '__main__':
    run()
