from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Team.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()

            # Create users (super hero users)
            users = [
                User(username='octoman', email='octoman@school.edu', password='octopass'),
                User(username='catwoman', email='catwoman@school.edu', password='catpass'),
                User(username='batkid', email='batkid@school.edu', password='batpass'),
                User(username='spidergirl', email='spidergirl@school.edu', password='spiderpass'),
            ]
            for user in users:
                user.save()

            # Create teams
            team1 = Team(name='Octo Avengers')
            team1.save()
            team1.members.add(users[0], users[1])
            team2 = Team(name='Cat Crusaders')
            team2.save()
            team2.members.add(users[2], users[3])

            # Create workouts
            workout1 = Workout(name='Push Ups', description='Do 20 push ups')
            workout2 = Workout(name='Running', description='Run 1 mile')
            workout3 = Workout(name='Plank', description='Hold plank for 1 minute')
            workout1.save()
            workout2.save()
            workout3.save()

            # Create activities
            Activity.objects.create(user=users[0], activity_type='Running', duration=timedelta(minutes=30))
            Activity.objects.create(user=users[1], activity_type='Push Ups', duration=timedelta(minutes=10))
            Activity.objects.create(user=users[2], activity_type='Plank', duration=timedelta(minutes=5))
            Activity.objects.create(user=users[3], activity_type='Running', duration=timedelta(minutes=20))

            # Create leaderboard
            Leaderboard.objects.create(user=users[0], score=120)
            Leaderboard.objects.create(user=users[1], score=110)
            Leaderboard.objects.create(user=users[2], score=90)
            Leaderboard.objects.create(user=users[3], score=100)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
