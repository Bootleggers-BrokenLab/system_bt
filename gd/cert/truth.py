#!/usr/bin/env python3
#
#   Copyright 2020 - The Android Open Source Project
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import time

from mobly.asserts import assert_true
from mobly.asserts import assert_false

from mobly import signals

import sys, traceback


class ObjectSubject(object):

    def __init__(self, value):
        self._value = value

    def isEqualTo(self, other):
        if self._value != other:
            raise signals.TestFailure(
                "Expected \"%s\" to be equal to \"%s\"" % (self._value, other),
                extras=None)

    def isNotEqualTo(self, other):
        if self._value == other:
            raise signals.TestFailure(
                "Expected \"%s\" to not be equal to \"%s\"" % (self._value,
                                                               other),
                extras=None)

    def isNone(self):
        if self._value is not None:
            raise signals.TestFailure(
                "Expected \"%s\" to be None" % self._value, extras=None)

    def isNotNone(self):
        if self._value is None:
            raise signals.TestFailure(
                "Expected \"%s\" to not be None" % self._value, extras=None)


class BooleanSubject(ObjectSubject):

    def __init__(self, value):
        super().__init__(value)

    def isTrue(self):
        assert_true(self._value, "")

    def isFalse(self):
        assert_false(self._value, "")


def assertThat(subject):
    if type(subject) is bool:
        return BooleanSubject(subject)
    else:
        return ObjectSubject(subject)