import pytest

from src.event.event import Event
from src.event.member_service import MemberService


@pytest.mark.integration
def test_register_new_member__integration():
    #Arrange
    promenad = Event("Promenad")
    ms = MemberService()


    #Act
    promenad.register_new_member("Göran", ms)
    deltagare = promenad.participants
    medlemmar = ms.get_members()

    #Assert
    assert 'Göran' in deltagare
    assert 'Göran' in medlemmar
