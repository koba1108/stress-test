■シナリオの切り替え方
deployment-master.yaml / deployment-worker.yaml

　env -> TASK_FILE に測定したいシナリオファイル名を指定

　　
■シナリオファイル名
tasks.py　=> ログイン/ログアウト 測定用
seq-tasks.py　=> impression / conversion / click 測定用



■k8sへの適用手順
１．クラスターを作成


２．クラスターへ接続（switch context）
$ gcloud container clusters get-credentials クラスタ名 --zone ゾーン名 --project プロジェクト名
※上記コマンドはGKEのクラスタ詳細ページの「接続」ボタンを押すと表示される。


３．Dockerfileのあるディレクトリへ移動


４．Dockerイメージをビルド => CloudRegistroyへPUSH
gcloud builds submit --tag gcr.io/プロジェクト名/locust-tasks:latest .


５．Deployment登録
＜Master＞
$ kubectl apply -f deployment-master.yaml

＜Worker＞
$ kubectl apply -f deployment-worker.yaml


６．Service登録
kubectl apply -f service.yaml


７．GKE -> サービス に表示されているエンドポイントのport8089のリンクをクリックしてLocustページへ
