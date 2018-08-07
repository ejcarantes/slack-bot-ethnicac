from apscheduler.schedulers.blocking import BlockingScheduler
from hello import views
from hello.views import slackBot, twittertrends


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    slackBot.api_call(
        "chat.postMessage",
        channel="CC3BN2BC4",
        text=twittertrends(),
        icon_emoji=':robot_face:'
    )
    # print('This job is run every 30 minute.')

"""
@sched.scheduled_job('cron', day_of_week='mon-sun', minutes=10)
def scheduled_job():
    slackBot.api_call(
        "chat.postMessage",
        channel = "CC3BN2BC4",
        text=twittertrends(),
        icon_emoji=':robot_face:'
    )
    # print('This job is run every weekday at 5pm.')
    """

sched.start()