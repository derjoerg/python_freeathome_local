"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC, abstractmethod
import textwrap

from ..functionids import FunctionIDs
from ..pairingids import PairingIDs
from .parameterfactory import ParameterFactory
from .datapointfactory import DatapointFactory
from .inputdatapoint import InputDatapoint
from .outputdatapoint import OutputDatapoint

class AbstractChannel(ABC):
    """Model for an abstract Channel."""

    _device: AbstractDevice | None = None
    _identifier: str = ""
    _floor: Floor | None = None
    _room: Room | None = None
    _displayName: str = ""
    _functionID: FunctionIDs
    _inputs: {}
    _outputs: {}
    _parameters: {}

    def __init__(self, device: AbstractDevice, identifier: str, floor: Floor | None, room: Room | None, displayName: str, functionID: FunctionIDs, parameters: dict[str, Any], inputs: dict[str, Any], outputs: dict[str, Any]):
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
                self._parameters[key] = parameter

        for key, value in inputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                self._inputs[key] = datapoint

        for key, value in outputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                self._outputs[key] = datapoint

    def __str__(self) -> str:

        if self._floor is None:
            floor = '<Not set>'
        else:
            floor = self._floor.getName()
        
        if self._room is None:
            room = '<Not set>'
        else:
            room = self._room.getName()

        string = (
            f"Identifier: {self._identifier}\n"
            f"Name      : {self._displayName}\n"
            f"Floor     : {floor}\n"
            f"Room      : {room}\n"
            f"Function  : {self._functionID}"
        )

        string = (
            f"{string}\n"
            f"Inputs: {len(self._inputs)}\n"
            f"----------"
        )

        for key, input in self._inputs.items():
            value = str(input)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        string = (
            f"{string}\n"
            f"Outputs: {len(self._outputs)}\n"
            f"----------"
        )

        for key, output in self._outputs.items():
            value = str(output)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        string = (
            f"{string}\n"
            f"Parameters: {len(self._parameters)}\n"
            f"----------"
        )

        for key, parameter in self._parameters.items():
            value = str(parameter)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )
        
        return string

    def getDevice(self):
        return self._device

    def getIdentifier(self) -> str:
        return self._identifier

    def getDisplayName(self) -> str:
        return self._displayName

    def getFunctionID(self):
        return self._functionID

    def getInputs(self):
        return self._inputs

    def updateFromDict(self, key, value):
        """Return Datapoint object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data
        
        Returns:
        -------
            The updated Datapoint object.
        """

        if key in self._outputs:
            datapoint = self._outputs[key].setValue(value)
            return datapoint
        elif key in self._inputs:
            # Very special handling for MovementDetector because 
            # for whatever reason an Input-Datapoint is set through
            # the websocket instead of an Output-Datapoint ...
            datapoint = self._inputs[key].setSpecialValue(value)
            return datapoint
        else:
            print(self.getDisplayName(), ' - ', key, ' : ', value)

    def getOutputByPairingID(self, pairingID) -> AbstractDatapoint:

        for key, value in self._outputs.items():

            if value.getPairingID() == pairingID:
                return value
        
        raise NameError

    def getInputByPairingID(self, pairingID) -> AbstractDatapoint:
    
        for key, value in self._inputs.items():

            if value.getPairingID() == pairingID:
                return value
        
        raise NameError
