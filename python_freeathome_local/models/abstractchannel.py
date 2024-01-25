"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from abc import ABC
from typing import TYPE_CHECKING, Any

from ..functionids import FunctionIDs
from ..pairingids import PairingIDs
from .datapointfactory import DatapointFactory
from .inputdatapoint import InputDatapoint
from .outputdatapoint import OutputDatapoint
from .parameter import Parameter
from .parameterfactory import ParameterFactory

if TYPE_CHECKING:
    from .abstractdatapoint import AbstractDatapoint
    from .abstractdevice import AbstractDevice
    from .floor import Floor
    from .room import Room


class AbstractChannel(ABC):
    """Model for an abstract Channel."""

    _device: AbstractDevice
    _identifier: str = ""
    _floor: Floor | None = None
    _room: Room | None = None
    _displayName: str = ""
    _functionID: FunctionIDs | None = None
    _inputs: dict[str, InputDatapoint] | None = None
    _outputs: dict[str, OutputDatapoint] | None = None
    _parameters: dict[str, Parameter] | None = None

    def __init__(
        self,
        device: AbstractDevice,
        identifier: str,
        floor: Floor | None,
        room: Room | None,
        displayName: str,
        functionID: FunctionIDs,
        parameters: dict[str, Any],
        inputs: dict[str, Any],
        outputs: dict[str, Any],
    ):
        """Initialize an AbstractChannel."""
        self._device = device
        self._identifier = identifier
        self._floor = floor
        self._room = room
        self._displayName = displayName
        self._functionID = functionID
        self._inputs = {}
        self._outputs = {}
        self._parameters = {}

        for key, value in parameters.items():
            parameter = ParameterFactory.create(key, value)

            if parameter is not None:
                if isinstance(parameter, Parameter):
                    self._parameters[key] = parameter

        for key, value in inputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                if isinstance(datapoint, InputDatapoint):
                    self._inputs[key] = datapoint

        for key, value in outputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                if isinstance(datapoint, OutputDatapoint):
                    self._outputs[key] = datapoint

    def __str__(self) -> str:
        """Redefine object-to-string."""
        if self._floor is None:
            floor = "<Not set>"
        else:
            floor = self._floor.getName()

        if self._room is None:
            room = "<Not set>"
        else:
            room = self._room.getName()

        string = (
            f"Identifier: {self._identifier}\n"
            f"Name      : {self._displayName}\n"
            f"Floor     : {floor}\n"
            f"Room      : {room}\n"
            f"Function  : {self._functionID}"
        )

        if isinstance(self._inputs, dict):
            string = f"{string}\nInputs: {len(self._inputs)}\n----------"

            for key, input in self._inputs.items():
                value = str(input)
                string = (
                    f"{string}\n"
                    f"{textwrap.indent(value, '    ')}\n"
                    f"----------"
                )

        if isinstance(self._outputs, dict):
            string = f"{string}\nOutputs: {len(self._outputs)}\n----------"

            for key, output in self._outputs.items():
                value = str(output)
                string = (
                    f"{string}\n"
                    f"{textwrap.indent(value, '    ')}\n"
                    f"----------"
                )

        if isinstance(self._parameters, dict):
            string = (
                f"{string}\nParameters: {len(self._parameters)}\n----------"
            )

            for key, parameter in self._parameters.items():
                value = str(parameter)
                string = (
                    f"{string}\n"
                    f"{textwrap.indent(value, '    ')}\n"
                    f"----------"
                )

        return string

    def getDevice(self) -> AbstractDevice:
        """Return Device of the Channel."""
        return self._device

    def getIdentifier(self) -> str:
        """Return Identifier of the Channel."""
        return self._identifier

    def getDisplayName(self) -> str:
        """Return DisplayName of the Channel."""
        return self._displayName

    def getFunctionID(self) -> FunctionIDs | None:
        """Return FunctionID of the Channel."""
        return self._functionID

    def getInputs(self) -> dict[str, InputDatapoint] | None:
        """Return all InputDatapoints of the Channel."""
        return self._inputs

    def updateFromDict(self, key: str, value: str) -> AbstractDatapoint | None:
        """Return Datapoint object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data

        Returns:
        -------
            The updated Datapoint object.
        """
        datapoint = None

        if isinstance(self._outputs, dict):
            if key in self._outputs:
                if isinstance(self._outputs[key], OutputDatapoint):
                    datapoint = self._outputs[key].setValue(value)
                    return datapoint
        if isinstance(self._inputs, dict):
            if key in self._inputs:
                # Very special handling for MovementDetector because
                # for whatever reason an Input-Datapoint is set through
                # the websocket instead of an Output-Datapoint ...
                if isinstance(self._inputs[key], InputDatapoint):
                    datapoint = self._inputs[key].setSpecialValue(int(value))
                    return datapoint

        print(self.getDisplayName(), " - ", key, " : ", value)
        return datapoint

    def getOutputByPairingID(self, pairingID: PairingIDs) -> AbstractDatapoint:
        """Return OutputDatapoint of a specific PairingID."""
        if isinstance(self._outputs, dict):
            for key, value in self._outputs.items():
                if value.getPairingID() == pairingID:
                    return value

        raise NameError

    def getInputByPairingID(self, pairingID: PairingIDs) -> AbstractDatapoint:
        """Return InputDatapoint of a specific PairingID."""
        if isinstance(self._inputs, dict):
            for key, value in self._inputs.items():
                if value.getPairingID() == pairingID:
                    return value

        raise NameError
