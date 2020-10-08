from celery import shared_task, task
from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from at_scrape_exercise.spiders import at_char_spider

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@task
def crawl_char_detail():
    at_char_spider.char_detail()
    print("+++++++++++++++++CRAWLED char_detail+++++++++++++++++")

# crawl_char_detail.delay(2,2)

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def scraper_example():
    logger.info("Starttttting task!")
    now = datetime.now()
    result = now.day + now.minute
    logger.info("task finished: result = %i" % result)
