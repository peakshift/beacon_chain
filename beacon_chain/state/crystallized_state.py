from typing import (  # noqa: F401
    Any,
    Dict,
)

from .crosslink_record import CrosslinkRecord
from .shard_and_committee import ShardAndCommittee
from .validator_record import ValidatorRecord


class CrystallizedState():
    fields = {
        # List of validators
        'validators': [ValidatorRecord],
        # Last CrystallizedState recalculation
        'last_state_recalc': 'int64',
        # What active validators are part of the attester set
        # at what height, and in what shard. Starts at slot
        # last_state_recalc - CYCLE_LENGTH
        'shard_and_committee_for_slots': [[ShardAndCommittee]],
        # The last justified slot
        'last_justified_slot': 'int64',
        # Number of consecutive justified slots ending at this one
        'justified_streak': 'int64',
        # The last finalized slot
        'last_finalized_slot': 'int64',
        # The current dynasty
        'current_dynasty': 'int64',
        # Records about the most recent crosslink for each shard
        'crosslink_records': [CrosslinkRecord],
        # Total balance of deposits
        'total_deposits': 'int256',
        # Used to select the committees for each shard
        'dynasty_seed': 'hash32',
        # start of the current dynasty
        'dynasty_start': 'int64',
    }
    defaults = {
        'validators': [],
        'last_state_recalc': 0,
        'shard_and_committee_for_slots': [],
        'last_justified_slot': 0,
        'justified_streak': 0,
        'last_finalized_slot': 0,
        'current_dynasty': 0,
        'crosslink_records': [],
        'total_deposits': 0,
        'dynasty_seed': b'\x00'*32,
        'dynasty_start': 0,
    }  # type: Dict[str, Any]

    def __init__(self, **kwargs):
        for k in self.fields.keys():
            assert k in kwargs or k in self.defaults
            setattr(self, k, kwargs.get(k, self.defaults.get(k)))

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    @property
    def num_validators(self) -> int:
        return len(self.validators)

    @property
    def num_crosslink_records(self) -> int:
        return len(self.crosslink_records)
