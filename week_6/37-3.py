from datetime import datetime, timedelta


class Meeting:
    def __init__(self, date: datetime, title: str):
        self.date = date
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings

    def add_meeting(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting

    def next_available_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            meeting_date += timedelta(minutes=60)

        return meeting_date


def test_add_meeting():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'Urodziny mam!')
    birthday2 = Meeting(datetime(2020, 11, 9, 12, 0), 'Urodziny mam!')
    calendar = Calendar()

    # when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)

    # then
    assert len(calendar.meetings) == 1


def test_add_two_meetings():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'Urodziny mam!')
    birthday2 = Meeting(datetime(2021, 11, 9, 12, 0), 'Urodziny mam!')
    calendar = Calendar()

    # when
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)

    # then
    assert len(calendar.meetings) == 2


def test_check_next_available_time_slot():
    # given
    birthday = Meeting(datetime(2020, 11, 9, 12, 0), 'Urodziny mam!')
    birthday2 = Meeting(datetime(2020, 11, 9, 13, 0), 'Urodziny mam!')
    birthday3 = Meeting(datetime(2020, 11, 9, 14, 0), 'Urodziny mam!')
    calendar = Calendar()
    calendar.add_meeting(birthday)
    calendar.add_meeting(birthday2)
    calendar.add_meeting(birthday3)

    # when
    next_time_slot = calendar.next_available_slot(datetime(2020, 11, 9, 12, 0))

    # then
    assert next_time_slot == datetime(2020, 11, 9, 15, 0)


def test_id_given_datetime_available():
    # given
    calendar = Calendar()

    # when
    next_time_slot = calendar.next_available_slot(datetime(2020, 11, 9, 12, 0))

    # then
    assert next_time_slot == datetime(2020, 11, 9, 12, 0)
