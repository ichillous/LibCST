# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict
from typing import Any, Callable, TypeVar, cast


T = TypeVar("T")


def mark_no_op(
    f: Callable[["CSTMatchers", T], None]
) -> Callable[["CSTMatchers", T], None]:
    """
    Annotates stubs with a field to indicate they should not be collected
    by BatchableCSTVisitor.get_visitors() to reduce function call
    overhead when running a batched visitor pass.
    """

    cast(Any, f)._is_no_op = True
    return f


class CSTMatchers:
    # TODO: generate stubs for matchers with codegen
    pass
