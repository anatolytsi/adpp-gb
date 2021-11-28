from abc import ABC, abstractmethod


class Observer(ABC):
    """Abstract observer class"""

    @abstractmethod
    def update(self, course):
        """
        Abstract method to update observers about the course changes
        :param course: observed course
        """
        pass


class CourseNotifier:
    """Course notifier class"""

    def __init__(self):
        self.observers = []

    def notify(self):
        """Notifies course observers"""
        for item in self.observers:
            item.update(self)


class SmsSender(Observer):
    """SMS sender observer"""

    def update(self, course):
        """
        Updates SMS observers via SMS
        :param course: observed course
        """
        print(f'SMS: user {course.students[-1].name} joined course {course.name}')


class EmailSender(Observer):
    """Email sender observer"""

    def update(self, course):
        """
        Updates Email observers via Email
        :param course: observed course
        """
        print(f'EMAIL: user {course.students[-1].name} joined course {course.name}')
