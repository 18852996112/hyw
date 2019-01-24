import itchat
import requests as rq


def get_msg(text) :
    print ("receive msg:", text)
    info = text['Content'].encode('utf8')
    # Í¼ÁéAPI½Ó¿Ú
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    # ½Ó¿ÚÇëÇóÊý¾Ý
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": str(info)
            }
        },
        "userInfo": {
            "apiKey": "7e6aa600f1c44ed7a36ceb925cd6c849",
            "userId": "18852996112"
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Host': 'openapi.tuling123.com',
        'User-Agent': 'Mozilla/5.0 (Wi`ndows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 '
                      'Safari/537.36 '
    }
    result = rq.post(api_url, headers=headers, json=data).json();
    print("message:", info)
    print("reply:", result)
    return result['results'][0]['values']['text'];


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    itchat.send_msg(get_msg(msg), msg['FromUserName'])
    print()


if __name__ == '__main__':
    #text = input("please input:")
    #print ("text:", text)
    #print(get_msg(text))
    itchat.auto_login(enableCmdQR=2)
    itchat.run()