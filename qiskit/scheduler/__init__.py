# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
===========================================
Circuit Scheduler (:mod:`qiskit.scheduler`)
===========================================

.. currentmodule:: qiskit.scheduler

A circuit scheduler compiles a circuit program to a pulse program.

Core API
========

.. autoclass:: ScheduleConfig

.. currentmodule:: qiskit.scheduler.schedule_circuit
.. autofunction:: schedule_circuit
.. currentmodule:: qiskit.scheduler

Pulse scheduling methods
========================

.. currentmodule:: qiskit.scheduler.methods
.. autofunction:: as_soon_as_possible
.. autofunction:: as_late_as_possible
.. currentmodule:: qiskit.scheduler
"""
from qiskit.scheduler import schedule_circuit
from qiskit.scheduler.config import ScheduleConfig
