#author:mcc
#project:httrun
#data:2020/8/24
#time:17:16


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.login_test import  TestCaseLogin


class TestCaseFR3tiaojiao(HttpRunner):
    config = (
        Config("fr3 调焦Status远小步")
            .base_url("http://www.1123.com/ovopark-device")
            .verify(False)
    )

    teststeps = [
        Step(
            RunTestCase("setUp /login.action")
            .call(TestCaseLogin)  # 导入后就可以调用了
            .export(*["token"])  # 在RunTestCase步骤中定义这个变量的导出
        ),
        Step(
            RunRequest("fr3Status")
                .get("/fr3/fr3PtzZoom")
                .with_params(
                    **{
                        "cmd": "1",
                        "deviceStatusId": "1729379",
                        "direction": "0",
                        "step":"0"
                      }
                    )


                .with_headers(
                    **{
                        "Content-Type": "application/json",
                        "authenticator":"$token"
                      }
                    )
                .validate()
                .assert_equal("body.message", "网络繁忙")
        ),

    ]


if __name__ == "__main__":
    TestCaseFR3tiaojiao().test_start()