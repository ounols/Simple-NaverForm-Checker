import time
import naver_form

if __name__ == '__main__':
    print("Naver form")

    file = open("info.txt", "r", encoding='utf8')
    strings = file.readlines()
    file.close()

    url = strings[0]
    driver = naver_form.getDriver(url)

    naver_form.insertForm(driver, 1, strings[1])
    time.sleep(2)
    naver_form.insertForm(driver, 2, strings[2])
    time.sleep(2)
    naver_form.insertForm(driver, 3, strings[3])
    time.sleep(2)
    naver_form.insertForm(driver, 4, "아니오")
    time.sleep(2)
    naver_form.insertForm(driver, 5, "예")
    time.sleep(2)
    naver_form.insertForm(driver, 6, strings[4])
    time.sleep(2)
    naver_form.insertForm(driver, 7, "아니오")
    time.sleep(2)
    naver_form.insertForm(driver, 9, "아니오")
    time.sleep(2)
    naver_form.insertForm(driver, 11, "확인하였음")
    time.sleep(2)
    naver_form.submit(driver)
    time.sleep(2)
    print("result = " + naver_form.isSubmit(driver))
    time.sleep(2)
    naver_form.close(driver)



