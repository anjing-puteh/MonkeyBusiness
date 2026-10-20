from modules.registry import Ctx, set_xrpc_defaults, xrpc
import config

from core_common import E

set_xrpc_defaults(service="local", models=["LDJ"])

@xrpc("IIDX34streaming/common")
async def iidx34streaming_common(ctx: Ctx):

    response = E.response(E.IIDX34streaming())

    return response

@xrpc("IIDX34streaming/getcm")
async def iidx34streaming_getcm(ctx: Ctx):

    response = E.response(E.IIDX34streaming())

    return response
