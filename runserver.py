# -*- coding: UTF-8 -*-

from datetime import datetime
from Dance import app
from version import softVersion
import os
import logging
from logging.handlers import TimedRotatingFileHandler


if __name__ == "__main__":

    # 准备log
    now = datetime.now()
    strLogDir = os.path.join(os.getcwd(), "log")
    if not os.path.exists(strLogDir):
        os.makedirs(strLogDir)

    logFileName = "./log_%s.txt" % now.strftime("%Y-%m")
    logFilePath = os.path.join(strLogDir, "log_byte")
    strWhen = "midnight"
    logHandler = TimedRotatingFileHandler(logFilePath, when=strWhen, interval=1, backupCount=8)
    logFormatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    logHandler.setFormatter(logFormatter)
    g_logger = logging.getLogger('')
    g_logger.addHandler(logHandler)
    g_logger.setLevel(logging.WARNING)

    # 启动
    strLog = '============ byte starts to dance (Version:%s)  ==============\n' % softVersion.getCurrentVersion()
    logging.warning(strLog)

    # 启动flask
    app.run(host="0.0.0.0", port=80, use_reloader=False, threaded=True)
