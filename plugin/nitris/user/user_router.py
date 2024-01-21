from fastapi import APIRouter
from starlette.requests import Request
from core.database import DBConnect
from core.template import UserTemplates
from lib.board_lib import get_list_thumbnail
from core.models import Board, BoardFile, BoardNew, Scrap, WriteBaseModel
from lib.common import *
from lib.member_lib import get_member
from .. import plugin_config
from ..plugin_config import module_name

router = APIRouter()

templates = UserTemplates()


@router.get("/show")
async def show(request: Request):
    """json 출력예시"""
   
    return {"message": "Hello Plugin JSON!"}


@router.get("/load_flash/{fl_num}")
async def show(request: Request, fl_num: int):
    """플래시 반환"""
    file_dir_ = "swf"
    if fl_num_ <= 50000:
        file_dir_ = "pre_swf/01"
    else:
        if fl_num_ >= 50001 and fl_num_ <= 100000:
            file_dir_ = "pre_swf/02"
        else:
            if fl_num_ >= 100001 and fl_num_ <= 150000:
                file_dir_ = "pre_swf/03"
            else:
                if fl_num_ >= 150001 and fl_num_ <= 200000:
                    file_dir_ = "pre_swf/04"
                else:
                    if fl_num_ >= 200001 and fl_num_ <= 250000:
                        file_dir_ = "pre_swf/05"
                    else:
                        if fl_num_ >= 250001 and fl_num_ <= 300000:
                            file_dir_ = "pre_swf/06"
                        else:
                            if fl_num_ >= 300001 and fl_num_ <= 350000:
                                file_dir_ = "pre_swf/07"
                            else:
                                if fl_num_ >= 350001 and fl_num_ <= 400000:
                                    file_dir_ = "pre_swf/08"
                                else:
                                    if fl_num_ >= 400001 and fl_num_ <= 450000:
                                        file_dir_ = "pre_swf/09"
                                    else:
                                        if fl_num_ >= 450001 and fl_num_ <= 500000:
                                            file_dir_ = "pre_swf/10"
                                        else:
                                            file_dir_ = "swf"
    return {"file_dir": file_dir_}

@router.get("/myhome/{mb_id}")
async def show(request: Request, mb_id: str):
    """작가방 출력"""
    db = DBConnect().sessionLocal()
    bo_table = "myflash"
    board = db.get(Board, bo_table)
    search_bbs = dynamic_create_write_table(bo_table)
    templates.env.globals["get_list_thumbnail"] = get_list_thumbnail
    article = db.scalars(
        select(search_bbs)
        .where(search_bbs.wr_is_comment == 0)
        .where(search_bbs.mb_id == mb_id)
        .order_by(search_bbs.wr_num)
    ).all()
    s_member = get_member(mb_id)
    return templates.TemplateResponse(
        f"{plugin_config.TEMPLATE_PATH}/myhome.html",
        {
            "request": request,
            "board": board,
            "title": s_member.mb_nick + "님의 마이홈",
            "content": f"준비중!",
            "mb_id": mb_id,
            "mb_nick": s_member.mb_nick,
            "bo_table": bo_table,
            "writes": article
        })

@router.get("/myhome/{mb_id}/{bo_table}")
async def show(request: Request, mb_id: str, bo_table: str):
    """작가방 출력"""
    db = DBConnect().sessionLocal()
    board = db.get(Board, bo_table) 
    search_bbs = dynamic_create_write_table(bo_table)
    templates.env.globals["get_list_thumbnail"] = get_list_thumbnail
    article = db.scalars(
        select(search_bbs)
        .where(search_bbs.wr_is_comment == 0)
        .where(search_bbs.mb_id == mb_id)
        .order_by(search_bbs.wr_num)
    ).all()
    s_member = get_member(mb_id)
    return templates.TemplateResponse(
        f"{plugin_config.TEMPLATE_PATH}/myhome.html",
        {
            "request": request,
            "board": board,
            "title": s_member.mb_nick + "님의 마이홈",
            "content": f"준비중!",
            "mb_id": mb_id,
            "mb_nick": s_member.mb_nick,
            "bo_table": bo_table,
            "writes": article
        })