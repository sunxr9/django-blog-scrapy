from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
import logging
from blog import celery_app

logger = logging.getLogger(__name__)


# @shared_task
@celery_app.task()
def celery_send_email(subject, message, from_email, recipient_list):
    try:
        # 使用celery并发处理邮件发送的任务
        send_mail(subject, message, from_email, recipient_list)
        return 'success!'
    except Exception as e:
        logger.error("邮件发送失败: {}".format(e))
