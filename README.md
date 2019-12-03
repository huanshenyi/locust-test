インストール

```text
pip install  locust
```

実行例
```text
locust -f first-test.py --host=https://www.imooc.com/
```
-f :実行ファイルを選択
--host:使用するurlを指定

web画面は開く
`127.0.0.1:8098`

- Number of users to simulate  模擬するユーザーの数
- Hatch rate 秒ごとに起動するユーザーの数


UIなしで実行する
```text
locust -f first-test.py --host=https://www.imooc.com/ --no-web -c 10 -r 2 -t 1m
```
- -f テストスクリプト選択
- --host:指定被测试应用的URL的地址
- --no-web：UIなしで実行 
- -c：模擬ユーザーの数
- -r：毎秒ごとに立ち上げるユーザー
- -t：テストの実行時間

UIに関するパラメタ

```text
locust -f .\load_test.py -P 8999 --host=https://www.imooc.com --web-host=10.2.64.134 
```

- -P portの指定
- --web-host ipホストの指定

```text
locust -f load_test.py --host=https://www.imooc.com --no-web -c 10 -r 2 -t 1m10s --csv=result/load_test20190808_1
```
- csv テスト結果を保存