# Python - Serialization
In this directory we will delve into how data can be transformed and comunicated with different parts of a system and between systems.  It is meant to enhance our understanding and practical skills when handling real-world applications.  The methods we sill explore are **marshalling** and **serialization**.

## Marshalling
This is the process of transforming objects into a format that can be stored and/or transmitted over a network.  It involves packaging complex objects and their attributes into a simple (usually binary) format.  This is most crucial when objects need to be represented in a standard format throughout different platforms.

## Serialization
This process is closely related to marshalling.  It involves converting data structures or objects into a format that can be saved to a file or sent over a network.  Its main goal is to preserve the state of an object in order to recreate it identically in a different system.  This process is essential in developung applications that require data persistence, distributed computing, and data sharing between different software components.