from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator", # DAGS에 표시되는 이름,  .py 파일 이름과 같이써야 구분이 쉬움
    schedule="0 0 * * *", # cron 표현식, 0분 0시에 실행 (분 시 일 월 요일 (주기))
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 시작시간, 한국 시간으로 변경해줘야함,
    catchup=False, # 시작시간 이전의 task들은 실행하지 않는다. true, false (true로 하면 한꺼번에 돌아감)
    # dagrun_timeout=datetime.timedelta(minutes=60), # dag가 실행되는 최대 시간, 60분이상 돌게되면 실패로 되도록 설정
    # tags=["example", "example2"], # DAG에 태그를 달아줄 수 있다.
    # params={"example_key": "example_value"}, # DAG에 파라미터를 넘겨줄 수 있다. 밑에 task들에게 공통적으로 넘겨줄 파라미터가 있다면 사용
) as dag:
      bash_t1 = BashOperator(
        task_id="bash_t1", # graph에 표현될 id, 객체 명과 똑같이 쓰는게 구분이 편하다
        bash_command="echo whoami",
    )
      
      bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
      
      bash_t1 >> bash_t2 # bash_t1이 성공하면 bash_t2가 실행된다.