from filewatch.observer import Subject, ObserverBase


class ObserverObj1(ObserverBase):
    def notify(self, *args, **kwargs):
        a_list = kwargs['a_list']
        a_list.append('a')

class ObserverObj2(ObserverBase):
    def notify(self, *args, **kwargs):
        a_list = kwargs['a_list']
        a_list.append('b')

class ObserverObj3(ObserverBase):
    def notify(self, *args, **kwargs):
        a_list = kwargs['a_list']
        a_list.append('c')

class MySubject(Subject):
    pass

class TestObserver(object):
    def test_notifications(self):
        """Does a subject broadcast to all observers?"""
        subject = MySubject()

        subject.register_observer(ObserverObj1())
        subject.register_observer(ObserverObj2())
        subject.register_observer(ObserverObj3())

        my_list = []
        subject.notify(a_list=my_list)

        assert len(my_list) == 3
        assert my_list == ['a', 'b', 'c', ]

