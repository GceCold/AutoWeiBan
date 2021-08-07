import weiban
import json
import time  # time.sleep延时
import os  # 兼容文件系统
import random

import fire

tenantCode = '51900002'  # 吉珠院校ID

"""
# 密码登录，已经失效
def pwLogin():
    print(
        '默认院校为吉林大学珠海学院，ID:' + tenantCode + '\n'
        + '若有需要，请自行抓包获取院校ID修改' + '\n'
    )

    # 登录信息输入
    account = input('请输入账号\n')
    password = input('请输入密码\n')

    # 获取Cookies
    print('\n获取Cookies中')
    cookie = WeiBanAPI.getCookie()
    print('Cookies获取成功')
    time.sleep(2)

    randomTimeStamp = random.randint(1E8, 1E12)
    print('验证码,浏览器打开 https://weiban.mycourse.cn/pharos/login/randImage.do?time={}'.format(randomTimeStamp))

    verifyCode = input('请输入验证码')

    # 登录请求
    loginResponse = WeiBanAPI.login(account, password, tenantCode, randomTimeStamp, verifyCode, cookie)
    return loginResponse
"""


class CLI(object):
    def search_tenant(self, tenant_name):
        for tenant_data in weiban.get_tenant_list()['data']:
            if tenant_name in tenant_data['name']:
                print(f"{tenant_data['name']} -> {tenant_data['code']}")

    def qr_mode(self):
        pass

    def token_mode(self, tenant_code, user_id, user_project_id, token):
        """手动输入token登录"""
        # 请求用户信息
        try:
            print('请求用户信息')
            stu_info_response = weiban.getStuInfo(user_id,
                                                  tenant_code)
            print('用户信息：' + stu_info_response['data']['realName'] + '\n'
                  + stu_info_response['data']['orgName']
                  + stu_info_response['data']['specialtyName']
                  )
            time.sleep(2)
        except BaseException:
            print('解析用户信息失败，将尝试继续运行，请注意运行异常')

        # 请求课程完成进度
        try:
            get_progress_response = weiban.getProgress(user_project_id,
                                                       tenant_code)
            print('课程总数：' + str(get_progress_response['data']['requiredNum']) + '\n'
                  + '完成课程：' + str(get_progress_response['data']['requiredFinishedNum']) + '\n'
                  + '结束时间' + str(get_progress_response['data']['endTime']) + '\n'
                  + '剩余天数' + str(get_progress_response['data']['lastDays'])
                  )
            time.sleep(2)
        except BaseException:
            print('解析课程进度失败，将尝试继续运行，请注意运行异常')

        # 请求课程列表
        get_list_course_response = {}
        try:
            get_list_course_response = weiban.getListCourse(user_project_id,
                                                            '3',
                                                            tenant_code,
                                                            '')
            time.sleep(2)
        except BaseException:
            print('请求课程列表失败')

        print('解析课程列表并发送完成请求')

        for i in get_list_course_response['data']:
            print('\n----章节码：' + i['categoryCode'] + '章节内容：' + i['categoryName'])
            courseList = weiban.getCourseListByCategoryCode(i['categoryCode'], user_project_id, user_id, tenant_code)
            for j in courseList['data']:
                print('课程内容：' + j['resourceName'] + '\nuserCourseId:' + j['userCourseId'])

                if (j['finished'] == 1):
                    print('已完成')
                else:
                    print('发送完成请求')
                    weiban.do_study(user_project_id, j['resourceId'], tenant_code, user_id, token=token)
                    time.sleep(10)
                    weiban.finish_course(j['userCourseId'], tenant_code)

                    delayInt = weiban.getRandomTime()
                    print('\n随机延时' + str(delayInt))
                    time.sleep(delayInt)
        print('所有课程完成，若有漏刷，请再次运行')


if __name__ == '__main__':
    fire.Fire(CLI)
