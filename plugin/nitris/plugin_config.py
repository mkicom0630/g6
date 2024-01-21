import os

# module_name 는 플러그인의 폴더 이름입니다.
module_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
router_prefix = "nitris"
admin_router_prefix = router_prefix

TEMPLATE_PATH = f"{module_name}/templates"

# 관리자 메뉴를 설정합니다.
admin_menu = {
        f"{module_name}": [
            {
                "name": "트리니티빌더",
                "url": "",
                "tag": "",
            },
            {
                "id": module_name + "1",  # 메뉴 아이디
                "name": "마이홈 관리",
                "url": f"{admin_router_prefix}/myhome_admin",
                "tag": "demo1",
            },
            {
                "id": module_name + "2",  # 메뉴 아이디
                "name": "사용자 경험치 관리",
                "url": f"{admin_router_prefix}/xp_admin",
                "tag": "demo2",
            },
        ]
    }