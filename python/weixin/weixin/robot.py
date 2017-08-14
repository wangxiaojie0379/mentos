#coding:utf-8


from werobot import WeRoBot

robot=WeRoBot(enable_session=False,
              token='chentu123',
               APP_ID='wx939a702b916b6508',
              APP_SECRET='c85c21188ba42a6263f0e28f6869ab6f')

@robot.handler
def hello(message):
    return 'hello'
