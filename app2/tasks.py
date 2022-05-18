# from celery import task     # for celery==4.4.2
from celery import shared_task    # for celery== 5.2.6
from celery.utils.log import get_task_logger
from .email import send_review_email

logger = get_task_logger(__name__)


@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info("sent review email") 
    return send_review_email(name, email, review)

