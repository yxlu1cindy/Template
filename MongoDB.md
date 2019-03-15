db          #查看当前在哪个数据库    
use foobar  #选择数据库foobar   

> post = {"title" : "My Blog Post", "content" : "Here's my blog post.","date" : new Date()}    
> db.blog.insert(post)    #用insert方法将其保存到blog集合中    

> post.comments = ["good"]   
> db.blog.update({title : "My Blog Post"}, post)   #update新的一个feature    

> db.blog.remove({title : "My Blog Post"})   #删除该document
