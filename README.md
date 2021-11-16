# Simple-NaverForm-Checker
간단하게 대충 만든 네이버 폼을 채워주는 파이썬 코드입니다.
## NaverForm-Checker 사용 절차
```python
driver = naver_form.getDriver(url)
```
1. 해당 url의 웹드라이버를 얻어옵니다.

```python
naver_form.insertForm(driver, 1, "벤자민 커비 테니슨")
```
2. 폼을 채웁니다.

```python
naver_form.submit(driver)
...
print("result = " + naver_form.isSubmit(driver))
```
3. 제출 버튼을 눌러 제출되었는지 확인합니다.

```python
naver_form.close(driver)
```
4. 웹드라이버를 해제합니다.

## `naver_form.insertForm` 설명
```python
naver_form.insertForm(웹드라이버, itemid, 입력할 값)
```
### itemid
`div`객체 중 id가 formItem으로 진행하는 객체의 `itemid`값을 작성하면 됩니다.
(주의! 폼의 순서대로 `itemId`가 할당되어있지 않음) (언젠간 수정할 예정입니다.)

### 입력할 값
해당 폼에 입력할 값을 작성합니다. `str`의 형태로 넣는 것을 추천드립니다.
아래는 폼의 종류(`class`)에 따른 입력값입니다.
* `formItemPh text` : 입력값이 그대로 작성됩니다.
* `formItemPh singleChoice vertical` : 입력값과 일치하는 값을 선택합니다.
