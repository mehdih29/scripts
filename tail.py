#!/usr/bin/env python

import re, os, time, sys
from time import time, sleep
import re

from os.path import join, getsize, getmtime

if len(sys.argv) == 1:
    print("Argument Missing !")
    print("Usage:\n    {0:s} /path/to/log/file".format(sys.argv[0]))
    sys.exit(1)

startTime = time()
mTimeStart = 0
fileName = sys.argv[1]

if not os.path.exists(fileName) or not os.path.isfile(fileName):
    print("This file '{0:s}' does not exist !".format(fileName))
    sys.exit(2)

try:
    with open(fileName, 'r') as f:
        f.read(1)
except Exception as e:
    print("This file '{0:s}' cannot be opened for reading !".format(fileName))
    sys.exit(3)

folderLogs = os.path.dirname(fileName)

copyLines = []
reg = '''(?P<date>\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s?(?:AM|PM)) ( - Process\((?P<ibmmq_err_process>[^\)]+)\)\s+User\((?P<ibmmq_err_user>[^\)]+)\)\s+Program\((?P<ibmmq_err_program>[^\)]+)[^\)\n]*\)\s+Host\((?P<ibmmq_err_host>[^\)]+)\)\s+Installation\((?P<ibmmq_err_installation>[^\)]+)\)\s+VRMF\((?P<ibmmq_err_vrmf>[^\)]+)\)\s+(?:QMgr\((?P<ibmmq_err_qmgr>[^\)]+)\))?\s*^(?P<ibmmq_err_code>AMQ\d+):\s+(?P<ibmmq_err_text>.*?)\s+^EXPLANATION:\s+(?P<ibmmq_err_explanation>.*?)\s*^ACTION:\s+(?P<ibmmq_err_action>.*)\s*^----+(?: (?P<ibmmq_err_source>\w+\.c) : (?P<ibmmq_err_lineno>\d+) )?-+$)'''
regex = re.compile(reg, re.MULTILINE )#), flags = re.MULTILINE
try:

    while True:
        with open(fileName, 'r') as f:
            lines = f.read()
            #import pdb; pdb.set_trace()
            x = regex.match(lines)
            b = re.match(r"""(?P<date>\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}\s?(?:AM|PM)) ( - Process\((?P<ibmmq_err_process>[^\)]+)\)\s+User\((?P<ibmmq_err_user>[^\)]+)\)\s+Program\((?P<ibmmq_err_program>[^\)]+)[^\)\n]*\)\s+Host\((?P<ibmmq_err_host>[^\)]+)\)\s+Installation\((?P<ibmmq_err_installation>[^\)]+)\)\s+VRMF\((?P<ibmmq_err_vrmf>[^\)]+)\)\s+(?:QMgr\((?P<ibmmq_err_qmgr>[^\)]+)\))?\s*^(?P<ibmmq_err_code>AMQ\d+):\s+(?P<ibmmq_err_text>.*?)\s+^EXPLANATION:\s+(?P<ibmmq_err_explanation>.*?)\s*^ACTION:\s+(?P<ibmmq_err_action>.*)\s*^----+(?: (?P<ibmmq_err_source>\w+\.c) : (?P<ibmmq_err_lineno>\d+) )?-+$)""", lines)
            print x

#        show = False
#
#        if len(copyLines) == 0:
#            showLines = lines[-10:]
#            show = True
#
#        elif len(copyLines) != len(lines):
#            showLines = lines[len(copyLines) - len(lines):]
#            show = True
#
#        if show:
#            copyLines = list(lines)
#            for line in showLines:
#                print(line)
#



        sleep(10)

except KeyboardInterrupt as e:
    print("Program stopped by user !")
    sys.exit(0)

except Exception as e:
    print("Unknown error during execution !")
    print(e)
    sys.exit(4)

03/22/2019 08:17:30 AM - Process(16296.7) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:30 AM - Process(16296.7) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:32 AM - Process(16296.9) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:32 AM - Process(16296.9) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(15325.5728072) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(15325.5728072) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.8) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.8) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.10) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.10) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.13) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.13) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(15325.5728078) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(15325.5728078) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.15) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.15) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.6) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(15325.5728076) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:33 AM - Process(16296.6) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:33 AM - Process(15325.5728076) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:34 AM - Process(15325.5728071) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:34 AM - Process(15325.5728071) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:35 AM - Process(16296.4) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:35 AM - Process(16296.4) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:36 AM - Process(15325.5728077) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:36 AM - Process(15325.5728077) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:36 AM - Process(16296.11) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:36 AM - Process(16296.11) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:36 AM - Process(16296.14) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:36 AM - Process(16296.14) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 16296 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 08:17:37 AM - Process(15325.5728073) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 08:17:37 AM - Process(15325.5728073) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P1.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.17) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.17) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.7) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.7) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P2.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.11) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.15) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.11) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.15) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.13) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(6834.13) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(15325.5783801) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(15325.5783803) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(15325.5783805) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:47 PM - Process(15325.5783801) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(15325.5783803) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:47 PM - Process(15325.5783805) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:51 PM - Process(15325.5783800) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:51 PM - Process(6834.12) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:51 PM - Process(6834.12) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:51 PM - Process(15325.5783800) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:51 PM - Process(6834.16) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:51 PM - Process(6834.16) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:51 PM - Process(6834.10) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:51 PM - Process(6834.10) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:51 PM - Process(15325.5783802) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:51 PM - Process(15325.5783802) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:52 PM - Process(6834.14) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P1.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P1.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:52 PM - Process(6834.14) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P1.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P1.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:52 PM - Process(6834.4) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:52 PM - Process(15325.5783804) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9271: Channel 'NBBEBEB04P2.SVR' timed out.
EXPLANATION:
A timeout occurred while waiting to receive from the other end of channel
'NBBEBEB04P2.SVR'. The address of the remote end of the connection was
'10.123.1.22'.
ACTION:
The return code from the select() [TIMEOUT] 14 seconds call was 4 (X'4').
Record these values and tell the systems administrator.
----- amqccita.c : 4482 -------------------------------------------------------
03/22/2019 03:32:52 PM - Process(6834.4) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 6834 for channel 'NBBEBEB04P2.SVR'
ended abnormally. The host name is '10.123.1.22'; in some cases the host name
cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------
03/22/2019 03:32:52 PM - Process(15325.5783804) User(mqm) Program(amqrmppa)
                    Host(sysamq05) Installation(Installation1)
                    VRMF(8.0.0.8) QMgr(QM05)
AMQ9999: Channel 'NBBEBEB04P2.SVR' to host '10.123.1.22' ended abnormally.
EXPLANATION:
The channel program running under process ID 15325 for channel
'NBBEBEB04P2.SVR' ended abnormally. The host name is '10.123.1.22'; in some
cases the host name cannot be determined and so is shown as '????'.
ACTION:
Look at previous error messages for the channel program in the error logs to
determine the cause of the failure. Note that this message can be excluded
completely or suppressed by tuning the "ExcludeMessage" or "SuppressMessage"
attributes under the "QMErrorLog" stanza in qm.ini. Further information can be
found in the System Administration Guide.
----- amqrmrsa.c : 930 --------------------------------------------------------