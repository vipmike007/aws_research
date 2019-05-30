# aws_research
此项目为了实现无服务器架构的搜索引擎。目前由后台部分没有问题 用postman 调用  https://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1?key=<模拟输入关键字> 测试

## 设计架构如下。 (dynamoDB+lambda + API Gateway+S3 ）
* dynamoDB (预定义数据库如下）
  * Name    Results
  * mike    resultsmike
  * mike2   resultmike2
  * test1   resultstest1
  * test2   resultstest2

* lambda 
  * 对api gateway过来的event 请求处理并且并且返回对应的信息
  * 根据关键字去 dynamoDB  查找返回需要的结果

*  api gateway - API 管理和转发请求
https://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1?key=test

*  S3 静态页面去调用 （实现，不能确定是api的原因还是js的原因，我把我所有的测试结果说下）

## 测试结果
目前只能通过postman 去做后台的调用，是成功的。
* postman method- post  ,
url - https://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1?key=test  (key=test模拟的输入test的情况）
如下返回值
```
{
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*"
    },
    "body": "hello:['test2', 'test1']"
}
* 注意 test2 和 test1是从dynomoDB取出的模拟联想输入的值
```

* 通过index.html
如下代码总是有问题（暂时没用keyup因为还在debug问题
```
            function myFunction() {
                var xhttp = new XMLHttpRequest();
                var linkDataProperty = document.getElementById("linkDataProperty");
                var searchstring = linkDataProperty.value;
                var ep = "https://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1";
                var url = ep+"?key="+searchstring;
                xhttp.onreadystatechange = function() {
                    if (xhttp.readyState == 4 ) {
                        if (xhttp.status == 200) {
                                var propertiesXML = xhttp.responseText;
                                document.getElementById("my-demo").innerHTML = xhttp.responseText;
                        }
                        else {
                                document.getElementById("my-demo").innerHTML = xhttp.responseText;
                        }
                    }
                    else {
                        document.getElementById("my-demo").innerHTML = xhttp.responseBody; 
                    }
                }
                xhttp.open("POST", url, true);
                xhttp.send();

            }
```            

## 关于index.html 不能正常得到返回值（地址http://bucketdemo05302.s3-website-us-east-1.amazonaws.com/)
  1. 当用js 调用https://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1?key=test get或者post方法
  xhttp.readystatus=2& xhttp.status=0以后就不往后走了，所以一直不能获得responseText的值。但是lambda log看到调用也是成功的，没有错误信息
  2. 把参数去掉，当用js 调用https://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1 （不佳key=xxx,也就是说不读取文本框的内容）
  xhttp.readystatus=4& xhttp.status=200 没有问题
  3. 用postman 去调用 ttps://ahubh52730.execute-api.us-east-1.amazonaws.com/default/Test1?key=test -没有任何问题，可以返回从dynamodb取出的值
  4. 我没有前端经验，debug了两天也没找到原因，如果有兴趣可以一起
