from flask import Blueprint, render_template
from ..models import Question
# 특정 /main/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로 
mbp = Blueprint('main', __name__, url_prefix='/')

# Flask에서 값을 주소줄로 입력받아서 사용하는 방법

# 5001 로 접속하면 index.html 을 화면에 랜더링링
@mbp.route('/')
def index():
    return render_template('index.html')

# <자료형:변수명>
# <path:변수명> : /를 포함한 서브경로 전달

#@mbp.route('/path/<path:subpath>')
#def print_path(subpath):
#    return f'{__name__} {subpath}hello'

#@mbp.route('/items/')
#@mbp.route('/items/<itemname>')
#@mbp.route('/items/<itemname>/<int:quantity>')
#def print_items(itemname='기본값', quantity=0):
#    return f'{__name__} {itemname, quantity} hello'