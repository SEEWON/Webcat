# 컴퓨터공학과 주요공지
from batch_files import batch_cse_main
from batch_files import logger
from batch_files import batch_scholarship
from batch_files import batch_academic
from batch_files import batch_general
from batch_files import batch_cse_job

batch_cse_main.exec_batch()

# 컴퓨터공학과 취업/인턴십공지
batch_cse_job.exec_batch()

# 일반공지
batch_general.exec_batch()

# 학사공지
batch_academic.exec_batch()

# 장학공지
batch_scholarship.exec_batch()

logger.testing()
