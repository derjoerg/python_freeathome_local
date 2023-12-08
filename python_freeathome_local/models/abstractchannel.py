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

    __device: AbstractDevice | None = None
    __identifier: str = ""
    __floor: Floor | None = None
    __room: Room | None = None
    __displayName: str = ""
    __functionID: FunctionIDs
    __inputs: {}
    __outputs: {}
    __parameters: {}

    def __init__(self, device: AbstractDevice, identifier: str, floor: Floor | None, room: Room | None, displayName: str, functionID: FunctionIDs, parameters: dict[str, Any], inputs: dict[str, Any], outputs: dict[str, Any]):
        self.__device = device
        self.__identifier = identifier
        self.__floor = floor
        self.__room = room
        self.__displayName = displayName
        self.__functionID = functionID
        self.__inputs = {}
        self.__outputs = {}
        self.__parameters = {}

        for key, value in parameters.items():
            parameter = ParameterFactory.create(key, value)

            if parameter is not None:
                self.__parameters[key] = parameter

        for key, value in inputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                self.__inputs[key] = datapoint

        for key, value in outputs.items():
            datapoint = DatapointFactory.create(self, key, value)

            if datapoint is not None:
                self.__outputs[key] = datapoint

    def __str__(self) -> str:

        if self.__floor is None:
            floor = '<Not set>'
        else:
            floor = self.__floor.getName()
        
        if self.__room is None:
            room = '<Not set>'
        else:
            room = self.__room.getName()

        string = (
            f"Identifier: {self.__identifier}\n"
            f"Name      : {self.__displayName}\n"
            f"Floor     : {floor}\n"
            f"Room      : {room}\n"
            f"Function  : {self.__functionID}"
        )

        string = (
            f"{string}\n"
            f"Inputs: {len(self.__inputs)}\n"
            f"----------"
        )

        for key, input in self.__inputs.items():
            value = str(input)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        string = (
            f"{string}\n"
            f"Outputs: {len(self.__outputs)}\n"
            f"----------"
        )

        for key, output in self.__outputs.items():
            value = str(output)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        string = (
            f"{string}\n"
            f"Parameters: {len(self.__parameters)}\n"
            f"----------"
        )

        for key, parameter in self.__parameters.items():
            value = str(parameter)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )
        
        return string

    def getDevice(self):
        return self.__device

    def getIdentifier(self) -> str:
        return self.__identifier

    def getDisplayName(self) -> str:
        return self.__displayName

    def getInputs(self):
        return self.__inputs

    def updateFromDict(self, key, value):
        """Return Datapoint object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data
        
        Returns:
        -------
            The updated Datapoint object.
        """

        if key in self.__outputs:
            datapoint = self.__outputs[key].setValue(value)
            return datapoint
