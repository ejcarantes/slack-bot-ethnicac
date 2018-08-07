from apscheduler.schedulers.blocking import BlockingScheduler
from hello import views
from hello.views import slackBot, twittertrends

sched = BlockingScheduler()
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    if response == 0:
        print (hostname+' is up!')
    else:
        print (hostname+' is down!')
    # views.postTrend("CC06NGT8S", views.trends())
    # print('This job is run every 30 minute.')

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    slackBot.api_call(
        "chat.postMessage",
        channel="C3BN2BC4",
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