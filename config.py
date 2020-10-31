import os
SUPPORT_PATH = [
    '/User/DoLogin2',
    '/Course/GetStuCourse2',
    '/Bus/GetTimetableAndReserve',
    '/Bus/GetUserReserve3',
    '/Bus/CreateUserReserve',
    '/Bus/GetUserIllegal2',
    '/Leave/GetStuApply',
    '/Leave/GetInsertInfo',
    '/Leave/GetTeacher2',
    '/Leave/DoSaveApply2',
]


try:
    TARGET_HOST = os.environ['TARGET_HOST']
except KeyError:
    TARGET_HOST = '127.0.0.1'
