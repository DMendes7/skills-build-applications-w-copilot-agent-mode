from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Add test data for users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=25)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=30)

        # Add test data for teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)

        # Add test data for activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-04-01')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-04-02')

        # Add test data for leaderboard
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Add test data for workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing yoga session', duration=60)
        Workout.objects.create(name='HIIT', description='High-intensity interval training', duration=30)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
