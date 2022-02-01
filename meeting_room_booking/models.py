from django.db import models
import constants


DEPARTMENTS = constants.DEPARTMENTS


class MeetingRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=1)


class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    department = models.CharField(max_length=2, choices=DEPARTMENTS)

    def get_lsat_name(self):
        return self.full_name.split()[0]


class Booking(models.Model):
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    datetime_begin = models.DateTimeField(max_length=255)
    datetime_end = models.DateTimeField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def book_the_room(self, dt_begin, dt_end, room, book_user):
        self.datetime_begin = dt_begin
        self.datetime_end = dt_end
        self.meeting_room = room
        self.user = book_user
        self.save()

    def get_duration(self):
        return (self.datetime_end - self.datetime_begin).total_seconds() // 60
