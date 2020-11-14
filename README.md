# send_smart
QNAP NAS上LXCを作成して、LXC上から実行する。

## QNAP NAS ホスト

`/tmp/smart/`フォルダに

- smart_0_1.info
- smart_0_2.info

があるので、LXCでの実行時間直前にshareフォルダにコピーする。  
コピーコマンドをcrontabに追記する。  
下記は例、コピー先はどこでもいい。
send_smartは6時に実行するので、コピーは5時55分にしている。  
`55 5 * * * cp /tmp/smart/*.info /share/Web/smart/`  
QNAP NASでのcrontab設定は[こちら](https://wiki.qnap.com/wiki/Add_items_to_crontab)。

## LXC
 ContainerStationの該当LXCの設定から、上記のコピー先をマウントしておく。

![mnt](https://user-images.githubusercontent.com/47170845/99150055-4c01ad80-26d5-11eb-90cc-855b1223136f.png) 

LXCのcronに設定する。  
`0 6 * * * /home/ubuntu/apps/send_smart/run.sh`

## Sample
ステータスが0じゃないときはたぶんエラーなので赤くしている。

![example](https://user-images.githubusercontent.com/47170845/99150672-75243d00-26d9-11eb-87ec-a7e8068def9c.png)

