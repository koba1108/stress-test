## ローカル環境作成

```bash
docker-compose up
```
　　
## シナリオファイル名と内容

asp-tasks.py　=> ログイン後に各画面を定期的に移動
i-tasks.py　=> impression, conversion, clickのAPIを呼び出す
marchant-tasks.py　=> ログイン後に各画面を定期的に移動
partner-tasks.py　=> ログイン後に各画面を定期的に移動

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
docker build -t gcr.io/${your_project_name}/locust-tasks:latest .
docker push gcr.io/${your_project_name}/locust-tasks:latest
```

5. kubectl apply でクラスタに反映
```
$ kubectl apply -f k8s/configMap.yaml
$ kubectl apply -f k8s/asp/
$ kubectl apply -f k8s/i/
$ kubectl apply -f k8s/marchant/
$ kubectl apply -f k8s/partner/
```

7. GKE -> サービスに表示されているグローバルIPにアクセス
