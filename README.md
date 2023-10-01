# pythonCrawlerExample
> 파이썬 크롤러 예제

- 작성일: 230929
- 최종수정일: 230931
- 메인파일: GenshinImpactWikiCrawler.py

> [원신 위키](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)에서 캐릭터별 이미지 다운로드
- input: 캐릭터 이름 (한글)을 엔터로 구분
- output: 이미지 종류를 폴더명으로해서 하위에 이미지 저장

> 작성 동기
- 업무의 3할이 크롤러/자동화 프로그램이라 퉁쳐서 정리하려고
- 추석연휴에 심심해서
- 클래스 구조에 대한 동경

> 한계 & 추후 과제
- 캐릭터별 속성(영문명, 이미지이름)등을 파일에서 관리함.
  + DB를 만들면 편하겠지만 세팅부터 너무 많은 일이 필요함
- 원신 위키 페이지 로딩 엄청 느리다
- 혼자 대강 쓸거라 오류처리를 제대로 하지 않음
  + 그래도 아직 터진적은 없으니까 괜찮지 않을까 하는 안일함
```python
        for retry in range(5):
            try: doSomeThing()
            except Exception as e: print(e)
            else: break
```
