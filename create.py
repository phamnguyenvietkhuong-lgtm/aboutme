import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docs = [
{
"name": "陳武林",
"mail": "wlchen@pu.edu.tw",
"lab": 665
},
{
"name": "王耀德",
"mail": "ytwang@pu.edu.tw",
"lab": 686
},
{
"name": "康贊清",
"mail": "tckang@pu.edu.tw",
"lab": 783
}
]
collection_ref = db.collection("靜宜資管")
for doc in docs:
 collection_ref.add(doc)
print("已新增:", doc["name"])
print("已成功新增3位老師資料！")
print("請到 Firestore 查看")

