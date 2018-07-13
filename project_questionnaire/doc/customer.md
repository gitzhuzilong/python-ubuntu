# 客户接口

## 问卷接口

## 创建问卷

method: PUT

api: `/api/v1/customer_questionnaire`

body:
- **title**: 问卷标题
- **expire_date**: 截止时间,格式是:YYYY-MM-DDD,例如:2018-10-20
- **quantity**: 数量
response:
```json
{
    "id":1,//新建的问卷id
}
```

## 更新问卷

method: POST

api: `/api/v1/customer_questionnaire`

body:
- **questionnaire_id**: 问卷id
- **title**: 问卷标题
- **expire_date**: 截止时间,格式是:YYYY-MM-DDD,例如:2018-10-20
- **quantity**: 数量

response:
```json
{
    "msg":"更新成功"
}
```

## 删除问卷

method: DELETE

api: `/api/v1/customer_questionnaire`

body:

- **ids**: 删除的问卷id列表,例如{"ids":[1,2,3,4]}

response:
```json
{
    "deleted_ids":[2,4]//被删除的问卷id列表
}
```

## 获取问卷

method: GET

api: `/api/v1/customer_questionnaire`

params:
- page: 第几页数据,默认1
- limit: 每页数据,默认10
- status: 状态,默认草稿
- with_detail: 是否需要详情,默认False
- id: 问卷id,默认空

response:
```json
{
    "pages":100,//总页数
    "count":888,//问卷总数
    "objs":[//问卷列表
        {
            "id":1,//问卷id
            "title":"测试问卷",//问卷标题
            "quantity":100,//问卷数量
            "free_quantity":100,//剩余问卷数量
            "expire_date":"2018-12-10",//问卷截止日期
            "create_date":"2018-7-4",//问卷创建时间
            "status":0,//问卷状态:0-->草稿,1-->待审核,2-->审核失败,3-->审核通过,4-->已发布
            "customer":{
                "id":1,//客户id
                "name":"千锋",//客户名称
            },
            //假如with_detail参数为True,那么包含以下信息
            "questions":[
                {
                    "id",1,//问题id
                    "title":"问题1",//问题标题
                    "category":"radio",//问题类型,radio为单选,checkbox为多选
                    "items":[
                        {
                            "id":1,//选项id
                            "content":"选项1",//选项内容
                        }
                    ]
                }
                ....
            ],
            "comments":[//批注信息
                {
                "id":1,//批注id
                "create_date":"2018-7-5",//批注日期
                "content":"测试批注不通过",//批注内容
                }
                .....
            ]
        }
        ....
    ]
}
```

## 创建题目

method: PUT

api: `/api/v1/customerquestion/`

body: 
- **title**: 题目标题
- **category**: radio或者checkbox
- **questionnaire_id**: 问卷id
- **items**:["选项1", "选项2", "选项3"]

response:
```json
{
    "id": 1,//题目id
}
```
## 更新题目

method: POST

api: `/api/v1/customerquestion/`

body: 
- **title**: 题目标题
- **category**: radio或者checkbox
- **question_id**: 题目id
- **items**:["选项1", "选项2", "选项3"]

response:
```json
{
    "msg": "更新成功"
}
```

## 删除问题

method: DELETE

api: `/api/v1/customerquestion/`

body:

-**ids**: 问题列表,例如:[1,2,3,4]

response:
```json
{
    "deleted_ids": [2,4],//被删除的问题id列表
}
```

## 创建题目选项

method: PUT

api: `/api/v1/customerquestionitem`

body:
- **content**: 题目选项
- **question_id**: 题目id
- **questionnaire_id**: 问卷id

## 问卷状态

### 修改问卷状态

method: POST

api: `/api/v1/questionnaire_state`

body:
- **id**: 问卷id
- **state**: 问卷状态

> 本接口用于：
> - 问卷提交审核：将问卷状态改为1,
> - 问卷发布：将问卷状态改为4

response：
```json
{
    "msg":"修改成功"
}
```

## 客户发起支付请求

method:PUT

api:`/api/v1/payment`

body:
- **amount**://金额

response：
```json
{
    "qrcode":"",//支付信息二维码图片的base64编码，使用方式<img src="data:image/png;base64,">
}
```

## 客户钱包流水

method: GET

api:`/api/v1/customer_wallet_flow`

body:
- page: 第几页,默认1
- limit：每页数量,默认10
- category：流水类型,false代表消费,true代表支付

response：
```json
[
    {
        "create_date":"2018-01-01",
        "amount":100,
        "reason":"支付宝扫码支付",//原因
        "state":false,//false,未完成,true,已完成
        "category":false,//类型
    }
    .....
]
```

