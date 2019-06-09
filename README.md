## シナリオの切り替え方

deployment-master.yaml / deployment-worker.yaml
```
　env -> TASK_FILE に測定したいシナリオファイル名を指定
```
　　
## シナリオファイル名

tasks.py　=> ログイン/ログアウト 測定用

seq-tasks.py　=> impression / conversion / click 測定用



## k8sへの適用手順
1. クラスターを作成
2. クラスターへ接続（switch context）
```bash
$ gcloud container clusters get-credentials クラスタ名 --zone ゾーン名 --project プロジェクト名
```
※ 上記コマンドはGKEのクラスタ詳細ページの「接続」ボタンを押すと表示される。
3. Dockerfileのあるディレクトリへ移動
4. Dockerイメージをビルド => CloudRegistryへPUSH
```bash
$ gcloud builds submit --tag gcr.io/プロジェクト名/locust-tasks:latest .
```

5. Deployment登録
```
＜Master＞
$ kubectl apply -f deployment-master.yaml

＜Worker＞
$ kubectl apply -f deployment-worker.yaml
```

6. Service登録
```bash
$ kubectl apply -f service.yaml
```


7. GKE -> サービス に表示されているエンドポイントのport8089のリンクをクリックしてLocustページへ
