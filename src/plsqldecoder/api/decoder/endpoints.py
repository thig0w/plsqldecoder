# -*- coding: utf-8 -*-
"""API endpoint definitions for /decoder namespace."""
from fastapi import APIRouter, HTTPException
from plsqldecoder.api.decoder.business import decode

tags_metadata = [
    {"name": "decoder", "description": "Decodes pl/sql develepor password hash"}
]

router = APIRouter(
    prefix="/decoder",
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        505: {"description": "Internal Server Error"},
    },
)


@router.get("/{hash}", tags=["decoder"])
async def decoder(hash: str):
    """Decodes Hash"""
    try:
        decoded_pass = decode(hash)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    return {"pass": decoded_pass}
