# tasklists
The project provides a basic api support for task management and enterprise deskboard. The following are planned implementation:

1. Create Task
-- Send mail if current user is not the task handler
2. Transfer Task
-- Send acknowledgment email
-- Send mail to stake holders about status updates
3. Close Task
-- send email to all stake holders
4. List Tasks
5. Filter Tasks

# The Project will be using:
1. marshmallow : serializers
2. celery : background worker
3. sqlalchemy : ORM provider
4. flask : app engine
5. flask-email : email source

Note: For development purpose SMTP are selected as free tier.

https://stackoverflow.com/questions/19323990/flask-migrate-not-creating-tables
