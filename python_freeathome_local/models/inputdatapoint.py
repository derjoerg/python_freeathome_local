"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .abstractdatapoint import AbstractDatapoint

if TYPE_CHECKING:
    from ..pairingids import PairingIDs
    from .abstractchannel import AbstractChannel


@dataclass
class InputDatapoint(AbstractDatapoint):
    """Model for an Input-Datapoint."""

    def __init__(
        self,
        channel: AbstractChannel,
        identifier: str,
        pairingID: PairingIDs,
        value: str,
    ):
        """Initialize a Inputdatapoint."""
        super().__init__(channel, identifier, pairingID, value)

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Input-Datapoint:\n" f"{parent}"

    async def setValue(self, value: int):
        """Set Value of current Datapoint and inform SysAp."""
        super().setValue(value)
        return (
            await self.getChannel()
            .getDevice()
            .getSysAp()
            .getApi()
            .setDatapoint(self)
        )

    def setSpecialValue(self, value: int):
        """Set Value of current Datapoint without informing SysAp."""
        return super().setValue(value)
