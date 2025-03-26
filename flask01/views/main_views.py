from flask import Blueprint

# 특정 /main/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로 
mbp = Blueprint('main', __name__, url_prefix='/main')

# Flask에서 값을 주소줄로 입력받아서 사용하는 방법
# <변수명> /변수명
@mbp.route('/<username>')
def print_name(username):
    return f'{__name__} {username}hello'

# <자료형:변수명>
# <path:변수명> : /를 포함한 서브경로 전달

@mbp.route('/path/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath}hello'

@mbp.route('/items/')
@mbp.route('/items/<itemname>')
@mbp.route('/items/<itemname>/<int:quantity>')
def print_items(itemname='기본값', quantity=0):
    return f'{__name__} {itemname, quantity} hello'