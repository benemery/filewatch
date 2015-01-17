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

class TestObserver(object):
    def test_duplicate_observers(self):
        """Can we add duplicate observers?"""
        subject = Subject()

        ob1 = ObserverObj1()
        subject.register_observer(ob1)
        subject.register_observer(ob1)

        assert len(subject.observers) == 1

    def test_remove_removed_observer(self):
        """Can we remove the same observer twice?"""
        subject = Subject()

        ob1 = ObserverObj1()
        subject.register_observer(ob1)

        assert len(subject.observers) == 1

        subject.remove_observer(ob1)
        assert len(subject.observers) == 0

        subject.remove_observer(ob1)
        assert len(subject.observers) == 0

    def test_observer_add_remove(self):
        """Can we add and remove observers?"""
        subject = Subject()

        ob1 = ObserverObj1()
        subject.register_observer(ob1)
        subject.register_observer(ObserverObj2())
        subject.register_observer(ObserverObj3())

        assert len(subject.observers) == 3

        subject.remove_observer(ob1)
        assert len(subject.observers) == 2

        subject.remove_observers()
        assert len(subject.observers) == 0

    def test_notifications(self):
        """Does a subject broadcast to all observers?"""
        subject = Subject()

        subject.register_observer(ObserverObj1())
        subject.register_observer(ObserverObj2())
        subject.register_observer(ObserverObj3())

        my_list = []
        subject.notify(a_list=my_list)

        assert len(my_list) == 3
        assert my_list == ['a', 'b', 'c', ]

